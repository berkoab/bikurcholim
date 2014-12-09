import collections
import datetime
from datetime import date
import time
from datetime import datetime
from bikurcholim.models import Tasks
from django.core.urlresolvers import reverse_lazy

def getCols():
    href = "<a href=" + str(reverse_lazy('tasks')) + "{0} class='userId'>{0}</a>"
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
    cols['title'] = {
        'index': 2,
        'type': "string",
        'friendly': "Title",
        'tooltip': "Click here to sort"
    }
    cols['status'] = {
        'index': 3,
        'type': "string",
        'friendly': "Status",
        'tooltip': "Click here to sort"
    }
    cols['description'] = {
        'index': 4,
        'type': "string",
        'friendly': "Description",
        'tooltip': "Click here to sort",
	    'hidden':'true'
    }
    cols['due_by'] = {
        'index': 5,
        'type': "date",
        'friendly': "Due By",
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
	
	d = Tasks.objects.all()
	
	for tasks in d:
		columns = collections.OrderedDict()
		columns['id']=tasks.id
		if(tasks.status):
			columns['status']=tasks.status.status
		if(tasks.status.status=='Closed'):
			columns['statusFormat']="<div class='red'>{0}</div>"
		elif(tasks.status.status=='Assigned'):
			columns['statusFormat']="<div class='green'>{0}</div>"
		else:
			columns['statusFormat']="<div class='yellow'>{0}</div>"
		columns['title']=tasks.title
		columns['description']=tasks.description
		columns['due_by']=datetime_to_ms_str(tasks.due_by)

		rows.append(columns)
	return rows