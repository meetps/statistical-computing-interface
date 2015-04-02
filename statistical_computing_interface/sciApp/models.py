# -*- coding: utf-8 -*-
from django.db import models
import os.path
import os
def update_filename(instance, filename):
    path = 'documents'
    completepath=os.path.join('statistical_computing_interface/media/documents/', 'uploaded.csv')
    try:
    	os.remove(completepath)
    except OSError:	
	    pass
    return os.path.join(path, "uploaded.csv")
class Document(models.Model):
    docfile = models.FileField(upload_to=update_filename)