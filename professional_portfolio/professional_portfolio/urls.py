"""
URL configuration for professional_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from portfolio_webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('fullstack-portfolio/',views.fullstack_portfolio, name='fullstack_portfolio'),
    path('react/',views.react, name='react'),
    path('angular/',views.angular, name='angular'),
    path('node/',views.node, name='node'),
    path('djangoFlask/',views.djangoFlask, name='flaskDjango'),
    path('powerApps/',views.powerApps, name='powerApps'),
    path('csharp/',views.csharp, name='csharp'),
    path('rpa-portfolio/',views.rpa_portfolio, name='rpa_porfolio')

]
