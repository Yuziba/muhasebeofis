from django.forms import ModelForm
from muhasebeapp.models import MuhasebeModel


class AddTweetModelForm(ModelForm):
    class Meta:
        model = MuhasebeModel
        #fields = ["username", "onayno", "onayaciklama"]
        fields = "__all__"