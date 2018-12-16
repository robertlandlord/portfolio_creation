"""mysite URL Configuration

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
from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'), #main homepage
    re_path(r'^contact/$', views.contact, name='contact'), # contact page
    re_path(r'^register/$', views.UserFormView.as_view(), name='register'), #registration
    re_path(r'^login/$', views.LoginFormView.as_view() , name='login'), #login
    re_path(r'^logout/$',views.logout_user, name='logout'), #logout (redirects, just used as function)
    re_path(r'^password_change/$',views.PassChangeFormView.as_view(), name='pass_change'), # password changing

]
