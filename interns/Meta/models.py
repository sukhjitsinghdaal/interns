from django.db import models




class Duration(models.Model):
    name = models.CharField(max_length=255)

#engineering ,BA
class QualificationType(models.Model):
    qualification_type_name = models.CharField(max_length=255) 

#computer sciece, mechanical
class Qualification(models.Model):
    qualification_name = models.CharField(max_length=255)
    qualification_type_fk = models.ForeignKey(QualificationType,on_delete=models.CASCADE, null=True, blank= True)

class Country(models.Model):
    name = models.CharField(max_length=255)

class State(models.Model):
    name = models.CharField(max_length=255)
    country_fk = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank= True)

class City(models.Model):
    name = models.CharField(max_length=255)
    state_fk = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank= True)

class Category(models.Model):
    cat_name = models.CharField(max_length=255)
