from django.contrib import admin
from bikurcholim.models import Neighborhoods
from bikurcholim.models import Vehicles
from bikurcholim.models import Volunteers
from bikurcholim.models import Cities
from bikurcholim.models import Hospitals
from bikurcholim.models import TikvahHouses
from bikurcholim.models import Clients
from bikurcholim.models import ClientStatus
from bikurcholim.models import CaseStatus
from bikurcholim.models import Cases
from bikurcholim.models import Services
from bikurcholim.models import HousingSchedule
		
class VolunteersAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name')
	list_filter = ['neighborhood', 'vehicle', 'start_time_available', 'end_time_availalable']
	search_fields = ['last_name', 'first_name', 'street', 'work_place', 'email_address', ]
	fieldsets = [
		(None, {'fields': ['first_name', 'last_name', 'address', 'city', 'neighborhood', 'work_place', 'medical_training', 'home_phone', 
		'cell_phone', 'email_address', 'vehicle', 'other_languages', 'other_specialties']}),
		('Times Available', {'fields': ['start_time_available', 'end_time_availalable']}),
		('Days Available', {'fields': [('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'shabbos')]}),
		(None, {'fields': ['days_and_times_available_notes']}), 
		('Volunteer Options', {'classes': ('wide', 'extrapretty'),
		'fields': [('wants_alerts', 'wants_alerts_notes'), ('meal_preparation', 'meal_preparation_notes'),
										('meal_delivery', 'meal_delivery_notes'), ('hospital_visitation', 'hospital_visitation_notes'),
										('transportation_to_appointments', 'transportation_to_appointments_notes'), ('overnight_hospital_stays', 'overnight_hospital_stays_notes'),
										('assist_homebound', 'assist_homebound_notes'), ('assist_with_children', 'assist_with_children_notes'), 
										('assist_with_children_activities', 'assist_with_children_activities_notes'), ('able_to_entertain_children', 'able_to_entertain_children_notes'), 
										('visit_elderly', 'visit_elderly_notes'), ('assist_with_housekeeping', 'assist_with_housekeeping_notes'),
										('phone_calls', 'phone_calls_notes'), ('learn_with_elderly', 'learn_with_elderly_notes')]})
	]

class ClientsAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name')
	list_filter = ['status__status', 'neighborhood', 'hospital', 'tikvah_house']
	search_fields = ['last_name', 'first_name', 'street']
class CasesAdmin(admin.ModelAdmin):
	list_display = ('id', 'client', 'volunteer')
	list_filter = ['status__status', 'location__name']
	search_fields = ['client__first_name', 'client__last_name', 'volunteer__first_name', 'volunteer__last_name', 'description']
	
admin.site.register(Neighborhoods)
admin.site.register(Vehicles)
admin.site.register(Volunteers, VolunteersAdmin)
admin.site.register(Cities)
admin.site.register(Hospitals)
admin.site.register(TikvahHouses)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(ClientStatus)
admin.site.register(CaseStatus)
admin.site.register(Cases, CasesAdmin)
admin.site.register(Services)
admin.site.register(HousingSchedule)

admin.AdminSite.site_header="Bikur Cholim Database Administration"