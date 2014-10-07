import collections
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
        'tooltip': "This column has an initial filter", #Show some additional info about column
        'filter': "1..400" #Set initial filter.
    }
    cols['status'] = {
        'index': 2,
        'type': "string",
        'friendly': "Status",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
        'placeHolder': "abc123" #Overrides default placeholder and placeholder specified in data types(row 34).
    }
    cols['client'] = {
        'index': 3,
        'type': "string",
        'friendly': "Client",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
    }
    cols['volunteer'] = {
        'index': 4,
        'type': "string",
        'friendly': "Volunteer",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
    }
    cols['description'] = {
        'index': 5,
        'type': "string",
        'friendly': "Description",
        'tooltip': "This column has a custom placeholder", #Show some additional info about column
    }
    
    return cols
   
def getRows():
	rows=[]
	
	d = Cases.objects.all()
	
	for cases in d:
		columns = collections.OrderedDict()
		columns['id']=cases.id
		columns['status']=cases.status.status
		columns['client']=cases.client.last_name
		columns['volunteer']=cases.volunteer.last_name
		columns['description']=cases.description

		rows.append(columns)
	return rows