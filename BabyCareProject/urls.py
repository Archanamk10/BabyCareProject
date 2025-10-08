"""BabyCareProject URL Configuration

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
from django.contrib import admin
from django.urls import path
from.import CommonView
from government import govviews
from ashaworker import ashaviews
from Mother import motherviews
from Doctor import docviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',CommonView.index),
    path('login/',CommonView.login),
    #--------Government---------------
    path('adminhome/',govviews.adminhome),
    path('panchayathlink/',govviews.panchayathlink),
    path('panchayathreg/',govviews.panchayathreg),
    path('viewpanchayath/',govviews.viewpanchayath),
    path('workerlink/',govviews.workerlink),
    path('workerreg/',govviews.workerreg),
    path('viewworker/',govviews.viewworker),
    path('panchayathlistview/',govviews.panchayathlistview),
    path('projectlink/',govviews.projectlink),
    path('addproject/',govviews.addproject),
    path('viewprojects/',govviews.viewprojects),
    path('doctorlink/',govviews.doctorlink),
    path('adddoctor/',govviews.adddoctor),
    path('viewdoctor/',govviews.viewdoctor),
    path('allviews/',govviews.allviews),
    path('view_vacc/',govviews.view_vacc),
    path('view_food/',govviews.view_food),
    path('view_disease/',govviews.view_disease),
    path('view_health/',govviews.view_health),
    path('deletepanchayath/',govviews.deletepanchayath),
    path('deleteworker/',govviews.deleteworker),
    path('deleteproject/',govviews.deleteproject),
    path('deletedoctor/',govviews.deletedoctor),
    
     #--------Ashaworker---------------
    path('workerhome/',ashaviews.workerhome),
    path('govnotification/',ashaviews.govnotification),
    path('motherlink/',ashaviews.motherlink),
    path('addmother/',ashaviews.addmother),
    path('viewmother/',ashaviews.viewmother),
    path('alertlink/',ashaviews.alertlink),
    path('addvaccination/',ashaviews.addvaccination),
    path('viewvaccination/',ashaviews.viewvaccination),
    path('addfood/',ashaviews.addfood),
    path('viewfood/',ashaviews.viewfood),
    path('healthlink/',ashaviews.healthlink),
    path('addhealthtips/',ashaviews.addhealthtips),
    path('viewhealthtips/',ashaviews.viewhealthtips),
    path('adddisease/',ashaviews.adddisease),
    path('viewdisease/',ashaviews.viewdisease),
    path('deletemother/',ashaviews.deletemother),
    path('delete_vacc/',ashaviews.delete_vacc),
    path('delete_food/',ashaviews.delete_food),
    path('delete_tips/',ashaviews.delete_tips),
    path('delete_disease/',ashaviews.delete_disease),

   #--------Mother---------------
   path('motherhome/',motherviews.motherhome),
   path('vaccination_alerts/',motherviews.vaccination_alerts),
   path('food_details/',motherviews.food_details),
   path('health_tips/',motherviews.health_tips),
   path('disease_details/',motherviews.disease_details),

    #--------Doctor---------------
   path('doctorhome/',docviews.doctorhome),
   path('viewmothers/',docviews.viewmothers),
   
]
