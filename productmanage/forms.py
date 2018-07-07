from django import forms
from mainapp.models import Bike


class BikeChangeForm(forms.ModelForm):

    class Meta:
        model = Bike
        # fields = 'all'
        exclude = ('id',)
