from django.http import HttpResponse
from django.shortcuts import render
from bikurcholim.models import Volunteers
from bikurcholim.models import Clients

def index(request):
    return HttpResponse("Hello, world. You're at the bikurcholim index.")

def volunteers(request):
	cols = {}
	cols['id']={
		'index': 1, #The order this column should appear in the table
		'type': "number", #The type. Possible are string, number, bool, date(in milliseconds).
		'friendly': "<span class='glyphicon glyphicon-user'></span>",  #Name that will be used in header. Can also be any html as shown here.
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
	
	
	data = Volunteers.objects.all()
	
	r = {}
	r['cols'] = cols
	r['rows'] = data
	
	context = {'volunteers': r}
	return render(request, 'bikurcholim/volunteers.html', context)

def clients(request):
	data = Clients.objects.all()
	context = {'clients': data}
	return render(request, 'bikurcholim/clients.html', context)