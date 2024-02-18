from django import forms
from django.forms import ModelForm
from muhasebeapp.models import MuhasebeModel
from muhasebeapp.models import OnayBelgeModel


class AddTweetModelForm(ModelForm):
    class Meta:
        model = MuhasebeModel
        #fields = ["username", "onayno", "onayaciklama"]
        fields = "__all__"

class OnayBelgeForm(ModelForm):
    class Meta:
        model = OnayBelgeModel
        fields = ['dosya']

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')

