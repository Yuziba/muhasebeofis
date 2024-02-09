from django.db import models
from django.contrib.auth.models import User

"""
class MuhasebeModel(models.Model):
    nickname = models.CharField(max_length = 50)
    message = models.CharField(max_length = 100)

    def __str__(self):
        return f"Tweet nick: {self.nickname} message: {self.message}"
"""

class MuhasebeModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length = 100)

    def __str__(self):
        return f"Tweet nick: {self.username} message: {self.message}"
