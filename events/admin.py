from django.contrib import admin
from .models import Events, EventImage,  InformationImage, Impressum

#admin.site.site_header = 'DHL-Sommerkino Dashoboard '
#admin.site.site_title = 'Dhl-Sommerkino'

class EventImageInline(admin.TabularInline):
    model = EventImage

@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]

admin.site.register(Impressum)

admin.site.register(InformationImage)
