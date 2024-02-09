from django.forms import ModelForm
from muhasebeapp.models import MuhasebeModel


class AddTweetModelForm(ModelForm):
    class Meta:
        model = MuhasebeModel
        # fields = ["nickname", "message"]  //model alaninda username olarak degistirdik
        fields = ["username", "message"]