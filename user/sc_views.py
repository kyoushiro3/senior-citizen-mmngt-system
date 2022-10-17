from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Member, Family
from .forms import UserRegisterForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import MembersForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User









 
 