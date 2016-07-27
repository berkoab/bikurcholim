import collections
import datetime
from datetime import date
import time
from datetime import datetime
from bikurcholim.models import HousingSchedule
from django.core.urlresolvers import reverse_lazy

def getCols():
    href = "<a href=" + str(reverse_lazy('housingschedule')) + "{0} class='userId'>{0}</a>"
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
    cols['house'] = {
        'index': 2,
        'type': "string",
        'friendly': "House",
        'tooltip': "Click here to sort"
    }
    cols['apt'] = {
        'index': 3,
        'type': "string",
        'friendly': "Apt",
        'tooltip': "Click here to sort"
    }
    cols['client'] = {
        'index': 4,
        'type': "string",
        'friendly': "Client",
        'tooltip': "Click here to sort"
    }
    cols['from_date'] = {
        'index': 5,
        'type': "date",
        'friendly': "From Date",
        'tooltip': "Click here to sort"
    }
    cols['to_date'] = {
        'index': 6,
        'type': "date",
        'friendly': "To Date",
        'tooltip': "Click here to sort"
    }
    cols['days'] = {
        'index': 7,
        'type': "number",
        'friendly': "Days",
        'tooltip': "Click here to sort"
    }
    cols['notes'] = {
        'index': 8,
        'type': "string",
        'friendly': "Notes",
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
	
	d = HousingSchedule.objects.all()
	
	for c in d:
		columns = collections.OrderedDict()
		columns['id']=c.id
		if(c.house):
			columns['house']=c.house.name
		else:
			columns['house']=""
		columns['apt']=c.apt
		if(c.case):
			columns['client']=c.case.get_name()
		else:
			columns['client']=""
		columns['from_date']=datetime_to_ms_str(c.from_date)
		columns['to_date']=datetime_to_ms_str(c.to_date)
		columns['days']=c.get_days()
		columns['notes']=c.notes

		rows.append(columns)
	return rows