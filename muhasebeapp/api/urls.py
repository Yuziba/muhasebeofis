# muhasebeapp/api/urls.py

from django.urls import path
from .views import BelgeSirasiView

urlpatterns = [
    path('guncelle-belge-sirasi/', BelgeSirasiView.as_view(), name='guncelle_belge_sirasi'),
]
