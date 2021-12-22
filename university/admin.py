from django.contrib import admin
from .models import Stud
from .models import Organization
from .models import Group

admin.site.register(Stud)
admin.site.register(Organization)
admin.site.register(Group)
# Register your models here.
