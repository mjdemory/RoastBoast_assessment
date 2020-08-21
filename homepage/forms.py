from django import forms
from homepage.models import RoastBoastModel


class InputThoughtsForm(forms.ModelForm):
    class Meta:
        model = RoastBoastModel
        fields = ['choices', 'body']
