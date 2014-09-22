from django.db import models

class Neighborhoods(models.Model):
	neighborhood = models.CharField(max_length=50)
	def __str__(self):
		return self.neighborhood
		
class Vehicles(models.Model):
	vehicle = models.CharField(max_length=50)
	def __str__(self):
		return self.vehicle
		
class Volunteers(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	street_number = models.IntegerField()
	street = models.CharField(max_length=50, null=True)
	neighborhood = models.ForeignKey(Neighborhoods, null=True)
	work_place = models.CharField(max_length=100)
	medical_training = models.CharField(max_length=100)
	home_phone = models.CharField(max_length=50)
	cell_phone = models.CharField(max_length=50)
	email_address = models.CharField(max_length=50, null=True)
	days_times_available = models.CharField(max_length=200, null=True)
	vehicle = models.ForeignKey(Vehicles, blank=True, null=True)
	other_languages = models.CharField(max_length=200, null=True)
	other_specialties = models.CharField(max_length=200, null = True)
	def __str__(self):
		return self.first_name + ' ' + self.last_name
	
class VolunteerOptions(models.Model):
	volunteer = models.ForeignKey(Volunteers)
	option = models.CharField(max_length=50)
	choice = models.NullBooleanField()
	notes = models.CharField(max_length=200)
	def __str__(self):
		return self.option
	
class ClientStatus(models.Model):
	status = models.CharField(max_length=50)
	def __str__(self):
		return self.status
		
class Cities(models.Model):
	city = models.CharField(max_length=50)
	def __str__(self):
		return self.city
		
class Hospitals(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	def __str__(self):
		return self.name
	
class TikvahHouses(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	def __str__(self):
		return self.name
		
class Clients(models.Model):
	client_status = models.ForeignKey(ClientStatus, null = True)
	start_date = models.DateTimeField('start date')
	expected_end_date = models.DateTimeField('expected end date')
	end_date = models.DateTimeField('end date')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	street_number = models.IntegerField()
	street = models.CharField(max_length=50)
	city = models.ForeignKey(Cities, null = True)
	home_phone = models.CharField(max_length=50)
	cell_phone = models.CharField(max_length=50)
	text_ability = models.NullBooleanField()
	email_address = models.CharField(max_length=50, null=True)
	current_location = models.ForeignKey(Neighborhoods, null=True)
	hospital = models.ForeignKey(Hospitals, null=True)
	hospital_room = models.CharField(max_length=50)
	hospital_notes = models.CharField(max_length=200)
	tikvah_house = models.ForeignKey(TikvahHouses, null=True)
	tikvah_room = models.CharField(max_length=50)
	food_to_hospital = models.NullBooleanField()
	food_notes = models.CharField(max_length=300)
	food_to_home = models.NullBooleanField()
	allergies = models.CharField(max_length=200)
	yoshon = models.NullBooleanField()
	cholov_yisroel = models.NullBooleanField()
	transportation = models.CharField(max_length=200)
	visitor_comments = models.CharField(max_length=500)
	medical_equipment = models.CharField(max_length=200)
	def __str__(self):
		return self.first_name + ' ' + self.last_name
		
class CaseStatus(models.Model):
	status = models.CharField(max_length=50)
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
	def __str__(self):
		return self.client.name
		
#class Choice(models.Model):
#    question = models.ForeignKey(Question)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)	