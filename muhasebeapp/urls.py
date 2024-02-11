from django.urls import path
from . import views

app_name = 'muhasebeapp'

urlpatterns = [
    path('', views.main, name="main"),
    path('addtweet', views.addtweet, name="addtweet"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('deletetweet/<int:id>',views.deletetweet, name="deletetweet"), #burda id almamiz gerek
]
