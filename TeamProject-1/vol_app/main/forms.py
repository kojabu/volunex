from django import forms
from .models import *


EVENT_CATEGORY = list()
for  i in range(Category.objects.all().count()):
    EVENT_CATEGORY.append((i+1,Category.objects.all()[i].name))
print(EVENT_CATEGORY)

NAME_ORGANIZATION = list()
for  i in range(Organization.objects.all().count()):
    NAME_ORGANIZATION.append((i+1,Organization.objects.all()[i].name))
print(NAME_ORGANIZATION)

EVENT_LEVEL = list()
for  i in range(Level.objects.all().count()):
    EVENT_LEVEL.append((i+1,Level.objects.all()[i].name))
print(EVENT_LEVEL)

class AddEVentForm2(forms.Form):
    name = forms.CharField(max_length=60)
    pre_description = forms.CharField(max_length=100)
    description = forms.CharField()
    date = forms.DateField()
    category = forms.TypedChoiceField(choices=EVENT_CATEGORY, coerce=str)
    organization = forms.TypedChoiceField(choices=NAME_ORGANIZATION, coerce=str)
    level = forms.TypedChoiceField(choices=EVENT_LEVEL)
    photo = forms.ImageField(required=False)
    points = forms.IntegerField()




