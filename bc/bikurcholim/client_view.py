import collections
from bikurcholim.models import Clients

def getCols():
    cols = collections.OrderedDict()
    cols['id']={
        'index': 1, #The order this column should appear in the table
        'type': "number", #The type. Possible are string, number, bool, date(in milliseconds).
        'friendly': "<span class='glyphicon glyphicon-user'></span>",  #Name that will be used in header. Can also be any html as shown here.
        'format': "<a href='/bikurcholim/clients/{0}' class='userId' target='_blank'>{0}</a>",  #Used to format the data anything you want. Use {0} as placeholder for the actual data.
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
        'index': 4,
        'type': "string",
        'friendly': "Home Phone",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['cell_phone'] = {
        'index': 4,
        'type': "string",
        'friendly': "Cell Phone",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['email_address'] = {
        'index': 4,
        'type': "string",
        'friendly': "Email",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['neighborhood'] = {
        'index': 5,
        'type': "string",
        'friendly': "Neighborhood",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['status'] = {
        'index': 5,
        'type': "string",
        'friendly': "Status",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['start_date'] = {
        'index': 5,
        'type': "string",
        'friendly': "Start Date",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['expected_end_date'] = {
        'index': 5,
        'type': "string",
        'friendly': "Exp. End Date",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['end_date'] = {
        'index': 5,
        'type': "string",
        'friendly': "End Date",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['hospital'] = {
        'index': 5,
        'type': "string",
        'friendly': "Hospital",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['hospital_room'] = {
        'index': 5,
        'type': "string",
        'friendly': "Hospital Room",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['hospital_notes'] = {
        'index': 5,
        'type': "string",
        'friendly': "Hospital Notes",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['tikvah_house'] = {
        'index': 5,
        'type': "string",
        'friendly': "Tikvah House",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['tikvah_room'] = {
        'index': 5,
        'type': "string",
        'friendly': "Tikvah Room",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['food_notes'] = {
        'index': 5,
        'type': "string",
        'friendly': "Food Notes",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['allergies'] = {
        'index': 5,
        'type': "string",
        'friendly': "Allergies",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['transportation'] = {
        'index': 5,
        'type': "string",
        'friendly': "Transportation",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['visitor_comments'] = {
        'index': 5,
        'type': "string",
        'friendly': "Visitor Comments",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['medical_equipment'] = {
        'index': 5,
        'type': "string",
        'friendly': "Medical Equipment",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['donation_made'] = {
        'index': 5,
        'type': "string",
        'friendly': "Donation Made",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['text_ability'] = {
        'index': 5,
        'type': "string",
        'friendly': "Text Ability",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['yoshon'] = {
        'index': 5,
        'type': "string",
        'friendly': "Yoshon",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['cholov_yisroel'] = {
        'index': 5,
        'type': "string",
        'friendly': "Cholov Yisroel",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['food_to_hospital'] = {
        'index': 5,
        'type': "string",
        'friendly': "Food To Hospital",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['food_to_home'] = {
        'index': 5,
        'type': "string",
        'friendly': "Food To Home",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['meal_coordinator'] = {
        'index': 5,
        'type': "string",
        'friendly': "Meal Coordinator",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['meal_preparer'] = {
        'index': 5,
        'type': "string",
        'friendly': "Meal Preparer",
        'tooltip': "Click here to sort", #Show some additional info about column
    }

    return cols
   
def getRows():
	rows=[]
	
	d = Clients.objects.all()
	
	for client in d:
		columns = collections.OrderedDict()
		columns['id']=client.id
		columns['name']=client.get_name()
		columns['address']=client.address
		columns['city']=client.city.city
		columns['neighborhood']=client.neighborhood.neighborhood
		columns['home_phone']=client.home_phone
		columns['cell_phone']=client.cell_phone
		columns['email_address']=client.email_address
		columns['status']=client.status.status
		columns['start_date']=client.start_date
		columns['expected_end_date']=client.expected_end_date
		columns['end_date']=client.end_date
		columns['hospital']=client.hospital
		columns['hospital_room']=client.hospital_room
		columns['hospital_notes']=client.hospital_notes
		columns['tikvah_house']=client.tikvah_house
		columns['tikvah_room']=client.tikvah_room
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
		columns['meal_coordinator']=client.meal_coordinator.get_name()
		columns['meal_preparer']=client.meal_preparer.get_name()		

		rows.append(columns)
	return rows