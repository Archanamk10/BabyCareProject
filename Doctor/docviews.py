from django.http import HttpResponse
from django.shortcuts import render
#import MySQLdb
import MySQLdb
import simplejson as json
import random
import urllib.request
import webbrowser
from datetime import date

conn=MySQLdb.connect("localhost","root","","babycare")
c=conn.cursor()


def doctorhome(request):
    return render(request,'Doctor_home.html')

def viewmothers(request):
    doctor_id=request.session['userid']
    get_panchayah="select district,panchayath from doctor where doctor_id='"+str(doctor_id)+"'"
    c.execute(get_panchayah)
    doc_details=c.fetchone()
    str1="select * from mother_reg where district='"+str(doc_details[0])+"' and panchayath='"+str(doc_details[1])+"'"
    print(str1)
    c.execute(str1)
    view_data=c.fetchall()
    return render(request,'doctor_View_Mother.html',{"data":view_data})