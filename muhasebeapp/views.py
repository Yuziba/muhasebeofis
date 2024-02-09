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
        #nickname = request.POST["nickname"]   modelde degisiklik yaptik
        message = request.POST["message"]
        #models.MuhasebeModel.objects.create(nickname=nickname, message=message)
        models.MuhasebeModel.objects.create(username=request.user, message=message)
        return redirect(reverse('muhasebeapp:main'))
    else:
        return render(request, 'muhasebeapp/addtweet.html')
    
@login_required(login_url="/login")
def addtweetbymodelform(request):
    if request.method == "POST":
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            #nickname = form.cleaned_data["nickname"]   //modelde username olarak degistirdik
            username = form.cleaned_data["username"]
            message = form.cleaned_data["message"]
            #models.MuhasebeModel.objects.create(nickname=nickname, message=message)        ////modelde username olarak degistirdik
            models.MuhasebeModel.objects.create(username=request.user, message=message) 
            return redirect(reverse('muhasebeapp:main'))
        else:
            print("error in form")
            return render(request, "muhasebeapp/addtweetbymodelform.html", context={"form":form})
    else:
        form = AddTweetModelForm()
        return render(request, "muhasebeapp/addtweetbymodelform.html", context={"form":form})
    

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
    

