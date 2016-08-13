from django import forms


class SessionForm(forms.Form):
    distance = forms.IntegerField()
    duration = forms.IntegerField()
