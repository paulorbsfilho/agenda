from django.forms import *

from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'cell', 'email')


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'members')
        widgets = {'members': CheckboxSelectMultiple()}