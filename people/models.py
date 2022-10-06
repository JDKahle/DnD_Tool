from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    image = models.URLField(default='https://d1vzi28wh99zvq.cloudfront.net/images/8957/298771.png', blank=True)

    caste = models.CharField(max_length=100, blank=True)

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    team_role = models.CharField(max_length=250, blank=True)
    
    weapon = models.CharField(max_length=250, blank=True)
    shield = models.CharField(max_length=250, blank=True)
    
    outfit = models.CharField(max_length=250, blank=True)
    armor = models.CharField(max_length=250, blank=True)




    lvl = models.IntegerField(default=0, blank=True, null=True)
    xp = models.IntegerField(default=0, blank=True, null=True)
    ac = models.IntegerField(default=10, blank=True, null=True)
    hp = models.IntegerField(default=4, blank=True, null=True)
    speed = models.IntegerField(default=30, blank=True, null=True)



    str = models.IntegerField(default=10, blank=True, null=True)
    dex = models.IntegerField(default=10, blank=True, null=True)
    con = models.IntegerField(default=10, blank=True, null=True)
    int = models.IntegerField(default=10, blank=True, null=True)
    wis = models.IntegerField(default=10, blank=True, null=True)
    cha = models.IntegerField(default=10, blank=True, null=True)

    passive_perception = models.IntegerField(default=10, blank=True, null=True)

    languages = models.CharField(max_length=250, blank=True)
 
    description = models.TextField(blank=True, null=True)
    inventory = models.TextField(blank=True, null=True)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    



    def __str__(self):
        return f"{self.first_name} is equpped with a {self.weapon} and wears {self.armor}."