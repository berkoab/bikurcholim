from django.db import models

class Neighborhoods(models.Model):
	neighborhood = models.CharField(max_length=50)

class Vehicles(models.Model):
	vehicle = models.CharField(max_length=50)
	
class Volunteers(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	street_number = models.IntegerField(default=0)
	neighborhood = models.ForeignKey(Neighborhoods, blank=True, null=True)
	work_place = models.CharField(max_length=100)
	medical_training = models.CharField(max_length=100)
	home_phone = models.CharField(max_length=50)
	cell_phone = models.CharField(max_length=50)
	days_times_available = models.CharField(max_length=200, null=True)
	vehicle = models.ForeignKey(Vehicles, blank=True, null=True)
	other_languages = models.CharField(max_length=200, null=True)
	other_specialties = models.CharField(max_length=200, null = True)
	
class VolunteerOptions(models.Model):
	volunteer = models.ForeignKey(Volunteers)
	option = models.CharField(max_length=50)
	choice = models.NullBooleanField()
	notes = models.CharField(max_length=200)
	

	

#class Choice(models.Model):
#    question = models.ForeignKey(Question)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)