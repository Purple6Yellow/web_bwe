from django.contrib import admin
from .models import Atel, Wacht, Reserve, Prog

admin.site.site_header = "Admin Omgeving Stichting BWE"

admin.site.register(Atel)
admin.site.register(Wacht)
admin.site.register(Reserve) 

@admin.register(Prog)
class ProgAdmin(admin.ModelAdmin):
    list_display = ( "datum", "titel")
    list_filter = ("datum",)
    pass

#admin.site.register(Prog) 