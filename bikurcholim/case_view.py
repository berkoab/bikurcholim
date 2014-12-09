import collections
import datetime
from datetime import date
import time
from datetime import datetime
from bikurcholim.models import Cases
from django.core.urlresolvers import reverse_lazy

def getCols():
    cols = collections.OrderedDict()
    href = "<a href=" + str(reverse_lazy('cases')) + "{0} class='userId'>{0}</a>"
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
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['address'] = {
        'index': 3,
        'type': "string",
        'friendly': "Address",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['city'] = {
        'index': 4,
        'type': "string",
        'friendly': "City",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['home_phone'] = {
        'index': 5,
        'type': "string",
        'friendly': "Home Phone",
        'tooltip': "Click here to sort", #Show some additional info about column
		'hidden':'true'
    }
    cols['cell_phone'] = {
        'index': 6,
        'type': "string",
        'friendly': "Cell Phone",
        'tooltip': "Click here to sort", #Show some additional info about column
		'hidden':'true'
    }
    cols['email_address'] = {
        'index': 7,
        'type': "string",
        'friendly': "Email",
        'tooltip': "Click here to sort", #Show some additional info about column
		'hidden':'true'
    }
    cols['neighborhood'] = {
        'index': 8,
        'type': "string",
        'friendly': "Neighborhood",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['status'] = {
        'index': 9,
        'type': "string",
        'friendly': "Status",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['start_date'] = {
        'index': 10,
        'type': "date",
        'friendly': "Start Date",
        'hidden':'true'
    }
    cols['expected_end_date'] = {
        'index': 11,
        'type': "date",
        'friendly': "Exp. End Date",
        'hidden':'true'
    }
    cols['end_date'] = {
        'index': 12,
        'type': "date",
        'friendly': "End Date",
        'hidden':'true'
    }
    cols['hospital'] = {
        'index': 13,
        'type': "string",
        'friendly': "Hospital",
        'hidden':'true'
    }
    cols['hospital_room'] = {
        'index': 14,
        'type': "string",
        'friendly': "Hospital Room",
        'hidden':'true'
    }
    cols['hospital_notes'] = {
        'index': 15,
        'type': "string",
        'friendly': "Hospital Notes",
        'hidden':'true'
    }
    cols['food_notes'] = {
        'index': 16,
        'type': "string",
        'friendly': "Food Notes",
        'hidden':'true'
    }
    cols['allergies'] = {
        'index': 17,
        'type': "string",
        'friendly': "Allergies",
        'hidden':'true'
    }
    cols['transportation'] = {
        'index': 18,
        'type': "string",
        'friendly': "Transportation",
        'hidden':'true'
    }
    cols['visitor_comments'] = {
        'index': 19,
        'type': "string",
        'friendly': "Visitor Comments",
        'hidden':'true'
    }
    cols['medical_equipment'] = {
        'index': 20,
        'type': "string",
        'friendly': "Medical Equipment",
        'hidden':'true'
    }
    cols['donation_made'] = {
        'index': 21,
        'type': "string",
        'friendly': "Donation Made",
        'hidden':'true'
    }
    cols['text_ability'] = {
        'index': 22,
        'type': "bool",
        'friendly': "Text Ability",
        'hidden':'true'
    }
    cols['yoshon'] = {
        'index': 23,
        'type': "bool",
        'friendly': "Yoshon",
        'hidden':'true'
    }
    cols['cholov_yisroel'] = {
        'index': 24,
        'type': "bool",
        'friendly': "Cholov Yisroel",
        'hidden':'true'
    }
    cols['food_to_hospital'] = {
        'index': 25,
        'type': "bool",
        'friendly': "Food To Hospital",
        'hidden':'true'
    }
    cols['food_to_home'] = {
        'index': 26,
        'type': "bool",
        'friendly': "Food To Home",
        'hidden':'true'
    }
    cols['meal_coordinator'] = {
        'index': 27,
        'type': "string",
        'friendly': "Meal Coordinator",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['meal_preparer'] = {
        'index': 28,
        'type': "string",
        'friendly': "Meal Preparer",
        'tooltip': "Click here to sort", #Show some additional info about column
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
	
	for client in d:
		columns = collections.OrderedDict()
		columns['id']=client.id
		columns['name']=client.get_name()
		columns['address']=client.address
		if(client.city):
			columns['city']=client.city.city
		if(client.neighborhood):
			columns['neighborhood']=client.neighborhood.neighborhood
		columns['home_phone']=client.home_phone
		columns['cell_phone']=client.cell_phone
		columns['email_address']=client.email_address
		if(client.status):
			columns['status']=client.status.status
		columns['start_date']=datetime_to_ms_str(client.start_date)
		columns['expected_end_date']=datetime_to_ms_str(client.expected_end_date)
		columns['end_date']=datetime_to_ms_str(client.end_date)
		if(client.hospital):
			columns['hospital']=client.hospital.name
		columns['hospital_room']=client.hospital_room
		columns['hospital_notes']=client.hospital_notes
		columns['food_notes']=client.food_notes
		columns['allergies']=client.allergies
		columns['transportation']=client.transportation
		columns['visitor_comments']=client.visitor_comments
		columns['medical_equipment']=client.medical_equipment
		columns['donation_made']=client.donation_made
		columns['text_ability']=client.text_ability
		columns['yoshon']=client.yoshon
		columns['cholov_yisroel']=client.cholov_yisroel
		columns['food_to_hospital']=client.food_to_hospital
		columns['food_to_home']=client.food_to_home
		if(client.meal_coordinator):
			columns['meal_coordinator']=client.meal_coordinator.get_name()
		if(client.meal_preparer):
			columns['meal_preparer']=client.meal_preparer.get_name()		

		rows.append(columns)
	return rows