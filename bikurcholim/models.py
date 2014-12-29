from django.db import models
from paintstore.fields import ColorPickerField
from django.forms import ModelForm, Textarea
from datetime import date
from time import mktime
from datetime import timedelta
from datetime import datetime
import time

class Neighborhoods(models.Model):
	neighborhood = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Neighborhoods"
		ordering = ('neighborhood',)
	def __str__(self):
		return self.neighborhood
		
class Cities(models.Model):
	city = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Cities"
		ordering = ('city',)
	def __str__(self):
		return self.city
		
class Vehicles(models.Model):
	vehicle = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Vehicles"
		ordering = ('vehicle',)
	def __str__(self):
		return self.vehicle

class Options(models.Model):
	name = models.CharField(max_length=100)
	class Meta:
		verbose_name_plural = "Options"
		ordering = ('name', )
	def __str__(self):
		return str(self.name)

class VolunteerClients(models.Model):
	case = models.ForeignKey('Cases')
	volunteer = models.ForeignKey('Volunteers')
	note = models.TextField(max_length=200, null=True, blank=True)
	class Meta:
		verbose_name = "volunteer cases"
		verbose_name_plural = "Volunteer Cases"
		ordering = ('case__last_name', 'case__first_name')
	def __str__(self):
		return str(self.case.last_name + ', ' + self.case.first_name)
					
class Volunteers(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=100, null=True, blank=True)
	city = models.ForeignKey(Cities, null = True, blank=True)
	neighborhood = models.ForeignKey(Neighborhoods, null=True, blank=True)
	work_place = models.TextField(max_length=100, null=True, blank=True)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	medical_training = models.TextField(max_length=100, null=True, blank=True)
	home_phone = models.CharField(max_length=50, null=True, blank=True)
	cell_phone = models.CharField(max_length=50, null=True, blank=True)
	email_address = models.EmailField(null=True, blank=True)
	vehicle = models.ForeignKey(Vehicles, null=True, blank=True)
	other_languages = models.TextField(max_length=200, null=True, blank=True)
	other_specialties = models.TextField(max_length=200, null = True, blank=True)
	days_and_times_available_notes = models.TextField("Notes on Availability", max_length=200, null = True, blank=True)
	start_time_available = models.TimeField("Available From", null=True, blank=True)
	end_time_availalable = models.TimeField("Available To", null=True, blank=True)
	sunday = models.BooleanField(default=None)
	monday = models.BooleanField(default=None)
	tuesday = models.BooleanField(default=None)
	wednesday = models.BooleanField(default=None)
	thursday = models.BooleanField(default=None)
	friday = models.BooleanField(default=None)
	shabbos = models.BooleanField(default=None)
	wants_alerts = models.BooleanField(default=None)
	wants_alerts_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	meal_preparation = models.BooleanField(default=None)
	meal_preparation_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	meal_delivery = models.BooleanField(default=None)
	meal_delivery_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	hospital_visitation = models.BooleanField(default=None)
	hospital_visitation_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	transportation_to_appointments = models.BooleanField(default=None)
	transportation_to_appointments_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	overnight_hospital_stays = models.BooleanField(default=None)
	overnight_hospital_stays_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	assist_homebound = models.BooleanField(default=None)
	assist_homebound_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	assist_with_children = models.BooleanField(default=None)
	assist_with_children_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	assist_with_children_activities = models.BooleanField(default=None)
	assist_with_children_activities_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	able_to_entertain_children = models.BooleanField(default=None)
	able_to_entertain_children_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	visit_elderly = models.BooleanField(default=None)
	visit_elderly_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	assist_with_housekeeping = models.BooleanField(default=None)
	assist_with_housekeeping_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	phone_calls = models.BooleanField(default=None)
	phone_calls_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	learn_with_elderly = models.BooleanField(default=None)
	learn_with_elderly_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	visit_homebound = models.BooleanField(default=None)
	visit_homebound_notes = models.CharField("Notes", max_length=100, null=True, blank=True)
	other_options = models.ManyToManyField(Options, through='OtherOptions')
	note = models.ManyToManyField(VolunteerClients)
	last_update_date = models.DateField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    
	class Meta:
		verbose_name_plural = "Volunteers"
		ordering = ('last_name','first_name')
	def get_name(self):
		return self.last_name + ', ' + self.first_name
	def get_fields(self):
		name_value = []
		for field in self.__class__._meta.fields:
			name = field.verbose_name
			value = field._get_val_from_obj(self)
			if(name=='city'):
				name_value.append(('City', self.city.city))
			elif(name=='neighborhood'):
				name_value.append(('Neighborhood', self.neighborhood.neighborhood))
			elif(name=='vehicle'):
				name_value.append(('Vehicle', self.vehicle.vehicle))
			else:
				name_value.append((name.title(), value))
		return name_value
	def __str__(self):
		return self.last_name + ', ' + self.first_name

class OtherOptions(models.Model):
	option = models.ForeignKey(Options)
	volunteer = models.ForeignKey(Volunteers)
	notes = models.TextField(max_length=200, null=True, blank=True)

	class Meta:
		verbose_name_plural = "Other Options"
		ordering = ('option', 'volunteer')
	def __str__(self):
		return self.option.name
	
class ClientStatus(models.Model):
	status = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Case Statuses"
		ordering = ('status',)
	def __str__(self):
		return self.status

class CaseStatus(models.Model):
	status = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Intake Call Statuses"
		ordering = ('status',)
	def __str__(self):
		return self.status
		
class Hospitals(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200, null=True, blank=True)
	class Meta:
		verbose_name_plural = "Hospitals"
		ordering = ('name',)
	def __str__(self):
		return self.name
	
class Houses(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=200, null=True, blank=True)
	phone_number = models.CharField(max_length=50, null=True, blank=True)
	color = ColorPickerField(null=True, blank=True)
	class Meta:
		verbose_name_plural = "Houses"
		ordering = ('name',)
	def __str__(self):
		return self.name

class Services(models.Model):
	service = models.CharField(max_length=50)
	color = ColorPickerField(null=True, blank=True)
	class Meta:
		verbose_name_plural = "Services"
		ordering = ('service',)
	def __str__(self):
		return self.service

class TaskStatus(models.Model):
	status = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Task Statuses"
		ordering = ('status',)
	def __str__(self):
		return self.status

class HousingSchedule(models.Model):
	house = models.ForeignKey(Houses)
	case = models.ForeignKey('Cases')
	apt = models.CharField(max_length=50, null=True, blank=True)
	from_date = models.DateField('from date')
	to_date = models.DateField('to date')
	notes = models.TextField(max_length=200, null=True, blank=True)
	def get_color(self):
		return self.house.color
	def get_days(self):
		return self.to_date - self.from_date
	class Meta:
		verbose_name_plural = "Housing Schedule"
	def __str__(self):
		return str(self.house.name)

class Cases(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	hospital = models.ForeignKey(Hospitals, null=True, blank=True)
	hospital_room = models.CharField(max_length=50, null=True, blank=True)
	medical_condition = models.TextField(max_length=200, null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	city = models.ForeignKey(Cities, null=True, blank=True)
	home_phone = models.CharField(max_length=50, null=True, blank=True)
	cell_phone = models.CharField(max_length=50, null=True, blank=True)
	email_address = models.EmailField(max_length=100, null=True, blank=True)
	neighborhood = models.ForeignKey(Neighborhoods, null=True, blank=True)
	status = models.ForeignKey(ClientStatus, null=True, blank=True)
	start_date = models.DateField(null=True, blank=True)
	expected_end_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)	
	hospital_notes = models.TextField(max_length=200, null=True, blank=True)
#	tikvah_house = models.ForeignKey(TikvahHouses, null=True, blank=True)
#	tikvah_room = models.CharField(max_length=50, null=True, blank=True)
	food_notes = models.TextField(max_length=300, null=True, blank=True)
	allergies = models.TextField(max_length=200, null=True, blank=True)
	transportation = models.TextField(max_length=200, null=True, blank=True)
	visitor_comments = models.TextField(max_length=500, null=True, blank=True)
	medical_equipment = models.TextField(max_length=200, null=True, blank=True)
	donation_made = models.CharField(max_length=50, null=True, blank=True)
	text_ability = models.BooleanField(default=None)
	yoshon = models.BooleanField(default=None)
	cholov_yisroel = models.BooleanField(default=None)
	food_to_hospital = models.BooleanField(default=None)
	food_to_home = models.BooleanField(default=None)
	meal_coordinator = models.ForeignKey(Volunteers, null=True, blank=True, related_name='meal_coordinator_set')
	meal_preparer = models.ForeignKey(Volunteers, null=True, blank=True, related_name='meal_preparer_set')
	services = models.ManyToManyField(Services, through='ClientService')
	#note = models.ManyToManyField(Notes)
 	housing = models.ManyToManyField(Houses, through='HousingSchedule')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    
	class Meta:
		verbose_name_plural = "Cases"
		ordering = ('status', 'last_name','first_name')
	def get_name(self):
		return self.last_name + ', ' + self.first_name
	def __str__(self):
		return self.last_name + ', ' + self.first_name
		
class ClientService(models.Model):
	service = models.ForeignKey(Services)
	client = models.ForeignKey(Cases)
	volunteer = models.ForeignKey(Volunteers, null=True, blank=True)
	description = models.TextField(max_length=200, null=True, blank=True)
	begin_date = models.DateField('open date', null=True, blank=True)
	end_date = models.DateField('close date', null=True, blank=True)
	status = models.ForeignKey(TaskStatus, null=True, blank=True)
	number_of_times = models.IntegerField(null=True, blank=True)
	def get_color(self):
		return self.service.color
	def get_week(self):
		d = self.begin_date
		current_week = int(date(d.year, d.month, d.day).strftime("%W"))
		first_day = datetime.fromtimestamp(mktime(time.strptime('%s %s %s' % (d.year, current_week, str(0)), '%Y %W %w')))
		last_day = first_day + timedelta(days=6)
		return '{0}-{1}'.format(first_day.strftime('%Y/%m/%d'), last_day.strftime('%Y/%m/%d'))
	class Meta:
		verbose_name_plural = "Client Services"
		ordering = ('client', 'begin_date', 'status')
class ClientServiceForm(ModelForm):
	class Meta:
		model = ClientService
		fields = '__all__'
		widgets = {
            'description': Textarea(attrs={'cols': 20, 'rows': 2}),
        }
		#exclude = ['description']

class IntakeCalls(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_call_received = models.DateField('date call received')
	initiating_phone_number = models.CharField(max_length=50, null=True, blank=True)
	initiating_name = models.CharField(max_length=50, null=True, blank=True)
	service = models.ForeignKey(Services, null=True, blank=True)
	location = models.ForeignKey(Hospitals, null=True, blank=True)
	description = models.TextField(max_length=200, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name_plural = "Intake Calls"
		ordering = ('id',)
	def __str__(self):
		return str(self.id)


	
class Tasks(models.Model):
	title = models.CharField(max_length=100)
	status = models.ForeignKey(TaskStatus)
	description = models.TextField(max_length=200, null=True, blank =True)
	due_by = models.DateField('due by', null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name_plural = "Tasks"
		ordering = ('status', 'created_at',)
	def __str__(self):
		return str(self.title)