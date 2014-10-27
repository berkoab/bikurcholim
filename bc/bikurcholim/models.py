from django.db import models

class Neighborhoods(models.Model):
	neighborhood = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Neighborhoods"
	def __str__(self):
		return self.neighborhood
		
class Cities(models.Model):
	city = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Cities"
	def __str__(self):
		return self.city
		
class Vehicles(models.Model):
	vehicle = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Vehicles"
	def __str__(self):
		return self.vehicle
	
class Volunteers(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=100, null=True, blank=True)
	city = models.ForeignKey(Cities, null = True, blank=True)
	neighborhood = models.ForeignKey(Neighborhoods, null=True, blank=True)
	work_place = models.TextField(max_length=100, null=True, blank=True)
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
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    
	class Meta:
		verbose_name_plural = "Volunteers"
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

class ClientStatus(models.Model):
	status = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Client Statuses"
	def __str__(self):
		return self.status

class CaseStatus(models.Model):
	status = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Case Statuses"
	def __str__(self):
		return self.status
		
class Hospitals(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200, null=True, blank=True)
	class Meta:
		verbose_name_plural = "Hospitals"
	def __str__(self):
		return self.name
	
class TikvahHouses(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=200, null=True, blank=True)
	class Meta:
		verbose_name_plural = "Tikvah Houses"
	def __str__(self):
		return self.name
		
class Clients(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
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
	hospital = models.ForeignKey(Hospitals, null=True, blank=True)
	hospital_room = models.CharField(max_length=50, null=True, blank=True)
	hospital_notes = models.TextField(max_length=200, null=True, blank=True)
	tikvah_house = models.ForeignKey(TikvahHouses, null=True, blank=True)
	tikvah_room = models.CharField(max_length=50, null=True, blank=True)
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
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    
	class Meta:
		verbose_name_plural = "Clients"
	def get_name(self):
		return self.last_name + ', ' + self.first_name
	def __str__(self):
		return self.last_name + ', ' + self.first_name

class Services(models.Model):
	service = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Services"
	def __str__(self):
		return self.service

class Cases(models.Model):
	client = models.ForeignKey(Clients)
	status = models.ForeignKey(CaseStatus)
	volunteer = models.ForeignKey(Volunteers, null=True, blank=True)
	open_date = models.DateField('open date', null=True, blank=True)
	date_of_service = models.DateTimeField('date and time of service', null=True, blank=True)
	close_date = models.DateField('close date', null=True, blank=True)
	service = models.ForeignKey(Services, null=True, blank=True)
	description = models.TextField(max_length=200, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name_plural = "Cases"
	def __str__(self):
		return str(self.id)
		