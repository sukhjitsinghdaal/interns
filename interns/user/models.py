from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import (BaseUserManager ,AbstractBaseUser)
import datetime


class UserManager(BaseUserManager):

    def create_user(self,email,password = None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email = email)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,password):
        if password is None:
            raise TypeError('Superusers must have a password.') 

        user = self.create_user(email = email ,password = password)
        user.is_staf = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique = True,null = True)

    is_staff = models.BooleanField(default = True)
    is_active  = models.BooleanField(default = True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
   
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin



class ProjectUser(User):
    user_role = models.CharField(max_length=255,null=True,blank=True)
    email_varified = models.BooleanField(default = False)
   
from Meta.models import Qualification,QualificationType

class Customer(models.Model):
    customer_id = models.OneToOneField(ProjectUser, on_delete = models.CASCADE)
    first_name  = models.CharField(max_length = 200,blank = True,null = False,verbose_name = 'First Name')
    last_name = models.CharField(max_length = 255,blank = True,null = False,verbose_name = 'Last Name')
    date_of_birth = models.DateTimeField(blank=True, null=True)
    gender  = models.CharField(max_length=55,default = "male")
    profile_image = models.ImageField(upload_to = 'profile_pic_folder',default = '',blank=True,null=True )
    phone = models.CharField(max_length = 16)
    batch = models.CharField(max_length=255,null=True,blank=True)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE,null=True,blank=True)
    qualification_type_id = models.ForeignKey(QualificationType,on_delete=models.CASCADE,null=True,blank=True)   
    
    




 