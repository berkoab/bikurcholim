from django.http import HttpResponse
from django.shortcuts import render
from bikurcholim.models import Volunteers
from bikurcholim.models import Clients

def index(request):
    return HttpResponse("Hello, world. You're at the bikurcholim index.")

def volunteers(request):
	data = Volunteers.objects.all()
	context = {'volunteers': data}
	return render(request, 'bikurcholim/volunteers.html', context)

def clients(request):
	data = Clients.objects.all()
	context = {'clients': data}
	return render(request, 'bikurcholim/clients.html', context)