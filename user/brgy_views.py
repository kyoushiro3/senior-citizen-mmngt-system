from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Member
from .forms import UserRegisterForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import MembersForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

#members
def addmember(request):
    form = MembersForm(request.POST or None, request.FILES or None)#######tuy nga part direkta
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('brgy/manage-members')

    return render(request,'brgy/add-member.html',{'form': form})

def showmembers(request):
    mem = request.user()
    brgy = mem.barangay_users.barangay
    
    data = Member.objects.filter(barangay=brgy)
    
    stu = {
    "members": data
    }
    return render(request, 'brgy/manage-members.html',stu)

class IndexView(ListView):
    template_name = 'brgy/manage-members.html'
    context_object_name = 'member_list'
    username = "San Jose"
    
    def get_queryset(self):
        return BarangayUser.objects.barangay
    
class MemberDetailView(DetailView):
    model = Member
    template_name = 'brgy/info-member.html'
    context_object_name = 'member'
    
    
def deletemember(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()
    return redirect('brgy/manage-members')

def updatemember(request, pk):
    member = Member.objects.get(pk=pk)
    form = MembersForm(request.POST or None, instance=member)

    if request.POST and form.is_valid():
        form.save()
        return redirect('brgy/manage-members/')
    return render(request, 'brgy/update-member.html', {'form':form})

def index(request): 
    return render(request, 'brgy/index.html',{'title':'Dashboard'})