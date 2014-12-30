import collections
from bikurcholim.models import HousingSchedule
from datetime import datetime
from datetime import timedelta
from django.core.urlresolvers import reverse_lazy

def format_datetime(dt, start):
	if(start):
		return dt.strftime('%Y-%m-%d')
	else:
		dt = dt + timedelta(days=1)
		return dt.strftime('%Y-%m-%d')
def getRows(sd, ed):
	events=[]
	start_date = datetime.strptime(sd, "%Y-%m-%d").date()
	end_date = datetime.strptime(ed, "%Y-%m-%d").date()

	d = HousingSchedule.objects.filter(from_date__range=(start_date, end_date))
	#o = VolunteerOptions.objects.all()
	
	
	for c in d:
		event = collections.OrderedDict()
		event['id'] = c.id
		event['title'] = c.house.name + ' - ' + c.case.get_name()
		event['start'] = format_datetime(c.from_date, True)
		event['end'] = format_datetime(c.to_date, False)
		event['color'] = c.get_color()
		event['url'] = str(reverse_lazy('housingschedule')) + str(c.id)
		event['name'] = c.case.get_name()
		events.append(event)
	return events