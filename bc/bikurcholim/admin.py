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


admin.site.register(Neighborhoods)
admin.site.register(Vehicles)
admin.site.register(Volunteers)
admin.site.register(VolunteerOptions)
admin.site.register(ClientStatus)
admin.site.register(Cities)
admin.site.register(Hospitals)
admin.site.register(TikvahHouses)
admin.site.register(Clients)
admin.site.register(CaseStatus)
admin.site.register(Cases)

