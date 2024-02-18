from django.shortcuts import render, redirect
from muhasebeapp.forms import AddTweetModelForm
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import DocumentForm, OnayBelgeForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import OnayBelgeModel
import os

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
    



"""        Onay Belge Yukleme          """

from django.core.files.storage import FileSystemStorage
from .forms import OnayBelgeForm  # OnayBelgeForm'unuzun doğru import edildiğinden emin olun
from .models import OnayBelgeModel  # OnayBelgeModel'inizin doğru import edildiğinden emin olun

def onayBelgeler(request):
    onayBelgeler = OnayBelgeModel.objects.all()

    if request.method == 'POST':
        form = OnayBelgeForm(request.POST, request.FILES)
        if form.is_valid():
            # Dosyayı belirli bir dizine kaydetmek için FileSystemStorage kullanımı
            fs = FileSystemStorage()
            dosya = form.cleaned_data['dosya']
            dosya_adi = fs.save(dosya.name, dosya)

            # Kaydedilen dosyanın yolu
            dosya_yolu = fs.url(dosya_adi)

            # OnayBelgeModel'e eklemek (isteğe bağlı)
            OnayBelgeModel.objects.create(dosya=dosya_yolu)

            return redirect('muhasebeapp:onaybelgeler')
    else:
        form = OnayBelgeForm()

    return render(request, 'muhasebeapp/onaybelgeler.html', {'form': form, 'onayBelgeler': onayBelgeler})

from django.shortcuts import redirect
from .models import OnayBelgeModel
import os

from django.shortcuts import redirect
from .models import OnayBelgeModel
import os
from django.conf import settings

def belge_sil(request, belge_id):
    try:
        belge = OnayBelgeModel.objects.get(id=belge_id)
        if belge:
            file_path = os.path.join(settings.MEDIA_ROOT, belge.dosya.name)
            if os.path.exists(file_path):
                # Dosyayı sistemden sil
                os.remove(file_path)
                
            # Veritabanından belgeyi sil
            belge.delete()
            
            # Model alanını güncelleyerek sayfadan isminin silinmesini sağla
            OnayBelgeModel.objects.filter(id=belge_id).update(dosya='')

    except OnayBelgeModel.DoesNotExist:
        # Belge bulunamazsa
        pass

    return redirect('muhasebeapp:onaybelgeler')



from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.utils.text import slugify
import os
from .models import OnayBelgeModel
from urllib.parse import unquote, unquote_plus

def belge_indir(request, belge_id):
    belge = get_object_or_404(OnayBelgeModel, id=belge_id)

    try:
        
        from django.utils.text import get_valid_filename
    
        file_name = belge.dosya.name.split("/")[-1]
        print("file adi ",file_name)
        dosya_adi, dosya_uzantisi = os.path.splitext(unquote(file_name))

        print("dosya adi", dosya_adi + dosya_uzantisi)
        
        # Dosyayı aç ve kullanıcıya gönder
        #file_path = os.path.join(default_storage.location, belge.dosya.name[1:].replace("/", os.path.sep))
        file_path = default_storage.path(belge.dosya.name[1:])
        base_path = os.path.dirname(file_path)
        #print("Base Path:", base_path)  
        dd = belge.dosya.name.split("/media/")[-1]
        file_path = default_storage.path(belge.dosya.name[1:])
        base_path = os.path.dirname(file_path)
        base_path_without_media = os.path.dirname(base_path)
        file_path = base_path_without_media+"\\"+dd
        file_path = file_path.replace("\\", "/")
        print("File Path:", file_path)  
        #print("File Path Exists:", os.path.exists(file_path))
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = FileResponse(file)
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                return response
        else:
            raise Http404("Belirtilen belge bulunamadı.")
    except FileNotFoundError:
        raise Http404("Belirtilen belge bulunamadı.")



