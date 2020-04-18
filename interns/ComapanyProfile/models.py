from django.db import models
from Meta.models import QualificationType,Country,City,State

class Company(models.Model):
    name = models.CharField(max_length=255)
    name_profile  = models.CharField(max_length=255)
    with_job = models.BooleanField(default=False)
    duration = models.CharField(max_length=255)
    name_category = models.CharField(max_length=255) 
    website_link = models.CharField(max_length=255,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True )
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True )
    state = models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True )
    stipend = models.CharField(max_length=255,null=True,blank=True)
    startdate = models.DateField(auto_now_add=True)



