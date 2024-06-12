from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Events)
admin.site.register(Category)
admin.site.register(Organization)
admin.site.register(Level)
admin.site.register(UserPoints)