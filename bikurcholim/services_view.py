import collections
import datetime
from datetime import date
import time
from datetime import datetime
from bikurcholim.models import ClientService
from django.core.urlresolvers import reverse_lazy

def getCols():
    href = "<a href=" + str(reverse_lazy('clientservice')) + "{0} class='userId'>{0}</a>"
    cols = collections.OrderedDict()
    cols['id']={
        'index': 1, #The order this column should appear in the table
        'type': "number", #The type. Possible are string, number, bool, date(in milliseconds).
        'friendly': "<span class='glyphicon glyphicon-user'></span>",  #Name that will be used in header. Can also be any html as shown here.
        'format': href,  #Used to format the data anything you want. Use {0} as placeholder for the actual data.
        'unique': 'true',  #This is required if you want checkable rows, or to use the rowClicked callback. Be certain the values are really unique or weird things will happen.
        'sortOrder': "asc", #Data will initially be sorted by this column. Possible are "asc" or "desc"
        'tooltip': "Unique ID number", #Show some additional info about column
    }
    cols['service'] = {
        'index': 2,
        'type': "string",
        'friendly': "Service",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['number_of_times'] = {
        'index': 3,
        'type': "number",
        'friendly': "Times",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['status'] = {
        'index': 4,
        'type': "string",
        'friendly': "Status",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['client'] = {
        'index': 5,
        'type': "string",
        'friendly': "Client",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['volunteer'] = {
        'index': 6,
        'type': "string",
        'friendly': "Volunteer",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['begin_date'] = {
        'index': 7,
        'type': "date",
        'friendly': "Begin Date",
        'hidden':'true'
    }
    cols['end_date'] = {
        'index': 9,
        'type': "date",
        'friendly': "End Date",
        'hidden':'true'
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
	
	d = ClientService.objects.all()
	
	for c in d:
		columns = collections.OrderedDict()
		columns['id']=c.id
		columns['service']=c.service.service
		columns['number_of_times']=c.number_of_times
		if(c.status):
			columns['status']=c.status.status
		columns['client']=c.client.get_name()
		if(c.volunteer):
			columns['volunteer']=c.volunteer.get_name()
		columns['begin_date']=datetime_to_ms_str(c.begin_date)
		columns['end_date']=datetime_to_ms_str(c.end_date)	

		rows.append(columns)
	return rows