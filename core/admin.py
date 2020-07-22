from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Admin View of AAI Maintaince"
admin.site.site_title = "My Admin"
admin.site.index_title = "Admin View of AAI Maintaince"


admin.site.register(Airports)
admin.site.register(Profile)
admin.site.register(Equipments)
admin.site.register(Stations)
admin.site.register(Glid_Path)
admin.site.register(COMSOFT)
admin.site.register(VCS_System)
admin.site.register(Localizer)
admin.site.register(DVOR)
admin.site.register(NDB)
admin.site.register(Datis_Terma)
admin.site.register(DVTR)
admin.site.register(UPS)
