from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Document, Member, announcement

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )

class LoginForm(forms.Form):
    class Meta:
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget = forms.TextInput(attrs= {'placeholder':'Email'}), required=False)
    username = forms.CharField(label="Username", widget = forms.TextInput(attrs= {'placeholder':'Username'}))
    password1 = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget = forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

civilstatus = (
    ('', 'Choose...'),
    ('1', 'Single'),
    ('2', 'Married'),
    ('3', 'Widowed')
)

sex= (
    ('', 'Choose...'),
    ('M', 'Male'),
    ('F', 'Female')
)

        
class MembersForm(forms.ModelForm):
    last_name = forms.CharField(label="Last Name", widget = forms.TextInput(attrs= {'placeholder':'Last Name'}))
    first_name = forms.CharField(label="First Name", widget = forms.TextInput(attrs= {'placeholder':'First Name'}))
    middle_name = forms.CharField(label="Middle Name", widget = forms.TextInput(attrs= {'placeholder':'Middle Name'}))
    name_ext = forms.CharField(label="Ext.", widget = forms.TextInput(attrs= {'placeholder':'Sr., III'}), required=False)
    place_of_birth = forms.CharField(max_length=30)
    contact_number = forms.IntegerField(label="Contact Number", widget = forms.TextInput(attrs= {'placeholder':'Contact Number'}))
    occupation = forms.CharField(label="Occupation", widget = forms.TextInput(attrs= {'placeholder':'Occupation'}))
    skills = forms.CharField(label="Skills", widget = forms.TextInput(attrs= {'placeholder':'Skills'}))
    annual_income = forms.IntegerField(label="Annual Income", widget = forms.TextInput(attrs= {'placeholder':'Annual Income'}))     
    date_of_birth =forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={ 'type': 'date'}))
    place_of_birth = forms.CharField(label="Place of Birth", widget = forms.TextInput(attrs= {'placeholder':'Place of Birth'}))
    # civilstatus = forms.CharField(label="Place of Birth", widget = forms.TextInput(attrs= {'placeholder':'Place of Birth'}))
    # fam_member = forms.SelectMultiple()
    # fam_member = forms.SelectMultiple()
    # image = forms.Im/ageField()
    class Meta:
        # specify model to be used
        model = Member

        # specify fields to be used
        fields = ['last_name', 'first_name', 'middle_name', 'name_ext','barangay','date_of_birth', 'place_of_birth', 'contact_number', 'sex', 'civilstatus', 'occupation', 'skills', 'annual_income', 'img', 'documents']   

class MembersUpdateForm(forms.ModelForm):
    last_name = forms.CharField(label="Last Name", widget = forms.TextInput(attrs= {'placeholder':'Last Name'}))
    first_name = forms.CharField(label="First Name", widget = forms.TextInput(attrs= {'placeholder':'First Name'}))
    middle_name = forms.CharField(label="Middle Name", widget = forms.TextInput(attrs= {'placeholder':'Middle Name'}))
    name_ext = forms.CharField(label="Ext.", widget = forms.TextInput(attrs= {'placeholder':'Sr., III'}), required=False)
    place_of_birth = forms.CharField(max_length=30)
    contact_number = forms.IntegerField(label="Contact Number", widget = forms.TextInput(attrs= {'placeholder':'Contact Number'}))
    occupation = forms.CharField(label="Occupation", widget = forms.TextInput(attrs= {'placeholder':'Occupation'}))
    skills = forms.CharField(label="Skills", widget = forms.TextInput(attrs= {'placeholder':'Skills'}))
    annual_income = forms.IntegerField(label="Annual Income", widget = forms.TextInput(attrs= {'placeholder':'Annual Income'}))     
    date_of_birth =forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={ 'type': 'date'}))
    

    # fam_member = forms.SelectMultiple()
    # fam_member = forms.SelectMultiple()
    # image = forms.Im/ageField()
    class Meta:
        # specify model to be used
        model = Member

        # specify fields to be used
        fields = ['last_name', 'first_name', 'middle_name', 'name_ext','barangay','date_of_birth', 'place_of_birth', 'contact_number', 'sex', 'civilstatus', 'occupation', 'skills', 'annual_income', 'userstatus', 'img', 'documents']   

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

class Announcement(forms.ModelForm):
    class Meta:
        model = announcement
        fields = ['title', 'desc']

