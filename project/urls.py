"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from .router import router
from rest_framework.authtoken import views
from user import views

urlpatterns = [

    path('admin/', admin.site.urls),

    ######### api path ##########################

    path('api/',include(router.urls)),
    # path('api-token-auth/',views.obtain_auth_token,name='api-tokn-auth'),

    #####user related path##########################
    path('',include('user.urls')),
    path('login/',views.loginview,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/',views.register,name='signup'),
    # path('jet/', include('jet.urls', 'jet')),
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    # path('password_reset/$', auth_views.PasswordResetView,
    #     {'template_name': "users/registration/password_reset_form.html"},
    #     name='password_reset'),
    # path('password_reset/done/$', auth_views.PasswordResetDoneView,
    #     {'template_name': "users/registration/password_reset_done.html"},
    #     name='password_reset_done'),
    # path('reset/(?P<uidb64>[0-9A-Za-z_-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.PasswordResetConfirmView,
    #     {'template_name': "users/registration/password_reset_confirm.html"},
    #     name='password_reset_confirm'),
    # path('reset/done/$', auth_views.PasswordResetCompleteView,
    #     {'template_name': "users/registration/password_reset_complete.html"},
    #     name='password_reset_complete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
