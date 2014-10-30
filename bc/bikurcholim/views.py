from bikurcholim.models import Clients, Volunteers, Cases, HousingSchedule
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views import generic
from django.core.urlresolvers import reverse
import volunteer_view, client_view, case_view, housing_view, service_events_view, housing_events_view
import collections
import datetime
import json
import re
import xlwt
ezxf = xlwt.easyxf

@login_required(login_url='/bikurcholim/login/')
def index(request):
	context = {}

	return render(request, 'bikurcholim/index.html', context)

@login_required(login_url='/bikurcholim/login/')
def volunteers(request):

	cols = volunteer_view.getCols()
	rows = volunteer_view.getRows()
	r = collections.OrderedDict()
	r['cols'] = cols
	r['rows'] = rows
		
	
	context = {'data': json.dumps(r),
			'bigName': 'Volunteers',
			'smallName': 'volunteers',
			'add': 'admin:bikurcholim_volunteers_add'}

	return render(request, 'bikurcholim/table_base.html', context)

@login_required(login_url='/bikurcholim/login/')
def clients(request):
	cols = client_view.getCols()
	rows = client_view.getRows()
	r = collections.OrderedDict()
	r['cols'] = cols
	r['rows'] = rows
		
	
	context = {'data': json.dumps(r),
			'bigName': 'Clients',
			'smallName': 'clients',
			'add': 'admin:bikurcholim_clients_add'}

	return render(request, 'bikurcholim/table_base.html', context)

@login_required(login_url='/bikurcholim/login/')
def cases(request):
	cols = case_view.getCols()
	rows = case_view.getRows()
	r = collections.OrderedDict()
	r['cols'] = cols
	r['rows'] = rows
		
	
	context = {'data': json.dumps(r),
			'bigName': 'Cases',
			'smallName': 'cases',
			'add': 'admin:bikurcholim_cases_add'}

	return render(request, 'bikurcholim/table_base.html', context)

@login_required(login_url='/bikurcholim/login/')
def housingschedule(request):
	cols = housing_view.getCols()
	rows = housing_view.getRows()
	r = collections.OrderedDict()
	r['cols'] = cols
	r['rows'] = rows
		
	
	context = {'data': json.dumps(r),
			'bigName': 'Housing Schedule',
			'smallName': 'housingschedule',
			'add': 'admin:bikurcholim_housingschedule_add'}

	return render(request, 'bikurcholim/table_base.html', context)

@login_required(login_url='/bikurcholim/login/')
def cases_advanced(request):
	values_list = request.POST['data']
	checkedCols = request.POST['checkedCols']
	json_object = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(values_list)
	
	cols=json_object['cols']

	rows=[]
	ccx=0
	
	for row in json_object['rows']:
		ccx=0
		r = collections.OrderedDict()
		for key, value in row.iteritems():
			if(key in checkedCols):
				r[key]=value
			ccx+=1
		rows.append(r)

	context = {}
	context = {'data': json.dumps(rows),
			'bigName': 'Cases',
			'smallName': 'cases',}
	return render(request, 'bikurcholim/cases_advanced.html', context)

@login_required(login_url='/bikurcholim/login/')
def volunteers_advanced(request):
	values_list = request.POST['data']
	checkedCols = request.POST['checkedCols']
	json_object = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(values_list)
	
	cols=json_object['cols']

	rows=[]
	ccx=0
	
	for row in json_object['rows']:
		ccx=0
		r = collections.OrderedDict()
		for key, value in row.iteritems():
			if(key in checkedCols):
				r[key]=value
			ccx+=1
		rows.append(r)	
	
	context = {}
	context = {'data': json.dumps(rows),
			'bigName': 'Volunteers',
			'smallName': 'volunteers',}
	return render(request, 'bikurcholim/volunteers_advanced.html', context)

@login_required(login_url='/bikurcholim/login/')
def clients_advanced(request):
	values_list = request.POST['data']
	checkedCols = request.POST['checkedCols']
	json_object = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(values_list)
	
	cols=json_object['cols']

	rows=[]
	ccx=0
	
	for row in json_object['rows']:
		ccx=0
		r = collections.OrderedDict()
		for key, value in row.iteritems():
			if(key in checkedCols):
				r[key]=value
			ccx+=1
		rows.append(r)	
	
	context = {}
	context = {'data': json.dumps(rows),
			'bigName': 'Clients',
			'smallName': 'clients',}
	return render(request, 'bikurcholim/clients_advanced.html', context)

@login_required(login_url='/bikurcholim/login/')
def housingschedule_advanced(request):
	values_list = request.POST['data']
	checkedCols = request.POST['checkedCols']
	json_object = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(values_list)
	
	cols=json_object['cols']

	rows=[]
	ccx=0
	
	for row in json_object['rows']:
		ccx=0
		r = collections.OrderedDict()
		for key, value in row.iteritems():
			if(key in checkedCols):
				r[key]=value
			ccx+=1
		rows.append(r)	
	
	context = {}
	context = {'data': json.dumps(rows),
			'bigName': 'Housing Schedule',
			'smallName': 'housingschedule',}
	return render(request, 'bikurcholim/housingschedule_advanced.html', context)

def test(request):
	context = []
	return render(request, 'bikurcholim/test.html', context)

class VolunteersDetailView(generic.DetailView):

	model = Volunteers

	def get_context_data(self, **kwargs):
		context = super(VolunteersDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		url = 'admin:bikurcholim_volunteers_change'
		context['change'] = url
		return context

class ClientsDetailView(generic.DetailView):

	model = Clients

	def get_context_data(self, **kwargs):
		context = super(ClientsDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		url = 'admin:bikurcholim_clients_change'
		context['change'] = url
		return context
	
class CasesDetailView(generic.DetailView):

	model = Cases

	def get_context_data(self, **kwargs):
		context = super(CasesDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		url = 'admin:bikurcholim_cases_change'
		context['change'] = url
		return context

class HousingScheduleDetailView(generic.DetailView):

	model = HousingSchedule

	def get_context_data(self, **kwargs):
		context = super(HousingScheduleDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		url = 'admin:bikurcholim_housingschedule_change'
		context['change'] = url
		return context
	
def user_login(request):
	# Like before, obtain the context for the user's request.
	context = RequestContext(request)

	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']
		nextpost = request.POST['next']
		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				if len(nextpost) > 0:
					return HttpResponseRedirect(nextpost)
				else:
					return HttpResponseRedirect('bikurcholim')
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your Bikur Cholim account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			#print "Invalid login details: {0}, {1}".format(username, password)
			context = {
				'next': nextpost,
				'error': "Invalid login details supplied."
			}
			return render(request, 'bikurcholim/login.html', context)
			#return HttpResponse("Invalid login details supplied.")

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		next = request.GET.get('next')
		context = {
			'next': next,
		}
		return render(request, 'bikurcholim/login.html', context)

def export_xls(request):
	book = xlwt.Workbook(encoding='utf8')
	sheet = book.add_sheet('untitled')

	default_style = xlwt.Style.default_style
	datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
	date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')
	
	values_list = request.POST['data']
	checkedCols = request.POST['checkedCols']
	json_object = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(values_list)
	
	heading_xf = ezxf('font: bold on; align: horiz center')
	cols=json_object['cols']
	colx=0
	cc = []
	for col in cols:
		if(col in checkedCols):
			cc.append(True)
			if(colx==0):
				sheet.write(0, colx, 'Id', heading_xf)
			else:
				sheet.write(0, colx, cols[col]['friendly'], heading_xf)
			colx+=1
		else:
			cc.append(False)
	rowx = 1
	
	for row in json_object['rows']:
		colx=0
		ccx=0
		for key in row:
			if(cc[ccx]):
				value=row[key]
				
				if isinstance(value, datetime.datetime):
					style = datetime_style
				elif isinstance(value, datetime.date):
					style = date_style
				else:
					style = default_style
#				if(value==True):
#					sheet.write(rowx, colx, 'True', style=style)
#				else:
				sheet.write(rowx, colx, value, style=style)
				colx+=1
			ccx+=1
		rowx+=1	
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename=example.xls'
	book.save(response)
	return response

def events(request):
	start = request.POST['start']
	end = request.POST['end']
	data_type = request.POST['data_type']
	#csrfmiddlewaretoken = request.POST['csrfmiddlewaretoken']
	
	if(data_type=='services'):
		rows = service_events_view.getRows(start, end)
	elif(data_type=='housing'):
		rows = housing_events_view.getRows(start, end)
	context = {}
	context = {'data': json.dumps(rows)}
	return HttpResponse(json.dumps(rows))
    