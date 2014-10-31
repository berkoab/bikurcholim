import collections
from bikurcholim.models import Cases
from datetime import datetime
from datetime import timedelta

def format_datetime(dt):
	return dt.strftime('%Y-%m-%dT%H:%M:%S')
def getRows(sd, ed):
	events=[]
	start_date = datetime.strptime(sd, "%Y-%m-%d").date()-timedelta(days=1)
	end_date = datetime.strptime(ed, "%Y-%m-%d").date() 

	d = Cases.objects.filter(date_of_service__range=(start_date, end_date))
	#o = VolunteerOptions.objects.all()

	for c in d:
		event = collections.OrderedDict()
		event['id'] = c.id
		event['title'] = c.client.get_name()
		event['start'] = format_datetime(c.date_of_service)
		event['end'] = format_datetime(c.date_of_service+timedelta(hours=1))
		event['service'] = c.service.service
		event['url'] = '/admin/bikurcholim/cases/' + str(c.id)
		events.append(event)
	return events