from django.contrib import admin
from .models import PDBUser


@admin.register(PDBUser)
class PDBUserAdmin(admin.ModelAdmin):
    change_form_template = 'loginas/change_form.html'
