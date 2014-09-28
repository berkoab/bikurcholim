from django.contrib import admin
from bikurcholim.models import Neighborhoods
from bikurcholim.models import Vehicles
from bikurcholim.models import Volunteers
from bikurcholim.models import VolunteerOptions
from bikurcholim.models import ClientStatus
from bikurcholim.models import Cities
from bikurcholim.models import Hospitals
from bikurcholim.models import TikvahHouses
from bikurcholim.models import Clients
from bikurcholim.models import CaseStatus
from bikurcholim.models import Cases
from bikurcholim.models import VolunteerOptionValues

class VolunteerOptionsInline(admin.TabularInline):
    model = VolunteerOptions
    extra = 3
		
class VolunteersAdmin(admin.ModelAdmin):
	inlines = [VolunteerOptionsInline]
	list_display = ('last_name', 'first_name')
	list_filter = ['neighborhood']
	search_fields = ['last_name', 'first_name', 'street']
	fieldsets = [
		(None, {'fields': ['first_name', 'last_name', 'address', 'city', 'neighborhood', 'work_place', 'medical_training', 'home_phone', 
		'cell_phone', 'email_address', 'vehicle', 'other_languages', 'other_specialties']}),
		('Times Available', {'fields': ['start_time_available', 'end_time_availalable']}),
		('Days Available', {'fields': [('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'shabbos')]}),
		(None, {'fields': ['days_and_times_available_notes']})
	]

admin.site.register(Neighborhoods)
admin.site.register(Vehicles)
admin.site.register(Volunteers, VolunteersAdmin)
admin.site.register(VolunteerOptions)
admin.site.register(ClientStatus)
admin.site.register(Cities)
admin.site.register(Hospitals)
admin.site.register(TikvahHouses)
admin.site.register(Clients)
admin.site.register(CaseStatus)
admin.site.register(Cases)
admin.site.register(VolunteerOptionValues)

admin.AdminSite.site_header="Bikur Cholim Database Administration"