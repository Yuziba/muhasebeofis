from django.contrib import admin
from muhasebeapp.models import MuhasebeModel

class MuhasebeAdmin(admin.ModelAdmin):
    fields = ['message','nickname']

admin.site.register(MuhasebeModel, MuhasebeAdmin)