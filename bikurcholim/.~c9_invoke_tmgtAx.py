from django.contrib import admin
from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from bikurcholim.models import Neighborhoods
from bikurcholim.models import Vehicles
from bikurcholim.models import Volunteers
from bikurcholim.models import Cities
from bikurcholim.models import Hospitals
from bikurcholim.models import Houses
from bikurcholim.models import Cases
from bikurcholim.models import ClientStatus
from bikurcholim.models import CaseStatus
from bikurcholim.models import IntakeCalls
from bikurcholim.models import Services
from bikurcholim.models import HousingSchedule
from bikurcholim.models import Phones
from bikurcholim.models import PhoneTypes
from bikurcholim.models import Tasks
from bikurcholim.models import TaskStatus
from bikurcholim.models import ClientService
from bikurcholim.models import OtherOptions, Options
from bikurcholim.models import VolunteerClients
from bikurcholim.models import CaseManagers
from django.forms import TextInput, Textarea

class VolunteerOptionsInline(admin.TabularInline):
    model = OtherOptions
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }
class VolunteerClientsInline(admin.TabularInline):
    model = VolunteerClients
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }   		
class VolunteersAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'cell_phone')
	list_filter = ['neighborhood', 'vehicle', 'meal_delivery', 'hospital_visitation', 
					'transportation_to_appointments', 'overnight_hospital_stays', 'assist_homebound', 'assist_with_children', 
					'assist_with_children_activities', 'able_to_entertain_children', 'visit_elderly', 
					'assist_with_housekeeping', 'phone_calls', 'learn_with_elderly', 'visit_homebound']
	search_fields = ['last_name', 'first_name', 'address', 'work_place', 'email_address', 'cell_phone', 'home_phone']
	fieldsets = [
		(None, 
			{'fields': ['first_name', 'last_name', 'home_phone', 
		'cell_phone', 'email_address', 'address', 'city', 'neighborhood', 'work_place', 'medical_training', 'vehicle', 'other_languages', 'other_specialties']}),
		('Times Available', {'fields': ['start_time_available', 'end_time_availalable', 'start_time_available2', 'end_time_availalable2']}),
		('Days Available', {'fields': [('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'shabbos')]}),
		(None, {'fields': ['days_and_times_available_notes']}), 
		('Dates', {'fields': ['start_date', 'end_date', 'last_update_date']}),
		('Volunteer Options', {'classes': ('wide', 'extrapretty'),
		'fields': [('wants_alerts', 'wants_alerts_notes'), ('meal_preparation', 'meal_preparation_notes'),
										('meal_delivery', 'meal_delivery_notes'), ('hospital_visitation', 'hospital_visitation_notes'),
										('transportation_to_appointments', 'transportation_to_appointments_notes'), ('overnight_hospital_stays', 'overnight_hospital_stays_notes'),
										('assist_homebound', 'assist_homebound_notes'), ('assist_with_children', 'assist_with_children_notes'), 
										('assist_with_children_activities', 'assist_with_children_activities_notes'), ('able_to_entertain_children', 'able_to_entertain_children_notes'), 
										('visit_elderly', 'visit_elderly_notes'), ('assist_with_housekeeping', 'assist_with_housekeeping_notes'),
										('phone_calls', 'phone_calls_notes'), ('learn_with_elderly', 'learn_with_elderly_notes'), ('visit_homebound', 'visit_homebound_notes')]})]
	inlines = [VolunteerOptionsInline, VolunteerClientsInline]
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }
class ClientServiceInline(admin.TabularInline):
    model = ClientService
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }
class PhonesInline(admin.TabularInline):
    model = Phones
    extra = 1
    
class HousingScheduleInline(admin.TabularInline):
    model = HousingSchedule
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }
class CasesAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'status', 'cell_phone', 'hospital', 'hospital_room', 'created_at')
	list_filter = ['status__status', 'neighborhood', 'hospital']
	search_fields = ['last_name', 'first_name', 'address']
	fieldsets = [
		(None, {'fields': ['first_name', 'last_name', 'hospital', 'hospital_room', 'other_location', 'medical_condition', 
						'address', 'city', 'home_phone', 'cell_phone', 'email_address', 'neighborhood', 
						'status', 'case_manager', 'hospital_notes', 'food_notes', 'transportation', 'visitor_comments', 
						'medical_equipment', 'donation_made']}),
		('Dates', {'fields': ['original_start_date', 'active_start_date', 'expected_end_date', 'end_date', 'inactive_date']}),
		('Options', {'classes': ('wide', 'extrapretty'),
		'fields': [('text_ability', 'text_ability_notes'), ('food_to_hospital', 'food_to_hospital_notes'), 
				('food_to_home', 'food_to_home_notes'), ('housing_checkbox', 'housing_notes'), 
				('transportation_checkbox', 'transportation_notes'), ('respite_in_home', 'respite_in_home_notes'), 
				('cleaning_in_home', 'cleaning_in_home_notes'), ('other', 'other_notes'), 'general_notes']}),
		('Meals', {'fields': ['meal_coordinator', 'meal_preparer']})
	]
	inlines = [PhonesInline, ClientServiceInline, HousingScheduleInline]
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }
class ClientServiceAdmin(admin.ModelAdmin):
	list_display = ('client', 'volunteer', 'status')
	list_filter = ['status__status']
	search_fields = ['description', 'client', 'volunteer']
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }
class ClientServiceAdminForm(forms.ModelForm):
	def clean_end_date(self):
		end_date = self.cleaned_data['end_date']
		if not end_date:
			raise forms.ValidationError("Please enter an end date.")
		return end_date
class PhonesAdmin(admin.ModelAdmin):
	list_display = ('type', 'client', 'number')
	list_filter = ['type']
	search_fields = ['note']
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }
class IntakeCallsAdminForm(forms.ModelForm):
    def clean_close_date(self):
    	date_call_received = self.cleaned_data["date_call_received"]
    	close_date = self.cleaned_data["close_date"]
    	if(close_date):
        	if((not date_call_received) or (close_date < date_call_received)):
        		raise forms.ValidationError('"Close Date" needs to be greater than "Open Date')
        return close_date
       
class IntakeCallsAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'hospital', 'date_call_received', 'initiating_phone_number', 'initiating_name', 'created_at')
	list_filter = ['hospital__name']
	search_fields = ['first_name', 'last_name', 'description']
	form = IntakeCallsAdminForm
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }
class HousingAdminForm(forms.ModelForm):
    def clean_to_date(self):
    	from_date = self.cleaned_data["from_date"]
    	to_date = self.cleaned_data["to_date"]
    	if(to_date):
        	if((not from_date) or (to_date < from_date)):
        		raise forms.ValidationError('"To Date" needs to be greater than "From Date')
        return to_date
       
class HousingScheduleAdmin(admin.ModelAdmin):
	list_display = ('case', 'from_date', 'to_date', 'house')
	list_filter = ['house']
	form = HousingAdminForm
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }
class TasksAdmin(admin.ModelAdmin):
	list_display = ('title', 'status')
	list_filter = ['status__status']
	search_fields = ['title', 'description']
	#form = IntakeCallsAdminForm
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':20})},
    }
admin.site.register(Neighborhoods)
admin.site.register(Vehicles)
admin.site.register(Volunteers, VolunteersAdmin)
admin.site.register(Cities)
admin.site.register(Hospitals)
admin.site.register(Houses)
admin.site.register(Cases, CasesAdmin)
admin.site.register(ClientStatus)
admin.site.register(CaseStatus)
admin.site.register(IntakeCalls, IntakeCallsAdmin)
admin.site.register(Services)
admin.site.register(Options)
admin.site.register(HousingSchedule, HousingScheduleAdmin)
admin.site.register(TaskStatus)
admin.site.register(Tasks, TasksAdmin)
admin.site.register(ClientService, ClientServiceAdmin)
admin.site.register(OtherOptions)
admin.site.register(VolunteerClients)
admin.site.register(PhoneTypes)
admin.site.register(Phones, PhonesAdmin)
admin.site.register(CaseManagers)
admin.AdminSite.site_header="Bikur Cholim Database Administration"
admin.AdminSite.site_title="Bikur Cholim Database Administration"