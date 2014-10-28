import collections
import datetime
from datetime import date
import time
from datetime import datetime
from bikurcholim.models import Cases

def getCols():
    cols = collections.OrderedDict()
    cols['id']={
        'index': 1, #The order this column should appear in the table
        'type': "number", #The type. Possible are string, number, bool, date(in milliseconds).
        'friendly': "<span class='glyphicon glyphicon-user'></span>",  #Name that will be used in header. Can also be any html as shown here.
        'format': "<a href='/bikurcholim/cases/{0}' class='userId' target='_blank'>{0}</a>",  #Used to format the data anything you want. Use {0} as placeholder for the actual data.
        'unique': 'true',  #This is required if you want checkable rows, or to use the rowClicked callback. Be certain the values are really unique or weird things will happen.
        'sortOrder': "asc", #Data will initially be sorted by this column. Possible are "asc" or "desc"
        'tooltip': "Unique ID number", #Show some additional info about column
    }
    cols['status'] = {
        'index': 2,
        'type': "string",
        'friendly': "Status",
        'tooltip': "Click here to sort"
    }
    cols['client'] = {
        'index': 3,
        'type': "string",
        'friendly': "Client",
        'tooltip': "Click here to sort"
    }
    cols['volunteer'] = {
        'index': 4,
        'type': "string",
        'friendly': "Volunteer",
        'tooltip': "Click here to sort"
    }
    cols['open_date'] = {
        'index': 5,
        'type': "date",
        'friendly': "Open Date",
        'tooltip': "Click here to sort"
    }
    cols['date_of_service'] = {
        'index': 6,
        'type': "date",
        'friendly': "Date and Time of Service",
        'tooltip': "Click here to sort"
    }
    cols['close_date'] = {
        'index': 7,
        'type': "date",
        'friendly': "Close Date",
        'tooltip': "Click here to sort"
    }
    cols['service'] = {
        'index': 8,
        'type': "string",
        'friendly': "Service",
        'tooltip': "Click here to sort"
    }
    cols['location'] = {
        'index': 9,
        'type': "string",
        'friendly': "Location",
        'tooltip': "Click here to sort"
    }
    cols['description'] = {
        'index': 10,
        'type': "string",
        'friendly': "Description",
        'hidden': 'true'
    }

    return cols

def datetime_to_ms_str(dt):
	if(dt):
		t = time.mktime(dt.timetuple())
		return int(t*1000)
	else:
		return 0

def getRows():
	rows=[]
	
	d = Cases.objects.all()
	
	for cases in d:
		columns = collections.OrderedDict()
		columns['id']=cases.id
		if(cases.status):
			columns['status']=cases.status.status
		if(cases.status.status=='Closed'):
			columns['statusFormat']="<div class='red'>{0}</div>"
		elif(cases.status.status=='Assigned'):
			columns['statusFormat']="<div class='green'>{0}</div>"
		else:
			columns['statusFormat']="<div class='yellow'>{0}</div>"
		columns['client']=cases.client.get_name()
		if (cases.volunteer):
			columns['volunteer']=cases.volunteer.get_name()
		columns['open_date']=datetime_to_ms_str(cases.open_date)
		columns['date_of_service']=datetime_to_ms_str(cases.date_of_service)
		columns['close_date']=datetime_to_ms_str(cases.close_date)
		if(cases.service):
			columns['service']=cases.service.service
		if (cases.location):
			columns['location']=cases.location.name
		columns['description']=cases.description

		rows.append(columns)
	return rows