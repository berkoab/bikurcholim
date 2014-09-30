from django.http import HttpResponse
from django.shortcuts import render
from bikurcholim.models import Volunteers
from bikurcholim.models import Clients
from django.core import serializers
import re
import json
import collections

def index(request):
    return HttpResponse("Hello, world. You're at the bikurcholim index.")

def volunteers(request):
	cols = {}
	cols['id']={
		'index': 1, #The order this column should appear in the table
		'type': "number", #The type. Possible are string, number, bool, date(in milliseconds).
		'friendly': "id",  #Name that will be used in header. Can also be any html as shown here.
		'format': "<a href='#' class='userId' target='_blank'>{0}</a>",  #Used to format the data anything you want. Use {0} as placeholder for the actual data.
		'unique': 'true',  #This is required if you want checkable rows, or to use the rowClicked callback. Be certain the values are really unique or weird things will happen.
		'sortOrder': "asc", #Data will initially be sorted by this column. Possible are "asc" or "desc"
		'tooltip': "This column has an initial filter", #Show some additional info about column
		'filter': "1..400" #Set initial filter.
	}
	cols['name'] = {
		'index': 2,
		'type': "string",
		'friendly': "Name",
		'tooltip': "This column has a custom placeholder", #Show some additional info about column
		'placeHolder': "abc123" #Overrides default placeholder and placeholder specified in data types(row 34).
	}

	rows=[]
	
	#data = Volunteers.objects.all()
	#data = Volunteers.objects.all().values_list()
	#for item in data:
	#	re.sub(r'(datetime.time\()(\d+)(,)(\d+)(, )(\d+)(\))', r'\2\\4\\6', item)
	data = serializers.serialize("json", Volunteers.objects.all())		
	j = json.loads(data)
	#for item in j:
	#	rows.append(item['fields'])
	
	d = Volunteers.objects.all()
	columns = {}
	columns['id']=d[0].id
	columns['name']=d[0].first_name
	rows.append(columns)
	r = collections.OrderedDict()
	r['cols'] = cols
	r['rows'] = rows
	
	context = {'volunteers': json.dumps(r)}
	return render(request, 'bikurcholim/volunteers.html', context)

def clients(request):
	data = Clients.objects.all()
	context = {'clients': data[0]['fields']}
	return render(request, 'bikurcholim/clients.html', context)