from readline import get_current_history_length
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.template.context import RequestContext

from project.settings import LOGOUT_REDIRECT_URL
from .models import Member, announcement
from .forms import MembersUpdateForm, UserRegisterForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import MembersForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import csv


# def exportcsv(request):
#     students = Member.objects.all()
#     response = HttpResponse('text/csv')
#     response['Content-Disposition'] = 'attachment; filename=students.csv'
#     writer = csv.writer(response)
#     writer.writerow(['ID', 'RollNo', 'Class', 'First Name', 'Last Name'])
#     studs = students.values_list('id','password','last_login',"is_superuser";"username";"first_name";"last_name";"email";"is_staff";"is_active";"date_joined"
# )
#     for std in studs:
#         writer.writerow(std)
#     return response
def welcome(request):    
    if request.user.is_superuser or request.user.is_staff:
        return redirect('dashboard')
    elif request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    
    return render(request,'user/welcome.html',{'title': 'SCIMS'})  

def register(request):  
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        user_form = UserRegisterForm(data = request.POST)
        form = MembersForm(request.POST, request.FILES)

        if user_form.is_valid() and form.is_valid():
            user = user_form.save()
            user.is_active = 0
            user.save()
            profile = form.save()
            profile.userstatus = 0
            profile.user = user
            profile.save()
            # current_site = get_current_site(request)
            subject = 'Registration of account'
            message = render_to_string('user/acc_active_email.html')
            user.email_user(subject, message)
            return redirect('login')

    else:
        user_form = UserRegisterForm()
        form = MembersForm()
    # else:
    #     return redirect('error')
            

    return render(request,'user/signup.html',{'user_form':user_form,'form':form, 'title': 'Sign Up'})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def loginview(request):   #login mayaten

    if request.user.is_superuser or request.user.is_staff:
        return redirect('dashboard')
    elif request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
 
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        #AuthenticationForm_can_also_be_used__
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            if user.is_superuser == 1:
                login(request, user)
                return redirect('dashboard')
            elif user.is_staff == 1:
                login(request, user)
                return redirect('dashboard')
            elif user.is_active == 0 and user.member.userstatus == '0' or user.member.userstatus == '4':
                messages.info(request,'Account is not yet activated.')
            # elif user.member.userstatus == '0':
            #     messages.error(request, "Account is not yet activated.")
            # elif user.member.userstatus == '1':
            #    login(request, user)
            #    return redirect('index')
            else:
                login(request, user)
                return redirect('index')
                # return redirect('error')
        else:
            messages.info(request, 'Invalid username or password.')
            # current = user.profile.user_role
        # try:
        #     if current == '0':
        #         return redirect('index')
                
        #     if current == '2':
        #         return redirect('staff/manage-members')
            
        # except:
        #         messages.error(request, 'Invalid email or password')
    # else:
    #     messages.error(request, 'Invalid username or password.')
    
    form = AuthenticationForm()

    return render(request, 'user/login.html', {'form':form,'title':'Log in'})
@login_required
def updateuser(request, pk):
    member = User.objects.get(pk=pk)
    
    form = UserRegisterForm(request.POST or None, instance=member)

    if request.POST and form.is_valid():
        form.save()
        return redirect('manage-users')

def logout_view(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect('login')

@login_required
def addmember(request):
    if request.user.is_superuser:
        return redirect('dashboard')
    if request.method == "POST":
        
        user_form = UserRegisterForm(data = request.POST)
        form = MembersForm(request.POST, request.FILES)

        if user_form.is_valid() and form.is_valid():

            user = user_form.save()
            user.save()
            profile = form.save()
            profile.userstatus = 1
            profile.user = user
            profile.save()
            messages.info(request, "Member has been added successfully.")
            return redirect('add-member')

    else:
        user_form = UserRegisterForm()
        form = MembersForm()

    return render(request,'user/add-member.html',{'user_form':user_form,'form':form})


def addbarangayuser(request):
    form = BarangayUserForm(request.POST or None, request.FILES or None)#######tuy nga part direkta
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('manage-members')

    return render(request,'user/add-barangay-user.html',{'form': form})
@login_required
class IndexView(ListView):
    template_name = 'user/manage-members.html'
    context_object_name = 'member_list'
    
    def get_queryset(self):
        return Member.objects.all()
    
@login_required
def managemembers(request):
    member_list = Member.objects.exclude(userstatus=0).exclude(userstatus=4)
    return render(request, 'user/manage-members.html', {'member': member_list, 'title':'Manage Members'})

class MemberDetailView(DetailView):
    model = Member
    template_name = 'user/info-member.html'
    context_object_name = 'member'
@login_required
def dashboard(request):
    if request.user.is_superuser == 1 or request.user.is_staff == 1:
        user = request.user.username
        total_members = Member.objects.all()
        male = Member.objects.filter(sex=0).count()
        female = Member.objects.filter(sex=1).count()
        announcements = announcement.objects.all()
        users = User.objects.all()
        staff = User.objects.filter(is_staff=1).count()
        active = User.objects.filter(is_active=1).count()
        inactive = User.objects.filter(is_active=0).count()
        
        context = {'total_members': total_members,
               'male': male,
               'female': female,
               'current': user,
               'title':'SCIMS',
               'announcements': announcements,
               'active': active,
               'users': users,
               'staff': staff,
               'inactive': inactive,
               } 
    else:
        return redirect('error')
    
    return render(request, 'user/dashboard.html', context)
@login_required
def allmembers(request):
    member_list = Member.objects.exclude(userstatus=0).exclude(userstatus=4)
    
    
    return render(request, 'user/all-members.html', {'member': member_list, 'title': 'All Members'})

def allmembersaccount(request):
    member_list = User.profile.filter()
    
    return render(request, 'user/all-members-account.html', {'members': member_list, 'title': 'All Members Account'})


#user
@login_required
def index(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('dashboard')
    
    user = request.user.username
    total_members = Member.objects.all()
    announcements = announcement.objects.all()
    
    context = {'total_members': total_members,
               'announcements': announcements,
               'current': user,
               'title':'SCIMS'}
    
    return render(request, 'user/index.html', context)
@login_required
def printID(request): #member print ID
    user = request.user.username
    total_members = Member.objects.all()
    
    context = {'total_members': total_members,
               'current': user}
    
    return render(request, 'user/printID.html', context)
@login_required
def memberprofile(request): #member profile
    if request.user.is_superuser:
        return redirect('error')
    else:
        
        user = request.user.username
        age1 = request.user.member.date_of_birth
        total_members = Member.objects.all()
        from datetime import datetime
        import math
        # dob = age1.year
        # tod = datetime.date.year
        # age = (tod.year - dob.year)
        age = math.trunc(((datetime.now().date() - request.user.member.date_of_birth).days / 365)) 
        
        
    
        context = {'total_members': total_members,'current': user, 'age': age, 'title': 'View Profile'}
    
    return render(request, 'user/member-profile.html', context)

def error(request): #member profile
    return render(request, 'user/error-404.html')
@login_required
def print(request, pk): #member profile
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'user/print.html')



#admin
@login_required
def deletemember(request, pk):
    member = get_object_or_404(Member, pk=pk)
    messages.info(request, "Member has been deleted successfully.")
    member.delete()
    return redirect('all-members')

@login_required
def deleterequest(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()
    messages.info(request, "Member request declined successfully.")
    return redirect('member-requests')

@login_required
def accept(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.userstatus = 1
    member.user.is_active = 1
    messages.info(request, "Member has been accepted successfully.")
    member.save()
    # current_site = get_current_site(request)
    # subject = 'Activate Your MySite Account'
    # message = render_to_string('user/acc_active_email.html')
    # member.email_user(subject, message)

    # messages.success(request, ('Please Confirm your email to complete registration.'))
    return redirect('member-requests')

@login_required
def updatemember(request, pk):
    member = Member.objects.get(pk=pk)
    
    form = MembersUpdateForm(request.POST or None, request.FILES or None, instance=member)

    if request.POST and form.is_valid():
        form.save()
        messages.info(request, "Member details has been updated successfully.")
        return redirect('manage-members')
    
    
    return render(request, 'user/update-member.html', {'form':form, 'title':'Update Member'})

def setactive(request):
    form  = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.is_active = False
        user.save()
    return redirect('manage-members')

#report
def agereport(request):
    user = request.user.username
    total_members = Member.objects.all()
    
    context = {'total_members': total_members,
               'current': user,
               'title':'SCIMS'}
    
    return render(request, 'user/age-report.html', context)

@login_required
def sexreport(request):
    from django.shortcuts import render
    from .models import Member
    
    labels = []
    data = []

    male = Member.objects.filter(sex=0).count()
    female = Member.objects.filter(sex=1).count()
    labels.append("Male")
    labels.append("Female")
    data.append(male)
    data.append(female)
    
    total = male + female    
    return render(request, 'user/sex-report.html', {'total': total, 'male':male, 'female':female, 'title':'Gender Report', 'labels': labels, 'data': data})
        

@login_required
def brgyreport(request):
    labels = []
    data = []
    
    
    labels.append("Amunitan")
    labels.append("Batangan")
    Amunitan = Member.objects.filter(barangay=0).count()

    data.append(Amunitan)

    Batangan = Member.objects.filter(barangay=1).count()

    data.append(Batangan)

    Baua = Member.objects.filter(barangay=2).count()
    labels.append("Baua")
    data.append(Baua)

    CabanbananNorte = Member.objects.filter(barangay=3).count()
    labels.append("Cabanbanan Norte")
    data.append(CabanbananNorte)

    CabanbananSur = Member.objects.filter(barangay=4).count()
    labels.append("Cabanbanan Sur")
    data.append(CabanbananSur)

    Cabiraoan = Member.objects.filter(barangay=5).count()
    labels.append("Cabiraoan")
    data.append(Cabiraoan)

    Callao = Member.objects.filter(barangay=6).count()
    labels.append("Callao")
    data.append(Callao)

    Calayan = Member.objects.filter(barangay=7).count()
    labels.append("Calayan")
    data.append(Calayan)

    Caroan = Member.objects.filter(barangay=8).count()
    labels.append("Caroan")
    data.append(Caroan)

    Casitan = Member.objects.filter(barangay=9).count()
    labels.append("Casitan")
    data.append(Casitan)

    Flourishing = Member.objects.filter(barangay=10).count()
    labels.append("Flourishing")
    data.append(Flourishing)

    Ipil = Member.objects.filter(barangay=11).count()
    labels.append("Ipil")
    data.append(Ipil)

    Isca = Member.objects.filter(barangay=12).count()
    labels.append("Isca")
    data.append(Isca)

    Magrafil = Member.objects.filter(barangay=13).count()
    labels.append("Magrafil")
    data.append(Magrafil)

    Minanga = Member.objects.filter(barangay=14).count()
    labels.append("Minanga")
    data.append(Minanga)

    Rebecca = Member.objects.filter(barangay=15).count()
    labels.append("Rebecca")
    data.append(Rebecca)

    Paradise = Member.objects.filter(barangay=16).count()
    labels.append("Paradise")
    data.append(Paradise)

    Pateng = Member.objects.filter(barangay=17).count()
    labels.append("Pateng")
    data.append(Pateng)

    Progressive = Member.objects.filter(barangay=18).count()
    labels.append("Progressive")
    data.append(Progressive)

    SanJose = Member.objects.filter(barangay=19).count()
    labels.append("San Jose")
    data.append(SanJose)

    SantaClara = Member.objects.filter(barangay=20).count()
    labels.append("Santa Clara")
    data.append(SantaClara)

    SantaCruz = Member.objects.filter(barangay=21).count()
    labels.append("Santa Cruz")
    data.append(SantaCruz)

    SantaMaria = Member.objects.filter(barangay=22).count()
    labels.append("Santa Maria")
    data.append(SantaMaria)

    Smart  = Member.objects.filter(barangay=23).count()
    labels.append("Smart")
    data.append(Smart)

    Tapel = Member.objects.filter(barangay=24).count()
    labels.append("Tapel")
    data.append(Tapel)

    barangays = Amunitan+Batangan+Baua+CabanbananNorte+CabanbananSur+Cabiraoan+Callao+Calayan+Caroan+Casitan+Flourishing+Ipil+Isca+Magrafil+Minanga+Rebecca+Paradise+Pateng+Progressive+SanJose+SantaClara+SantaCruz+SantaMaria+Smart+Tapel
    # no = Member.objects.filter(barangay).count()
    return render(request, 'user/barangay-report.html', {'barangays':barangays, 'labels': labels, 'data': data, 'Amunitan': Amunitan, 'Batangan': Batangan, 'Baua': Baua, 'CabanbananNorte': CabanbananNorte, 'CabanbananSur': CabanbananSur, 'Cabiraoan': Cabiraoan, 'Callao': Callao, 'Calayan': Calayan, 'Caroan': Caroan, 'Casitan': Casitan, 'Flourishing': Flourishing, 'Ipil': Ipil, 'Isca': Isca, 'Magrafil': Magrafil, 'Minanga': Minanga, 'Rebecca': Rebecca, 'Paradise': Paradise, 'Pateng': Pateng, 'Progressive': Progressive, 'SanJose': SanJose, 'SantaClara': SantaClara, 'SantaCruz': SantaCruz, 'SantaMaria': SantaMaria, 'Smart': Smart, 'Tapel': Tapel})

#users
@login_required
def adduser(request):
    form = UserRegisterForm(request.POST or None)
    form.is_staff = 1
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('manage-users')
    return render(request,'user/add-user.html',{'form': form})

@login_required
def manageusers(request):
    users = User.objects.exclude(is_superuser=1).exclude(is_active=0)
    return render(request, 'user/manage-users.html', {'users': users, 'title':'Manage Users'})
    
@login_required
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.info(request, "User has been deleted successfully.")
    return redirect('manage-users')


class userdetails(DetailView):
    model = User
    template_name = 'user/info-user.html'
    context_object_name = 'user'
 
@login_required    
def userpage(request):  #signup senior citizen
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    elif request.user.is_superuser or  request.user.is_staff:
        return redirect('dashboard')
    if request.method == "POST":
        user_form = UserRegisterForm(data = request.POST)
        profile_form = MembersForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.save()
            profile = profile_form.save()
            profile.user = user
            profile.save()
            return redirect('index')

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserRegisterForm()
        profile_form = MembersForm()

    return render(request,'user/user.html',{'user_form':user_form,'profile_form':profile_form})

@login_required 
def memberrequests(request):
    
    member_list = Member.objects.filter(userstatus=0)
    
    
    return render(request, 'user/member-requests.html', {'member': member_list, 'title':'Member Requests'})

#users
def activeusers(request):
    
    users= User.objects.filter(is_active=1)
    return render(request, 'user/active-users.html', {'users': users, 'title':'Active Users'})
 
def blockedusers(request):
     
    users = User.objects.filter(is_active=0)
    return render(request, 'user/blocked-users.html', {'users': users, 'title':'Blocked Users'})

def activateaccount(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active =True
    messages.info(request, "User has been activated successfully.")
    user.save()
    
    return redirect('blocked-users')

def deactivateaccount(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = False
    messages.info(request, "User has been deactivated successfully.")
    user.save()
    
    return redirect('active-users')

def assignstaff(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_staff = True
    user.member.userstatus = 1
    messages.info(request, "User has been assigned as staff successfully.")
    user.save()
    
    return redirect('manage-users')


def unassignstaff(request, pk):
    user = get_object_or_404(User, pk=pk)
    messages.info(request, "User has been unassigned as staff successfully.")
    user.is_staff = False
    user.save()
    
    return redirect('manage-users')

@login_required
def addannouncement(request):
    if request.POST['title'] and request.POST['desc']:
        announcement.objects.create(title=request.POST['title'], desc=request.POST['desc'])
        messages.info(request, "Announcement has been posted successfully.")
    return redirect('dashboard')
@login_required
def deleteannouncement(request, pk):
    announcements = get_object_or_404(announcement, pk=pk)
    messages.info(request, "Announcement has been deleted successfully.")
    announcements.delete()
    return redirect('dashboard')

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'accounts/change_password.html', {
#         'form': form
#     })

@login_required
def statusreport(request):    
    labels = []
    data = []
        
    labels.append("Active")
    Active = Member.objects.filter(userstatus=1).count()
    data.append(Active)
    
    labels.append("Inactive")
    Inactive = Member.objects.filter(userstatus=2).count()
    data.append(Inactive)
    
    total = Active + Inactive
    return render(request, 'user/status-report.html', {'total': total, 'labels': labels, 'data': data, 'Active': Active, 'Inactive': Inactive})