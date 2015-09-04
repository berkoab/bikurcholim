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
    cols['hospital'] = {
		'index': 3,
		'type': "string",
		'friendly': "Hospital",
		'hidden':'true'
	}
    cols['hospital_room'] = {
		'index': 4,
		'type': "string",
		'friendly': "Hospital Room",
		'hidden':'true'
	}
    cols['other_location'] = {
		'index': 5,
		'type': "string",
		'friendly': "Other Location",
		'hidden':'true'
	}
    cols['medical_condition'] = {
		'index': 6,
		'type': "string",
		'friendly': "Medical Condition",
		'hidden':'true'
	}
    cols['address'] = {
        'index': 7,
        'type': "string",
        'friendly': "Address",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['city'] = {
        'index': 8,
        'type': "string",
        'friendly': "City",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['home_phone'] = {
        'index': 9,
        'type': "string",
        'friendly': "Home Phone",
        'tooltip': "Click here to sort", #Show some additional info about column
		'hidden':'true'
    }
    cols['cell_phone'] = {
        'index': 10,
        'type': "string",
        'friendly': "Cell Phone",
        'tooltip': "Click here to sort", #Show some additional info about column
		'hidden':'true'
    }
    cols['email_address'] = {
        'index': 11,
        'type': "string",
        'friendly': "Email",
        'tooltip': "Click here to sort", #Show some additional info about column
		'hidden':'true'
    }
    cols['neighborhood'] = {
        'index': 12,
        'type': "string",
        'friendly': "Neighborhood",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['status'] = {
        'index': 13,
        'type': "string",
        'friendly': "Status",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['case_manager'] = {
        'index': 14,
        'type': "string",
        'friendly': "Case Manager",
        'tooltip': "Click here to sort", #Show some additional info about column
        'hidden':'true'
    }
    cols['original_start_date'] = {
        'index': 15,
        'type': "date",
        'friendly': "Orig. Start Date",
        'hidden':'true'
    }
    cols['active_start_date'] = {
        'index': 16,
        'type': "date",
        'friendly': "Act. Start Date",
        'hidden':'true'
    }
    cols['expected_end_date'] = {
        'index': 17,
        'type': "date",
        'friendly': "Exp. End Date",
        'hidden':'true'
    }
    cols['inactive_date'] = {
        'index': 18,
        'type': "date",
        'friendly': "Inactive Date",
        'hidden':'true'
    }
    cols['end_date'] = {
        'index': 19,
        'type': "date",
        'friendly': "End Date",
        'hidden':'true'
    }
    cols['hospital_notes'] = {
        'index': 20,
        'type': "string",
        'friendly': "Hospital Notes",
        'hidden':'true'
    }
    cols['food_notes'] = {
        'index': 21,
        'type': "string",
        'friendly': "Food Notes",
        'hidden':'true'
    }
    cols['transportation'] = {
        'index': 22,
        'type': "string",
        'friendly': "Transportation",
        'hidden':'true'
    }
    cols['visitor_comments'] = {
        'index': 23,
        'type': "string",
        'friendly': "Visitor Comments",
        'hidden':'true'
    }
    cols['medical_equipment'] = {
        'index': 24,
        'type': "string",
        'friendly': "Medical Equipment",
        'hidden':'true'
    }
    cols['donation_made'] = {
        'index': 25,
        'type': "string",
        'friendly': "Donation Made",
        'hidden':'true'
    }
    cols['text_ability'] = {
        'index': 26,
        'type': "bool",
        'friendly': "Text Ability",
        'hidden':'true'
    }
    cols['text_ability_notes'] = {
        'index': 27,
        'type': "bool",
        'friendly': "Text Ability Notes",
        'hidden':'true'
    }
    cols['food_to_hospital'] = {
        'index': 28,
        'type': "bool",
        'friendly': "Food To Hospital",
        'hidden':'true'
    }
    cols['food_to_hospital_notes'] = {
		'index': 29,
		'type': "string",
		'friendly': "Food to Hospital Notes",
		'hidden':'true'
	}
    cols['food_to_home'] = {
        'index': 30,
        'type': "bool",
        'friendly': "Food To Home",
        'hidden':'true'
    }
    cols['food_to_home_notes'] = {
		'index': 31,
		'type': "string",
		'friendly': "Food to Home Notes",
		'hidden':'true'
	}
    cols['housing_checkbox'] = {
        'index': 32,
        'type': "bool",
        'friendly': "Housing?",
        'hidden':'true'
    }
    cols['housing_notes'] = {
		'index': 33,
		'type': "string",
		'friendly': "Housing? Notes",
		'hidden':'true'
	}
    cols['transportation_checkbox'] = {
        'index': 34,
        'type': "bool",
        'friendly': "Transportation?",
        'hidden':'true'
    }
    cols['transportation_notes'] = {
		'index': 35,
		'type': "string",
		'friendly': "Transportation Notes",
		'hidden':'true'
	}
    cols['respite_in_home'] = {
        'index': 36,
        'type': "bool",
        'friendly': "Respite in Home",
        'hidden':'true'
    }
    cols['respite_in_home_notes'] = {
        'index': 37,
        'type': "string",
        'friendly': "Respite in Home Notes",
        'hidden':'true'
    }
    cols['cleaning_in_home'] = {
        'index': 38,
        'type': "bool",
        'friendly': "Cleaning in Home",
        'hidden':'true'
    }
    cols['cleaning_in_home_notes'] = {
        'index': 39,
        'type': "string",
        'friendly': "Cleaning in Home Notes",
        'hidden':'true'
    }
    cols['other'] = {
        'index': 40,
        'type': "bool",
        'friendly': "Other Options",
        'hidden':'true'
    }
    cols['other_notes'] = {
		'index': 41,
		'type': "string",
		'friendly': "Other Options Notes",
		'hidden':'true'
	}
    cols['general_notes'] = {
        'index': 42,
        'type': "string",
        'friendly': "General Notes",
        'hidden':'true'
    }
    cols['meal_coordinator'] = {
        'index': 43,
        'type': "string",
        'friendly': "Meal Coordinator",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['meal_preparer'] = {
        'index': 44,
        'type': "string",
        'friendly': "Meal Preparer",
        'tooltip': "Click here to sort", #Show some additional info about column
    }
    cols['phones'] = {
        'index': 45,
        'type': "string",
        'friendly': "Phones",
        'tooltip': "Click here to sort", #Show some additional info about column
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
	
	d = Cases.objects.all()
	
	for client in d:
		columns = collections.OrderedDict()
		columns['id']=client.id
		columns['name']=client.get_name()
		if(client.hospital):
			columns['hospital']=client.hospital.name
		else:
			columns['hospital']=""
		columns['hospital_room']=client.hospital_room
		columns['other_location']=client.other_location
		columns['medical_condition']=client.medical_condition
		columns['address']=client.address
		if(client.city):
			columns['city']=client.city.city
		else:
			columns['city']=""
		columns['home_phone']=client.home_phone
		columns['cell_phone']=client.cell_phone
		columns['email_address']=client.email_address
		if(client.neighborhood):
			columns['neighborhood']=client.neighborhood.neighborhood
		else:
			columns['neighborhood']=""
		if(client.status):
			columns['status']=client.status.status
		else:
			columns['status']=""
		if(client.case_manager):
			columns['case_manager']=client.case_manager.get_name()
		else:
			columns['case_manager']=""
		columns['original_start_date']=datetime_to_ms_str(client.original_start_date)
		columns['active_start_date']=datetime_to_ms_str(client.active_start_date)
		columns['expected_end_date']=datetime_to_ms_str(client.expected_end_date)
		columns['inactive_date']=datetime_to_ms_str(client.inactive_date)
		columns['end_date']=datetime_to_ms_str(client.end_date)
		columns['hospital_notes']=client.hospital_notes
		columns['food_notes']=client.food_notes
		columns['transportation']=client.transportation
		columns['visitor_comments']=client.visitor_comments
		columns['medical_equipment']=client.medical_equipment
		columns['donation_made']=client.donation_made
		columns['text_ability']=client.text_ability
		columns['text_ability_notes']=client.text_ability_notes
		columns['food_to_hospital']=client.food_to_hospital
		columns['food_to_hospital_notes']=client.food_to_hospital_notes
		columns['food_to_home']=client.food_to_home
		columns['food_to_home_notes']=client.food_to_home_notes
		columns['housing_checkbox']=client.housing_checkbox
		columns['housing_notes']=client.housing_notes
		columns['transportation_checkbox']=client.transportation
		columns['transportation_notes']=client.transportation_notes
		columns['respite_in_home']=client.respite_in_home
		columns['respite_in_home_notes']=client.respite_in_home_notes
		columns['cleaning_in_home']=client.cleaning_in_home
		columns['cleaning_in_home_notes']=client.cleaning_in_home_notes
		columns['other']=client.other
		columns['other_notes']=client.other_notes
		columns['general_notes']=client.general_notes
		if(client.meal_coordinator):
			columns['meal_coordinator']=client.meal_coordinator.get_name()
		else:
			columns['meal_coordinator']=""
		if(client.meal_preparer):
			columns['meal_preparer']=client.meal_preparer.get_name()
		else:
			columns['meal_preparer']=""
        phones = ""
        for n in client.phones_set.all():
			phones=phones+n.number+'|'
        columns['phones'] = phones[:-1]
        rows.append(columns)
	return rows