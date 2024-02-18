from django.urls import path, include

from . import cal
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'muhasebeapp'

urlpatterns = [
    path('', views.main, name="main"),
    path('addtweet', views.addtweet, name="addtweet"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('deletetweet/<int:id>',views.deletetweet, name="deletetweet"), #burda id almamiz gerek
    path('onaybelgeler/', views.onayBelgeler, name='onaybelgeler'),
    path('api/', include('muhasebeapp.api.urls')),  # Yeni eklenen satır drag and drop icin
    path('belge/sil/<int:belge_id>/', views.belge_sil, name='sil_belge'),
    path('belge/indir/<int:belge_id>/', views.belge_indir, name='indir_belge'),
    path('upload', views.file_upload_view, name="file-upload"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)