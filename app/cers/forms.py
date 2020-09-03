from dal import autocomplete
from django import forms
from .models import User, Attendance


class UserSearchForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', )
        widgets = {
            'user': autocomplete.ModelSelect2(url='user-autocomplete')
        }
