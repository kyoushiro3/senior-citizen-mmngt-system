from datetime import date
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.hashers import make_password
from django.db import models
from django.urls import reverse
from django.db.models.fields import BigAutoField
from django.db.models.fields.related import OneToOneField
from django.dispatch import receiver
from django.db.models.signals import post_save

class Document(models.Model):
     document = models.FileField(upload_to='documents/')
# class CustomUser(AbstractUser):
#     user_type_data = ((1, "Admin"), (2, "Barangay User"), (3, "Senior Citizen"))
#     user_type = models.CharField(default='1', choices=user_type_data, max_length=10)

# class Admin(models.Model):
#     id = models.AutoField(primary_key = True)
#     admin = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
# class User(AbstractUser):
#     is_member = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
       
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    last_name = models.CharField(max_length=25, null=True)
    first_name = models.CharField(max_length=25, null=True)
    middle_name = models.CharField(max_length=25, null=True)
    name_ext = models.CharField(max_length=5, null=True)
    barangay_choices = (('0', 'Amunitan'),('1', 'Batangan'),('2', 'Baua'),('3', 'Cabanbanan Norte'),('4', 'Cabanbanan Sur'),('5', 'Cabiraoan'),('6', 'Callao'),('7', 'Calayan'),('8', 'Caroan'),('9', 'Casitan'),('10', 'Flourishing'),('11', 'Ipil'),('12', 'Isca'),('13', 'Magrafil'),('14', 'Minanga'),('15', 'Rebecca'),('16', 'Paradise'),('17', 'Pateng'),('18', 'Progressive'),('19', 'San Jose'),('20', 'Santa Clara'),('21', 'Santa Cruz'),('22', 'Santa Maria'),('23', 'Smart'),('24', 'Tapel'))
    barangay = models.CharField(max_length=2, choices=barangay_choices, default=0)
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=30, null=True)
    contact_number = models.BigIntegerField(null=True)
    sex_choices = (('0', 'Male'),('1', 'Female'),)
    sex = models.CharField(max_length=1, choices=sex_choices, null=True)
    civilstatus_choices = (('0', 'Single'), ('1', 'Married'), ('3', 'Widowed'),)
    civilstatus = models.CharField(max_length=1, choices=civilstatus_choices)
    occupation = models.CharField(max_length=30, null=True)
    skills = models.CharField(max_length=1000, null=True)
    annual_income = models.BigIntegerField(null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_status_choices = (('0', 'Pending'),('1', 'Active'),('2', 'Inactive'))
    userstatus = models.CharField(max_length=1, choices=user_status_choices, default='1', null=True)
    img = models.ImageField(upload_to='images/', null=True)
    documents = models.FileField(upload_to='documents/', null=True)
    # image = models.ImageField(upload_to='images/')
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.user.username
    # def image_tag(self):
    #     return mark_safe(<)
    # def get_absolute_url(self):
    #     return reverse('classroom:student_detail',kwargs={'pk':self.pk})
    # def age(self):
    #     import datetime
    #     dob = self.date_of_birth.year
    #     tod = datetime.date.year
    #     my_age = (tod.year - dob.year) 
    #     return my_age
        
        
    class Meta:
        db_table = "tbl_members"

class announcement(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

          
        

    

    
