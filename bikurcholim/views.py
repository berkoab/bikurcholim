from bikurcholim.models import Cases, Volunteers, IntakeCalls, HousingSchedule, Tasks, ClientService, OtherOptions, Services
from bikurcholim.models import ClientServiceForm
from django.forms.models import modelformset_factory
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views import generic
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import volunteer_view, case_view, intakecalls_view, housing_view, service_events_view, housing_events_view, tasks_view, services_view
import collections
import datetime
import json
import re
import xlwt
ezxf = xlwt.easyxf

@login_required(login_url=reverse_lazy('login'))
def index(request):
	tasks = Tasks.objects.all().filter(status__status__iexact='open')
	clients = Cases.objects.all().filter(status__status__iexact='active')
	context = {'tasks': tasks,
			'clients': clients}
	return render(request, 'bikurcholim/index.html', context)
   
def get_table_rows(view):
	cols = view.getCols()
	rows = view.getRows()
	r = collections.OrderedDict()
	r['cols'] = cols
	r['rows'] = rows
	return r

def get_context(data, bigName, smallName, add):
	context = {'data': json.dumps(data),
			'bigName': bigName,
			'smallName': smallName,
			'add': add}
	return context

@login_required(login_url=reverse_lazy('login'))
def volunteers(request):
	r = get_table_rows(volunteer_view)
	context = get_context(r, 'Volunteers', 'volunteers', 'admin:bikurcholim_volunteers_add')
	return render(request, 'bikurcholim/table_base.html', context)

@login_required(login_url=reverse_lazy('login'))
def cases(request):
	r = get_table_rows(case_view)		
	context = get_context(r, 'Cases', 'cases', 'admin:bikurcholim_cases_add')
	return render(request, 'bikurcholim/table_base.html', context)

@login_required(login_url=reverse_lazy('login'))
def intakecalls(request):
	r = get_table_rows(intakecalls_view)		
	context = get_context(r, 'Intake Calls', 'intakecalls', 'admin:bikurcholim_intakecalls_add')
	return render(request, 'bikurcholim/table_base.html', context)

@login_required(login_url=reverse_lazy('login'))
def tasks(request):
	r = get_table_rows(tasks_view)		
	context = get_context(r, 'Tasks', 'tasks', 'admin:bikurcholim_tasks_add')
	return render(request, 'bikurcholim/table_base.html', context)

@login_required(login_url=reverse_lazy('login'))
def clientservice(request):
	r = get_table_rows(services_view)		
	context = get_context(r, 'Client Services', 'clientservice', 'admin:bikurcholim_clientservice_add')
	return render(request, 'bikurcholim/table_base.html', context)

@login_required(login_url=reverse_lazy('login'))
def housingschedule(request):
	r = get_table_rows(housing_view)		
	context = get_context(r, 'Housing Schedule', 'housingschedule', 'admin:bikurcholim_housingschedule_add')
	return render(request, 'bikurcholim/table_base.html', context)

def get_context_advanced(data, bigName, smallName):
	context = {'data': json.dumps(data),
			'bigName': bigName,
			'smallName': smallName}
	return context

@login_required(login_url=reverse_lazy('login'))
def intakecalls_advanced(request):
	rows = get_advanced_rows(request)
	context = get_context_advanced(rows, 'Intake Calls', 'intakecalls')
	return render(request, 'bikurcholim/intakecalls_advanced.html', context)

def get_advanced_rows(request):
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
	return rows

def tasks_advanced(request):
	rows = get_advanced_rows(request)
	context = get_context_advanced(rows, 'Tasks', 'tasks')
	return render(request, 'bikurcholim/tasks_advanced.html', context)

@login_required(login_url=reverse_lazy('login'))
def volunteers_advanced(request):
	rows = get_advanced_rows(request)	
	context = get_context_advanced(rows, 'Volunteers', 'volunteers')
	return render(request, 'bikurcholim/volunteers_advanced.html', context)

@login_required(login_url=reverse_lazy('login'))
def cases_advanced(request):
	rows = get_advanced_rows(request)
	context = get_context_advanced(rows, 'Cases', 'cases')
	return render(request, 'bikurcholim/cases_advanced.html', context)

@login_required(login_url=reverse_lazy('login'))
def clientservice_advanced(request):
	rows = get_advanced_rows(request)
	context = get_context_advanced(rows, 'ClientServices', 'clientservice')
	return render(request, 'bikurcholim/clientservice_advanced.html', context)

@login_required(login_url=reverse_lazy('login'))
def housingschedule_advanced(request):
	rows = get_advanced_rows(request)
	context = get_context_advanced(rows, 'Housing Schedule', 'housingschedule')
	return render(request, 'bikurcholim/housingschedule_advanced.html', context)

def test(request):
	context = []
	return render(request, 'bikurcholim/test.html', context)

class VolunteersDetailView(generic.DetailView):

	model = Volunteers
	prefetch_related = ['other_options']
	#otheroptions = OtherOptions.objects.filter(id=model)
	def get_context_data(self, **kwargs):
		context = super(VolunteersDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		url = 'admin:bikurcholim_volunteers_change'
		context['change'] = url
		#context['otheroptions'] = otheroptions
		return context

class CasesDetailView(generic.DetailView):

	model = Cases

	def get_context_data(self, **kwargs):
		context = super(CasesDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		url = 'admin:bikurcholim_cases_change'
		context['change'] = url
		return context
	
class IntakeCallsDetailView(generic.DetailView):

	model = Cases

	def get_context_data(self, **kwargs):
		context = super(IntakeCallsDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		url = 'admin:bikurcholim_intakecalls_change'
		context['change'] = url
		return context

class ClientServiceDetailView(generic.DetailView):

	model = ClientService

	def get_context_data(self, **kwargs):
		context = super(ClientServiceDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		url = 'admin:bikurcholim_clientservice_change'
		context['change'] = url
		return context
	
class TasksDetailView(generic.DetailView):

	model = Tasks

	def get_context_data(self, **kwargs):
		context = super(TasksDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		url = 'admin:bikurcholim_tasks_change'
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
	services = request.POST['services']
	#csrfmiddlewaretoken = request.POST['csrfmiddlewaretoken']
	
	if(data_type=='services'):
		rows = service_events_view.getRows(start, end, services)
	elif(data_type=='housing'):
		rows = housing_events_view.getRows(start, end)
	context = {}
	context = {'data': json.dumps(rows)}
	return HttpResponse(json.dumps(rows))

@login_required(login_url=reverse_lazy('login'))
def servicescalendar(request):
	services = Services.objects.all()
	context = {'services': services}
	return render(request, 'bikurcholim/servicescalendar.html', context)

@login_required(login_url=reverse_lazy('login'))
def housingcalendar(request):
	context = {}
	return render(request, 'bikurcholim/housingcalendar.html', context)

def gotoevent(request):
	url = request.POST['url']
	context = {}
	return render(request, url, context)

@login_required(login_url=reverse_lazy('login'))
def addcase(request):
	idFromPost = request.POST['id']
	url = request.POST['url']
	call = IntakeCalls.objects.get(pk=idFromPost)
	context = {}
	city = ''
	hospital = ''
	if call.city:
		city = '&city='+str(call.city.id)
	if call.hospital:
		hospital = '&hospital='+str(call.hospital.id)
	return redirect(url+'?first_name='+call.first_name
				+'&last_name='+call.last_name+city+hospital)
	
@login_required(login_url=reverse_lazy('login'))
def update_services(request):
    ClientFormSet = modelformset_factory(ClientService, form=ClientServiceForm, extra=0)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
    	formset = ClientFormSet(request.POST, request.FILES, 
							queryset=ClientService.objects.filter(status__status__exact='Open'))
        # create a form instance and populate it with data from the request:
        #form = ClientServiceForm(request.POST)
        # check whether it's valid:
        if formset.is_valid():
            success = 'Saved Successfully!!'
            formset.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render_to_response("bikurcholim/update_services.html", 
										{'success': success,"formset": formset,}
										, RequestContext(request))
            #return HttpResponseRedirect("bikurcholim/update_services.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        formset = ClientFormSet(queryset=ClientService.objects.filter(status__status__exact='Open'))

    return render_to_response("bikurcholim/update_services.html", {
        "formset": formset, }, RequestContext(request))
    #return render(request, 'update_services.html', {'form': form})