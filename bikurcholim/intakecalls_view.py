import collections
import datetime
from datetime import date
import time
from datetime import datetime
from bikurcholim.models import IntakeCalls
from django.core.urlresolvers import reverse_lazy

def getCols():
    cols = collections.OrderedDict()
    href = "<a href=" + str(reverse_lazy('intakecalls')) + "{0} class='userId'>{0}</a>"
    cols['id']={
        'index': 1, #The order this column should appear in the table
        'type': "number", #The type. Possible are string, number, bool, date(in milliseconds).
        'friendly': "<span class='glyphicon glyphicon-user'></span>",  #Name that will be used in header. Can also be any html as shown here.
        'format': href,  #Used to format the data anything you want. Use {0} as placeholder for the actual data.
        'unique': 'true',  #This is required if you want checkable rows, or to use the rowClicked callback. Be certain the values are really unique or weird things will happen.
        'sortOrder': "asc", #Data will initially be sorted by this column. Possible are "asc" or "desc"
        'tooltip': "Unique ID number", #Show some additional info about column
    }
    cols['name'] = {
        'index': 2,
        'type': "string",
        'friendly': "Name",
        'tooltip': "Click here to sort"
    }

    cols['date_call_received'] = {
        'index': 3,
        'type': "date",
        'friendly': "Open Date",
        'tooltip': "Click here to sort"
    }
    cols['initiating_phone_number'] = {
        'index': 4,
        'type': "string",
        'friendly': "Initiating Phone Number",
        'tooltip': "Click here to sort"
    }
    cols['initiating_name'] = {
        'index': 5,
        'type': "string",
        'friendly': "Initiating Name",
        'tooltip': "Click here to sort"
    }
    cols['service'] = {
        'index': 6,
        'type': "string",
        'friendly': "Service",
        'tooltip': "Click here to sort"
    }
    cols['hospital'] = {
        'index': 7,
        'type': "string",
        'friendly': "Location",
        'tooltip': "Click here to sort"
    }
    cols['city'] = {
        'index': 8,
        'type': "string",
        'friendly': "City",
        'tooltip': "Click here to sort"
    }
    cols['description'] = {
        'index': 9,
        'type': "string",
        'friendly': "Description",
        'hidden': 'true'
    }
    cols['made_into_case'] = {
        'index': 10,
        'type': "string",
        'friendly': "Made Into Case",
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
	
	d = IntakeCalls.objects.all()
	
	for cases in d:
		columns = collections.OrderedDict()
		columns['id']=cases.id
		columns['name'] = cases.get_name()
		columns['date_call_received']=datetime_to_ms_str(cases.date_call_received)
		columns['initiating_phone_number']=cases.initiating_phone_number
		columns['initiating_name']=cases.initiating_name
		if(cases.service):
			columns['service']=cases.service.service
		else:
			columns['service']=""
		if (cases.hospital):
			columns['hospital']=cases.hospital.name
		else:
			columns['hospital']=""
		if(cases.city):
			columns['city']=cases.city.city
		else:
			columns['city']=""
		if(cases.made_into_case):
			columns['made_into_case']=cases.made_into_case.status
		else:
			columns['made_into_case']=""
		columns['description']=cases.description

		rows.append(columns)
	return rows