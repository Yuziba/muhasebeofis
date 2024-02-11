from django.shortcuts import render, redirect
from muhasebeapp.forms import AddTweetModelForm
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def main(request):
    all_tweets = models.MuhasebeModel.objects.all()
    tweetdict = {"tweets": all_tweets}
    return render(request, 'muhasebeapp/main.html', context=tweetdict)


def addtweet(request):
    if request.POST:
        onayno          = request.POST.get("onayno", "")
        onayaciklama    = request.POST.get("onayaciklama", "")

        onaytar         = request.POST.get("onaytar", "")
        onay_odemetutar = request.POST.get("onay_odemetutar", "")
        onay_parabirimi = request.POST.get("onay_parabirimi", "")
        onay_odemeyolu  = request.POST.get("onay_odemeyolu", "")
        models.MuhasebeModel.objects.create(username=request.user, onayno=onayno, onayaciklama=onayaciklama, onaytar=onaytar, onay_odemetutar=onay_odemetutar, onay_parabirimi= onay_parabirimi,onay_odemeyolu=onay_odemeyolu,)
        return redirect(reverse('muhasebeapp:main'))
    else:
        return render(request, 'muhasebeapp/addtweet.html')
    
 

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
 

#kullaniciya kendi tweetini silme yetkisi verdirtme
@login_required
def deletetweet(request, id):
    tweet = models.MuhasebeModel.objects.get(pk=id)
    if request.user == tweet.username:                      #kontrol
        models.MuhasebeModel.objects.filter(id=id).delete() #silme kodu
        return redirect('muhasebeapp:main')                 #yonlendirme *ayni sayfa
    

