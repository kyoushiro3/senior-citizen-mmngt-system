"""iert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
    
        path('',views.welcome,name='welcome'),
        path('add-announcement', views.addannouncement, name='announcement'),
        path('delete-announcement/<int:pk>/', views.deleteannouncement, name='delete-announcement'),
        #admin urls
        path('dashboard',views.dashboard,name='dashboard'),
         path('add-member/', views.addmember, name='add-member'),
         path('info-member/<int:pk>/', views.MemberDetailView.as_view(), name='info-member'),
         path('manage-members/', views.managemembers, name='manage-members'),  
         path('update-member/<int:pk>/', views.updatemember, name='update-member'),
         path('delete-member/<int:pk>/', views.deletemember, name='delete-member'),
         path('delete-request/<int:pk>/', views.deleterequest, name='delete-request'),
        # path('add-user/', views.adduser, name='add-user'),
        path('info-user/<int:pk>/', views.userdetails.as_view(), name='info-user'),
        path('update/<int:pk>/', views.updateuser, name='update-user'),
        path('manage-users/', views.manageusers, name='manage-users'),
        path('active-users/', views.activeusers, name='active-users'), 
        path('blocked-users/', views.blockedusers, name='blocked-users'), 
        
        
        path('delete/<int:pk>/', views.delete_user, name='delete-user'),
        path('add-barangay-user/', views.addbarangayuser, name='add-barangay-user'),
        path('all-members-account', views.allmembersaccount, name='all-members-account'),
        path('member-requests', views.memberrequests, name='member-requests'),
        path('accept/<int:pk>/', views.accept, name='accept'),
        # path('login3', views.loginview2, name='login2'), 
        #staff
        path('all-members', views.allmembers, name='all-members'),
        path('activateaccount/<int:pk>/', views.activateaccount, name='activateaccount'),
        path('deactivateaccount/<int:pk>/', views.deactivateaccount, name='deactivateaccount'),
        path('assign-staff/<int:pk>/', views.assignstaff, name='assign-staff'),
        path('usassign-staff/<int:pk>/', views.unassignstaff, name='unassign-staff'),
                
        #client urls
        path('index',views.index,name='index'),
        path('user', views.userpage, name = "userpage"),
        path('printID',views.printID, name='printt'),
        path('member-profile',views.memberprofile, name='member-profile'),
        path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
        
        
        # path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
        # path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
        #path('password-change-done/$', auth_views.password_change_done, {'template_name': 'cadmin/password_change_done.html'}, name='password_change_done'),
        
        path('print/<int:pk>/',views.print,name='print'),
        path('error',views.error,name='error'),
        path('set-active', views.setactive, name='set-active'),
        
        #report
        path('age-report', views.agereport, name='age-report'),
        path('sex-report', views.sexreport, name='sex-report'),
        path('brgy-report', views.brgyreport, name='brgy-report'), 
        path('status-report', views.statusreport, name='status-report'), 
] 

