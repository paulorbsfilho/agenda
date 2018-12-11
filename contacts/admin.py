from django.contrib import admin

# Register your models here.

from django.contrib import admin

from contacts.models import *

admin.site.register(Contact)
admin.site.register(Group)