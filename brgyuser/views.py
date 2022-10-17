# from django.shortcuts import render,redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate,login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
# from .models import Member
# from .forms import UserRegisterForm
# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from django.template import Context
# from .forms import MembersForm
# from django.views.generic import ListView, DetailView
# from django.contrib.auth.mixins import  LoginRequiredMixin

# def login(request):
#     form = AuthenticationForm()
    
#     if request.method == 'POST':

#         #AuthenticationForm_can_also_be_used__

#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_authenticated == False:
#             login(request,user)
#             if request.GET.get('next'):
#                 return redirect(request.GET.get('next'))
#             else:
                
#             # messages.success(request, f' wecome {username} !!')
#                 return redirect('index')
#         else:
#             messages.info(request, f'Account does not exists.')
#     return render(request, 'user/login.html', {'form':form,'title':'log in'})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST) or None
#         if form.is_valid():
#             username = request.POST.get('username')
#             #########################mail####################################
#             htmly = get_template('user/Email.html')
#             d = { 'username': username }
#             subject, from_email, to = 'hello', 'from@example.com', 'to@emaple.com'
#             html_content = htmly.render(d)
#             msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
#             msg.attach_alternative(html_content, "text/html")
#             try:
#                 msg.send()
#             except:
#                 print("error in sending mail")
#             ##################################################################
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'user/signup.html', {'form': form,'title':'reqister here'})


# def addmember(request):
#     form = MembersForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('manage-members')

#     return render(request,'user/add-member.html',{'form': form})

# class IndexView(LoginRequiredMixin, ListView):
#     template_name = 'user/manage-members.html'
#     context_object_name = 'member_list'

#     def get_queryset(self):
#         return Member.objects.all()

# def managemembers(request):
#     member_list = Member.objects.all()
#     return render(request, 'user/manage-members.html', {'member': 'member_list'})

# class MemberDetailView(DetailView):
#     model = Member
#     template_name = 'user/info-member.html'
#     context_object_name = 'member'

# def signup(request):
#     return render(request, 'user/signup.html')
# ##################################################################
# ####################index#######################################
# @login_required
# def index(request):
#     return render(request, 'user/index.html',{'title':'index'})

# ########################################################################
# # ########### register here #####################################
# # def signup(request):
# #     if request.method == 'POST':
# #         form = UsersForm(request.POST) or None
# #         if form.is_valid():
# #             form.save()
# #             return redirect(request, 'user/index.html', {})
# #             # return redirect('dashboard.html')
# #     else:
# #         form = UsersForm()

# #     return render(request,'user/signup.html',{'form': form})



# ###################################################################################
# ################login forms###################################################


