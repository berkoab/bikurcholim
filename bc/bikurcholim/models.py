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

class VolunteerOptionValues(models.Model):
	option = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Volunteer Option Values"
	def __str__(self):
		return self.option
		
class Volunteers(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=100, null=True)
	city = models.ForeignKey(Cities, null = True)
	neighborhood = models.ForeignKey(Neighborhoods, null=True)
	work_place = models.TextField(max_length=100)
	medical_training = models.TextField(max_length=100)
	home_phone = models.CharField(max_length=50)
	cell_phone = models.CharField(max_length=50)
	email_address = models.EmailField(null=True)
	start_time_available = models.TimeField(default=None)
	end_time_availalable = models.TimeField(default=None)
	vehicle = models.ForeignKey(Vehicles, blank=True, null=True)
	other_languages = models.TextField(max_length=200, null=True)
	other_specialties = models.TextField(max_length=200, null = True)
	class Meta:
		verbose_name_plural = "Volunteers"
	def __str__(self):
		return self.first_name + ' ' + self.last_name

class VolunteerDaysAvailable(models.Model):
	volunteers = models.ForeignKey(Volunteers)
	sunday = models.BooleanField(default=None)
	monday = models.BooleanField(default=None)
	tuesday = models.BooleanField(default=None)
	wednesday = models.BooleanField(default=None)
	thursday = models.BooleanField(default=None)
	friday = models.BooleanField(default=None)
	shabbos = models.BooleanField(default=None)
	class Meta:
		verbose_name_plural = "Days Available"
		
class VolunteerOptions(models.Model):
	volunteers = models.ForeignKey(Volunteers)
	option = models.ForeignKey(VolunteerOptionValues)
	has_option = models.BooleanField(default=None)
	notes = models.CharField(max_length=200)
	class Meta:
		verbose_name_plural = "Volunteer Options"
	def __str__(self):
		return  self.option.option + '-' + self.volunteers.first_name + ' ' + self.volunteers.last_name
	
class ClientStatus(models.Model):
	status = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Client Statuses"
	def __str__(self):
		return self.status
		
class Hospitals(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	class Meta:
		verbose_name_plural = "Hospitals"
	def __str__(self):
		return self.name
	
class TikvahHouses(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	class Meta:
		verbose_name_plural = "Tikvah Houses"
	def __str__(self):
		return self.name
		
class Clients(models.Model):
	client_status = models.ForeignKey(ClientStatus, null = True)
	start_date = models.DateField('start date')
	expected_end_date = models.DateField('expected end date')
	end_date = models.DateField('end date')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	street_number = models.IntegerField()
	street = models.CharField(max_length=50)
	city = models.ForeignKey(Cities, null = True)
	home_phone = models.CharField(max_length=50)
	cell_phone = models.CharField(max_length=50)
	text_ability = models.NullBooleanField()
	email_address = models.EmailField(max_length=50, null=True)
	current_location = models.ForeignKey(Neighborhoods, null=True)
	hospital = models.ForeignKey(Hospitals, null=True)
	hospital_room = models.CharField(max_length=50)
	hospital_notes = models.TextField(max_length=200)
	tikvah_house = models.ForeignKey(TikvahHouses, null=True)
	tikvah_room = models.CharField(max_length=50)
	food_to_hospital = models.NullBooleanField()
	food_notes = models.TextField(max_length=300)
	food_to_home = models.NullBooleanField()
	allergies = models.TextField(max_length=200)
	yoshon = models.NullBooleanField()
	cholov_yisroel = models.NullBooleanField()
	transportation = models.TextField(max_length=200)
	visitor_comments = models.TextField(max_length=500)
	medical_equipment = models.TextField(max_length=200)
	class Meta:
		verbose_name_plural = "Clients"
	def __str__(self):
		return self.first_name + ' ' + self.last_name
		
class CaseStatus(models.Model):
	status = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Case Statuses"
	def __str__(self):
		return self.status
		
class Cases(models.Model):
	client = models.ForeignKey(Clients)
	status = models.ForeignKey(CaseStatus)
	open_date = models.DateTimeField('open date')
	date_of_service = models.DateTimeField('service date')
	close_date = models.DateTimeField('close date')
	description = models.CharField(max_length=200)
	volunteer = models.ForeignKey(Volunteers, null=True)
	class Meta:
		verbose_name_plural = "Cases"
	def __str__(self):
		return self.client.name
		