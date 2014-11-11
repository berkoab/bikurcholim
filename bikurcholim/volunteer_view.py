import collections
from bikurcholim.models import Clients, Volunteers
from django.core.urlresolvers import reverse_lazy

def getCols():
    href = "<a href=" + str(reverse_lazy('volunteers')) + "{0} class='userId' target='_blank'>{0}</a>"
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
    cols['name'] = {
        'index': 2,
        'type': "string",
        'friendly': "Name",
        'tooltip': "Click here to sort"
    }
    cols['address'] = {
        'index': 3,
        'type': "string",
        'friendly': "Address",
        'tooltip': "Click here to sort"
    }
    cols['city'] = {
        'index': 4,
        'type': "string",
        'friendly': "City",
        'tooltip': "Click here to sort"
    }
    cols['neighborhood'] = {
        'index': 5,
        'type': "string",
        'friendly': "Neighborhood",
        'tooltip': "Click here to sort"
    }
    cols['work_place'] = {
        'index': 6,
        'type': "string",
        'friendly': "Work Place",
        'tooltip': "Click here to sort"
    }
    cols['medical_training'] = {
        'index': 7,
        'type': "string",
        'friendly': "Medical Training",
        'hidden':'true'
    }
    cols['vehicle'] = {
        'index': 8,
        'type': "string",
        'friendly': "Vehicle",
        'hidden':'true'
    }
    cols['other_languages'] = {
        'index': 9,
        'type': "string",
        'friendly': "Other Languages",
        'hidden':'true'
    }
    cols['other_specialties'] = {
        'index': 10,
        'type': "string",
        'friendly': "Other Specialties",
        'hidden':'true'
    }
    cols['start_time_available'] = {
        'index': 11,
        'type': "number",
        'friendly': "Start Time Available",
		'tooltip': "Click here to sort"
    }
    cols['end_time_availalable'] = {
        'index': 12,
        'type': "number",
        'friendly': "End Time Available",
		'tooltip': "Click here to sort"
    }
    cols['days_and_times_available_notes'] = {
        'index': 13,
        'type': "string",
        'friendly': "Times Notes", 
        'hidden':'true'
    }
    
    cols['sunday'] = {
        'index': 14,
        'type': "bool",
        'friendly': "Sunday Avail.",
        'hidden':'true'
    }
    cols['monday'] = {
        'index': 15,
        'type': "bool",
        'friendly': "Monday Avail.",
        'hidden':'true'
    }
    cols['tuesday'] = {
        'index': 16,
        'type': "bool",
        'friendly': "Tuesday Avail.",
        'hidden':'true'
    }
    cols['wednesday'] = {
        'index': 17,
        'type': "bool",
        'friendly': "Wednesday Avail.",
        'hidden':'true'
    }
    cols['thursday'] = {
        'index': 18,
        'type': "bool",
        'friendly': "Thursday Avail.",
        'hidden':'true'
    }
    cols['friday'] = {
        'index': 19,
        'type': "bool",
        'friendly': "Friday Avail.",
        'hidden':'true'
    }
    cols['shabbos'] = {
        'index': 20,
        'type': "bool",
        'friendly': "Shabbos Avail.",
        'hidden':'true'
    }
    cols['wants_alerts'] = {
		'index': 21,
		'type': "bool",
		'friendly': "Wants Alerts",
		'hidden':'true'
	}
    cols['wants_alerts_notes'] = {
		'index': 22,
		'type': "string",
		'friendly': "Wants Alerts Notes", 
		'hidden':'true'
	}
    cols['meal_preparation'] = {
        'index': 23,
        'type': "bool",
        'friendly': "Meal Preparation",
        'hidden':'true'
    }
    cols['meal_preparation_notes'] = {
		'index': 24,
		'type': "string",
		'friendly': "Meal Preparation Notes", 
		'hidden':'true'
	}
    cols['meal_delivery'] = {
        'index': 25,
        'type': "bool",
        'friendly': "Meal Delivery",
        'hidden':'true'
    }
    cols['meal_delivery_notes'] = {
		'index': 26,
		'type': "string",
		'friendly': "Meal Delivery Notes", 
		'hidden':'true'
	}
    cols['hospital_visitation'] = {
		'index': 27,
		'type': "bool",
		'friendly': "Hospital Visit.",
		'hidden':'true'
	}
    cols['hospital_visitation_notes'] = {
		'index': 28,
		'type': "string",
		'friendly': "Hospital Visit. Notes", 
		'hidden':'true'
	}
    cols['transportation_to_appointments'] = {
		'index': 29,
		'type': "bool",
		'friendly': "Transportation",
		'hidden':'true'
	}
    cols['transportation_to_appointments_notes'] = {
		'index': 30,
		'type': "string",
		'friendly': "Transportation Notes", 
		'hidden':'true'
	}
    cols['overnight_hospital_stays'] = {
		'index': 31,
		'type': "bool",
		'friendly': "Overnight Hosp. Stays",
		'hidden':'true'
	}
    cols['overnight_hospital_stays_notes'] = {
		'index': 32,
		'type': "string",
		'friendly': "Overnight Hosp. Stays Notes", 
		'hidden':'true'
	}
    cols['assist_homebound'] = {
		'index': 33,
		'type': "bool",
		'friendly': "Assist Homebound",
		'hidden':'true'
	}
    cols['assist_homebound_notes'] = {
		'index': 34,
		'type': "string",
		'friendly': "Assist Homebound Notes", 
		'hidden':'true'
	}
    cols['assist_with_children'] = {
		'index': 35,
		'type': "bool",
		'friendly': "Assist With Child.",
		'hidden':'true'
	}
    cols['assist_with_children_notes'] = {
		'index': 36,
		'type': "string",
		'friendly': "Assist With Child. Notes", 
		'hidden':'true'
	}
    cols['assist_with_children_activities'] = {
		'index': 37,
		'type': "bool",
		'friendly': "Assist With Child. Act.",
		'hidden':'true'
	}
    cols['assist_with_children_activities_notes'] = {
		'index': 38,
		'type': "string",
		'friendly': "Assist With Child. Act. Notes", 
		'hidden':'true'
	}
    cols['able_to_entertain_children'] = {
		'index': 39,
		'type': "bool",
		'friendly': "Entertain Child.",
		'hidden':'true'
	}
    cols['able_to_entertain_children_notes'] = {
		'index': 40,
		'type': "string",
		'friendly': "Entertain Child. Notes", 
		'hidden':'true'
	}
    cols['visit_elderly'] = {
		'index': 41,
		'type': "bool",
		'friendly': "Visit Elderly",
		'hidden':'true'
	}
    cols['visit_elderly_notes'] = {
		'index': 42,
		'type': "string",
		'friendly': "Visit Elderly Notes", 
		'hidden':'true'
	}
    cols['assist_with_housekeeping'] = {
		'index': 43,
		'type': "bool",
		'friendly': "Assist with Housekeeping",
		'hidden':'true'
	}
    cols['assist_with_housekeeping_notes'] = {
		'index': 44,
		'type': "string",
		'friendly': "Assist with Housekeeping Notes", 
		'hidden':'true'
	}
    cols['phone_calls'] = {
		'index': 45,
		'type': "bool",
		'friendly': "Phone Calls",
		'hidden':'true'
	}
    cols['phone_calls_notes'] = {
		'index': 46,
		'type': "string",
		'friendly': "Phone Calls Notes", 
		'hidden':'true'
	}
    cols['learn_with_elderly'] = {
		'index': 47,
		'type': "bool",
		'friendly': "Learn with Elderly",
		'hidden':'true'
	}
    cols['learn_with_elderly_notes'] = {
		'index': 48,
		'type': "string",
		'friendly': "Learn with Elderly Notes", 
		'hidden':'true'
	}
    cols['home_phone'] = {
		'index': 49,
		'type': "string",
		'friendly': "Home Phone", 
		'hidden':'true'
	}
    cols['cell_phone'] = {
		'index': 50,
		'type': "string",
		'friendly': "Cell Phone", 
		'hidden':'true'
	}
    cols['email_address'] = {
		'index': 51,
		'type': "string",
		'friendly': "Email", 
		'hidden':'true'
	}
    return cols
   
def getRows():
	rows=[]
	
	d = Volunteers.objects.all()
	#o = VolunteerOptions.objects.all()
	
	for volunteer in d:
		columns = collections.OrderedDict()
		columns['id']=volunteer.id
		columns['name']=volunteer.get_name()
		columns['address']=volunteer.address
		if(volunteer.city):
			columns['city']=volunteer.city.city
		if(volunteer.neighborhood):
			columns['neighborhood']=volunteer.neighborhood.neighborhood
		columns['work_place']=volunteer.work_place
		columns['medical_training']=volunteer.medical_training
		if(volunteer.vehicle):
			columns['vehicle']=volunteer.vehicle.vehicle
		columns['other_languages']=volunteer.other_languages
		columns['other_specialties']=volunteer.other_specialties
		if(volunteer.start_time_available):
			columns['start_time_available']=volunteer.start_time_available.hour
		if(volunteer.end_time_availalable):
			columns['end_time_availalable']=volunteer.end_time_availalable.hour
		columns['days_and_times_available_notes']=volunteer.days_and_times_available_notes
		columns['sunday']=volunteer.sunday
		columns['monday']=volunteer.monday
		columns['tuesday']=volunteer.tuesday
		columns['wednesday']=volunteer.wednesday
		columns['thursday']=volunteer.thursday
		columns['friday']=volunteer.friday
		columns['shabbos']=volunteer.shabbos
		columns['wants_alerts'] = volunteer.wants_alerts
		columns['wants_alerts_notes'] = volunteer.wants_alerts_notes
		columns['meal_preparation'] = volunteer.meal_preparation
		columns['meal_preparation_notes'] = volunteer.meal_preparation_notes
		columns['meal_delivery'] = volunteer.meal_delivery
		columns['meal_delivery_notes'] = volunteer.meal_delivery_notes
		columns['hospital_visitation'] = volunteer.hospital_visitation
		columns['hospital_visitation_notes'] = volunteer.hospital_visitation_notes
		columns['transportation_to_appointments'] = volunteer.transportation_to_appointments
		columns['transportation_to_appointments_notes'] = volunteer.transportation_to_appointments_notes
		columns['overnight_hospital_stays'] = volunteer.overnight_hospital_stays
		columns['overnight_hospital_stays_notes'] = volunteer.overnight_hospital_stays_notes
		columns['assist_homebound'] = volunteer.assist_homebound
		columns['assist_homebound_notes'] = volunteer.assist_homebound_notes
		columns['assist_with_children'] = volunteer.assist_with_children
		columns['assist_with_children_notes'] = volunteer.assist_with_children_notes
		columns['assist_with_children_activities'] = volunteer.assist_with_children_activities
		columns['assist_with_children_activities_notes'] = volunteer.assist_with_children_activities_notes
		columns['able_to_entertain_children'] = volunteer.able_to_entertain_children
		columns['able_to_entertain_children_notes'] = volunteer.able_to_entertain_children_notes
		columns['visit_elderly'] = volunteer.visit_elderly
		columns['visit_elderly_notes'] = volunteer.visit_elderly_notes
		columns['assist_with_housekeeping'] = volunteer.assist_with_housekeeping
		columns['assist_with_housekeeping_notes'] = volunteer.assist_with_housekeeping_notes
		columns['phone_calls'] = volunteer.phone_calls
		columns['phone_calls_notes'] = volunteer.phone_calls_notes
		columns['learn_with_elderly'] = volunteer.learn_with_elderly
		columns['learn_with_elderly_notes'] = volunteer.learn_with_elderly_notes
		columns['home_phone'] = volunteer.home_phone
		columns['cell_phone'] = volunteer.cell_phone
		columns['email_address'] = volunteer.email_address
		#voptions = o.filter(volunteers=volunteer.id)
		
		#meal_prep = voptions.filter(option__option='Meal Preparation')
		#if(len(meal_prep)>0):
		#	columns['meal_preparation']=meal_prep[0].has_option
		rows.append(columns)
	return rows