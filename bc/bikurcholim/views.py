from django.http import HttpResponse
from django.shortcuts import render
from bikurcholim.models import Volunteers
from bikurcholim.models import VolunteerOptions
from bikurcholim.models import Clients
from django.core import serializers
import re
import json
import collections
import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the bikurcholim index.")

def volunteers(request):
	cols = {}
	cols['id']={
		'index': 1, #The order this column should appear in the table
		'type': "number", #The type. Possible are string, number, bool, date(in milliseconds).
		'friendly': "Id",  #Name that will be used in header. Can also be any html as shown here.
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
	cols['address'] = {
		'index': 3,
        'type': "string",
        'friendly': "Address",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
    }
	cols['city'] = {
        'index': 4,
        'type': "string",
        'friendly': "City",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
    }
	cols['neighborhood'] = {
        'index': 5,
        'type': "string",
        'friendly': "Neighborhood",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
    }
	cols['work_place'] = {
        'index': 6,
        'type': "string",
        'friendly': "Work Place",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
    }
	cols['medical_training'] = {
        'index': 7,
        'type': "string",
        'friendly': "Medical Training",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['vehicle'] = {
        'index': 8,
        'type': "string",
        'friendly': "Vehicle",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['other_languages'] = {
        'index': 9,
        'type': "string",
        'friendly': "Other Languages",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['other_specialties'] = {
        'index': 10,
        'type': "string",
        'friendly': "Other Specialties",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['start_time_available'] = {
        'index': 11,
        'type': "string",
        'friendly': "Start Time Available",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['end_time_availalable'] = {
        'index': 12,
        'type': "string",
        'friendly': "End Time Available",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['days_and_times_available_notes'] = {
        'index': 13,
        'type': "string",
        'friendly': "Times Notes",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
    }
	
	cols['sunday'] = {
        'index': 14,
        'type': "bool",
        'friendly': "Sunday Avail.",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['monday'] = {
        'index': 15,
        'type': "bool",
        'friendly': "Monday Avail.",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['tuesday'] = {
        'index': 16,
        'type': "bool",
        'friendly': "Tuesday Avail.",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['wednesday'] = {
        'index': 17,
        'type': "bool",
        'friendly': "Wednesday Avail.",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['thursday'] = {
        'index': 18,
        'type': "bool",
        'friendly': "Thursday Avail.",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['friday'] = {
        'index': 19,
        'type': "bool",
        'friendly': "Friday Avail.",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['shabbos'] = {
        'index': 20,
        'type': "bool",
        'friendly': "Shabbos Avail.",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	cols['meal_preparation'] = {
        'index': 21,
        'type': "bool",
        'friendly': "Meal Preparation",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'hidden':'true'
    }
	rows=[]
	
	#data = Volunteers.objects.all()
	#data = Volunteers.objects.all().values_list()
	#for item in data:
	#	re.sub(r'(datetime.time\()(\d+)(,)(\d+)(, )(\d+)(\))', r'\2\\4\\6', item)
	#data = serializers.serialize("json", Volunteers.objects.all())		
	#j = json.loads(data)
	#for item in j:
	#	rows.append(item['fields'])
	
	d = Volunteers.objects.all()
	o = VolunteerOptions.objects.all()
	
	for volunteer in d:
		columns = {}
		columns['id']=volunteer.id
		columns['name']=volunteer.last_name + ', ' + volunteer.first_name
		columns['address']=volunteer.address
		columns['city']=volunteer.city.city
		columns['neighborhood']=volunteer.neighborhood.neighborhood
		columns['work_place']=volunteer.work_place
		columns['medical_training']=volunteer.medical_training
		columns['vehicle']=volunteer.vehicle.vehicle
		columns['other_languages']=volunteer.other_languages
		columns['other_specialties']=volunteer.other_specialties
		columns['start_time_available']=str(volunteer.start_time_available)
		columns['end_time_availalable']=str(volunteer.end_time_availalable)
		columns['days_and_times_available_notes']=volunteer.days_and_times_available_notes
		columns['sunday']=volunteer.sunday
		columns['monday']=volunteer.monday
		columns['tuesday']=volunteer.tuesday
		columns['wednesday']=volunteer.wednesday
		columns['thursday']=volunteer.thursday
		columns['friday']=volunteer.friday
		columns['shabbos']=volunteer.shabbos
		voptions = o.filter(volunteers=volunteer.id)
		
		meal_prep = voptions.filter(option__option='Meal Preparation')
		if(len(meal_prep)>0):
			columns['meal_preparation']=meal_prep[0].has_option
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