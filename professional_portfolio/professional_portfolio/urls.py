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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('fullstack-portfolio/',views.fullstack_portfolio, name='fullstack_portfolio'),
    path('react/',views.react, name='react'),
    path('angular/',views.angular, name='angular'),
    path('node/',views.node, name='node'),
    path('djangoFlask/',views.djangoFlask, name='flaskDjango'),
    path('powerApps/',views.powerApps, name='powerApps'),
    path('csharp/',views.csharp, name='csharp'),
    path('rpa-portfolio/',views.rpa_portfolio, name='rpa_porfolio'),
    path('cloud-scripting/',views.cloud_scripting, name='cloud_scripting'),
    path('selenium/',views.selenium, name='selenium'),
    path('powerautomate/',views.powerautomate, name='powerautomate'),
    path('powerautomate-desktop/',views.powerautomate_desktop, name='powerautomate_desktop'),
    path('uipath/',views.uipath, name='uipath'),
    path('virtual-agents/',views.virtual_agents, name='virtual_agents'),
    path('machinelearning-portfolio/',views.machinelearning_portfolio, name='machinelearning_portfolio'),
    path('supervisedlearning/',views.supervisedlearning, name='supervisedlearning'),
    path('unsupervisedlearning/',views.unsupervisedlearning, name='unsupervisedlearning'),
    path('industry40-portfolio/',views.industry40_portfolio, name='industry40_portfolio'),
    path('industrialapplications/',views.industrialapplications, name='industrialapplications'),
    path('industrialsimulations/',views.industrialsimulations, name='industrialsimulations')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

