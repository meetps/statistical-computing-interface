import urllib.request
#data to be sent to server
#define data here
def mean(x):
	w=[]
	for i in range(len(x)):
		w.append(1)
	data="x="+str(x)+"&w="+str(w)
	byte = str.encode(data)
	req = urllib.request.Request('https://public.opencpu.org/ocpu/library/stats/R/weighted.mean',byte)
	res = urllib.request.urlopen(req)
	t= res.readline()
	decode=t.decode()
	source='https://public.opencpu.org'+decode[:-1]+'/print';
	response = urllib.request.urlopen(source)
	return response.read()