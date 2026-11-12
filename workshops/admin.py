import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Workshop, Registration

def export_registrations_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="workshop_registrations.csv"'
    
    writer = csv.writer(response)
    
    writer.writerow(['ID', 'Participant Name', 'Email', 'Phone', 'Workshop Title', 'Registration Date'])
    
   
    for reg in queryset:
        writer.writerow([reg.id, reg.full_name, reg.email, reg.phone, reg.workshop.title, reg.registered_at])
        
    return response

export_registrations_to_csv.short_description = "Export selected registrations to CSV"

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'speaker', 'capacity')
    search_fields = ('title', 'speaker')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'workshop', 'email', 'phone', 'registered_at')
    list_filter = ('workshop', 'registered_at')
    search_fields = ('full_name', 'email')
    actions = [export_registrations_to_csv]