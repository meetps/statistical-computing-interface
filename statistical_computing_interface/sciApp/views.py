# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.messages import constants as message_tags
import os.path
import json
import csv
import sqlite3
import time 
from statistical_computing_interface.sciApp import OpenCPU
from statistical_computing_interface.sciApp.models import Document
from statistical_computing_interface.sciApp.forms import DocumentForm

def chooseGraph(request):
	return render_to_response('sciApp/choose_graph.html')

def list(request):
	# Handle file upload
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()
			return HttpResponseRedirect(reverse('statistical_computing_interface.sciApp.views.chooseGraph'))
	else:
		form = DocumentForm() # A empty, unbound form

	# Load documents for the list page
	documents = Document.objects.all()

	# Render list page with the documents and the form
	return render_to_response(
		'sciApp/list.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)

def OpenCPUAnalysis(request):
	x=[5,3,4,1,5,3,5]
	y=[2,4,5,3,6,4,6]
	valuex=OpenCPU.mean(x)
	decodex=valuex.decode()
	mx=decodex[4:-1]
	valuey=OpenCPU.mean(y)
	decodey=valuey.decode()
	my=decodey[4:-1]
	data=[mx,my]
	# temp_dict={"datax":mx,"datay":my}
	# data.append(temp_dict)
	return render_to_response('sciApp/OpenCPUAnalysis.html', {'attributes': data})

def login(request):
	messages.add_message(request,10, 'A serious error occurred.')
	return render_to_response('sciApp/login.html')

def register(request):
	return render_to_response('sciApp/register.html')

def loginStatus(request):
	return HttpResponseRedirect('/sciApp/upload/')

def registerStatus(request):
	email = request.POST.get('InputEmail',False)
	password = request.POST.get('InputPwd',False)
	confirm_password = request.POST.get('InputPwd2',False)
	if password == confirm_password:
		conn=sqlite3.connect('user_database.db')
		conn.execute('''CREATE TABLE IF NOT EXISTS USER_DETAILS( EMAIL_ID CHAR(25), PWD_HASH CHAR(64) );''')
		conn.execute('''INSERT INTO USER_DETAILS( EMAIL_ID, PWD_HASH ) VALUES( ?, ?)''',(email , password))  
		return HttpResponseRedirect('/sciApp/upload/')
	return HttpResponseRedirect('/sciApp/register/')

def readData():
	completeName=os.path.join('statistical_computing_interface/media/documents/', 'uploaded.csv')
	d=[]
	f = open( completeName, 'r' )
	#data is assumed in the form of x and y values which are seperated by comma.
	csv_f = csv.reader(f)
	for row in csv_f:
		row = [int(i) for i in row]
		d.append(row)
	sorted_data=sorted(d,key=lambda tup: tup[1],reverse=True)
	data=[]
	for line in sorted_data:
		temp_dict={"name":line[0] , "data":line[1]}
		data.append(temp_dict)
	f.close()
	return data

def makeLineGraph(request):
	data=readData()
	print (data)
	return render_to_response('sciApp/plot_line.html', {"obj_as_json": json.dumps(data)})

def makeBarGraph(request):
	data=readData()
	print (data)
	return render_to_response('sciApp/plot_bar.html', {"obj_as_json": json.dumps(data)})
