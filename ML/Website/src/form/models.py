from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
# from django.utils import time
import datetime

NOTES = [
        (1, "Nul"),
        (2, "Passable"),
        (3, "Assez Bien"),
        (4, "Bien"),
        (5, "Tres Bien")
    ]


# Create your models here.
class FormAvis(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    avis = models.TextField(blank=True)
    note = models.IntegerField(choices=NOTES, default=1)
    date = models.DateField(auto_now=False)
    rate = models.IntegerField(default=1)


