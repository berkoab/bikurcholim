import collections
from bikurcholim.models import ClientService
from datetime import datetime
from datetime import timedelta
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
import json

def format_datetime(dt):
	return dt.strftime('%Y-%m-%dT%H:%M:%S')
def getRows(sd, ed, services):
	events=[]
	start_date = datetime.strptime(sd, "%Y-%m-%d").date()-timedelta(days=1)
	end_date = datetime.strptime(ed, "%Y-%m-%d").date() 

	d = ClientService.objects.filter(Q(begin_date__range=(start_date, end_date))|Q(end_date__range=(start_date, end_date)))
	d = d.filter(service__service__in=json.loads(services))
	d = d.filter(status__status='Open')
	for c in d:
		event = collections.OrderedDict()
		event['id'] = c.id
		event['title'] = c.client.get_name()
		event['start'] = format_datetime(c.begin_date)
		event['end'] = format_datetime(c.end_date+timedelta(hours=1))
		event['service'] = c.service.service
		event['color'] = c.get_color()
		event['url'] = str(reverse_lazy('clientservice')) + str(c.id)
		events.append(event)
	return events