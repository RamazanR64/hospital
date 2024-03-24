from django.contrib import admin
from .models import Specialization, Visit, Patient, Service

# Configure the display of Specialization admin page
@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

