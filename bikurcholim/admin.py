from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
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
from bikurcholim.models import Tasks
from bikurcholim.models import TaskStatus
from bikurcholim.models import ClientService
		
class VolunteersAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name')
	list_filter = ['neighborhood', 'vehicle', 'hospital_visitation', 
					'transportation_to_appointments', 'overnight_hospital_stays', 'assist_homebound', 'assist_with_children', 
					'assist_with_children_activities', 'able_to_entertain_children', 'visit_elderly', 
					'assist_with_housekeeping', 'phone_calls', 'learn_with_elderly', 'visit_homebound']
	search_fields = ['last_name', 'first_name', 'street', 'work_place', 'email_address']
	fieldsets = [
		(None, {'fields': ['first_name', 'last_name', 'home_phone', 
		'cell_phone', 'email_address', 'address', 'city', 'neighborhood', 'work_place', 'start_date', 'end_date', 'medical_training', 'vehicle', 'other_languages', 'other_specialties']}),
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
										('phone_calls', 'phone_calls_notes'), ('learn_with_elderly', 'learn_with_elderly_notes'), ('visit_homebound', 'visit_homebound_notes')]})]
	
class ClientServiceInline(admin.TabularInline):
    model = ClientService
    extra = 2

class HousingScheduleInline(admin.TabularInline):
    model = HousingSchedule
    extra = 2
    
class ClientsAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name')
	list_filter = ['status__status', 'neighborhood', 'hospital']
	search_fields = ['last_name', 'first_name', 'street']
	inlines = [ClientServiceInline, HousingScheduleInline]

class ClientServiceAdmin(admin.ModelAdmin):
	list_display = ('client', 'volunteer', 'status')
	list_filter = ['status__status']
	search_fields = ['description', 'client', 'volunteer']
	
class CasesAdminForm(forms.ModelForm):
    def clean_close_date(self):
    	open_date = self.cleaned_data["open_date"]
    	close_date = self.cleaned_data["close_date"]
    	if(close_date):
        	if((not open_date) or (close_date < open_date)):
        		raise forms.ValidationError('"Close Date" needs to be greater than "Open Date')
        return close_date
       
class CasesAdmin(admin.ModelAdmin):
	list_display = ('id', 'last_name', 'first_name', 'volunteer')
	list_filter = ['status__status', 'location__name']
	search_fields = ['first_name', 'last_name', 'volunteer__first_name', 'volunteer__last_name', 'description']
	form = CasesAdminForm
	
class HousingAdminForm(forms.ModelForm):
    def clean_to_date(self):
    	from_date = self.cleaned_data["from_date"]
    	to_date = self.cleaned_data["to_date"]
    	if(to_date):
        	if((not from_date) or (to_date < from_date)):
        		raise forms.ValidationError('"To Date" needs to be greater than "From Date')
        return to_date
       
class HousingScheduleAdmin(admin.ModelAdmin):
	list_display = ('from_date', 'to_date', 'housing')
	list_filter = ['housing']
	form = HousingAdminForm
    
class TasksAdmin(admin.ModelAdmin):
	list_display = ('title', 'status')
	list_filter = ['status__status']
	search_fields = ['title', 'description']
	form = CasesAdminForm

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
admin.site.register(HousingSchedule, HousingScheduleAdmin)
admin.site.register(TaskStatus)
admin.site.register(Tasks, TasksAdmin)
admin.site.register(ClientService, ClientServiceAdmin)

admin.AdminSite.site_header="Bikur Cholim Database Administration"
admin.AdminSite.site_title="Bikur Cholim Database Administration"