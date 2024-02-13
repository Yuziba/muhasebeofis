from django.db import models
from django.contrib.auth.models import User



class MuhasebeModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    onayno = models.CharField(max_length = 100)
    onayaciklama = models.CharField(max_length = 100, default='my_default_value')
    onaytar = models.CharField(max_length = 12)
    onay_odemetutar = models.CharField(max_length = 20)
    onay_parabirimi = models.CharField(max_length = 20)
    onay_odemeyolu = models.CharField(max_length = 20)

    def __str__(self):
        return f"Tweet nick: {self.username} Belgeno: {self.onayno} Aciklama: {self.onayaciklama} Tarih: {self.onaytar} Odeme Tutrari: {self.onay_odemetutar} Para Birimi: {self.onay_parabirimi} Odeme youlu: {self.onay_odemeyolu}"

class OnayBelgeModel(models.Model):
    dosya = models.FileField(upload_to='belgeler/')
    yukleme_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dosya.name