from django.http import HttpResponse,HttpResponseRedirect
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

def sendsms(ph,msg):
    sendToPhoneNumber= "+91"+ph
    userid = "2000022557"
    passwd = "54321@lcc"
    url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + "&msg=" + msg + "&userid=" + userid + "&password=" + passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)

def adminhome(request):
    return render(request,'Adminhome.html')

def panchayathlink(request):
    return render(request,'Panchayathlink.html')

def panchayathreg(request):
    if request.POST:
        pname=request.POST.get("pname")
        district=request.POST.get("district")
        wno=request.POST.get("wno")
        hno=request.POST.get("hno")
        president=request.POST.get("president")
        address=request.POST.get("address")
        email=request.POST.get("email")
        phn=request.POST.get("phn")

        pan_exists="select count(*) from panchayath_reg where name='"+str(pname)+"' and district='"+str(district)+"' or name='"+str(pname)+"' and phone_number='"+str(phn)+"'"
        print("-------"+pan_exists+"-------")
        c.execute(pan_exists)
        exisist_data=c.fetchone()
        try:
            if exisist_data[0]>0:
                message="Such details already exisist"
                return render(request,"PanchayathReg.html",{"message":message})
            else:
                pan_insert="insert into panchayath_reg(`name`,`district`,`ward_count`,`house_count`,`president_name`,`address`,`email`,`phone_number`)values('"+str(pname)+"','"+str(district)+"','"+str(wno)+"','"+str(hno)+"','"+str(president)+"','"+str(address)+"','"+str(email)+"','"+str(phn)+"')"
                c.execute(pan_insert)
                conn.commit()
                message="Added Successfully"
                return render(request,"PanchayathReg.html",{"message":message})
        except:
            message="Such details already exisist"
            return render(request,"PanchayathReg.html",{"message":message})

    return render(request,'PanchayathReg.html')

def viewpanchayath(request):
    view_pan="select * from panchayath_reg"
    c.execute(view_pan)
    view_data=c.fetchall()
    return render(request,'viewpanchayath.html',{"data":view_data})

def workerlink(request):
    return render(request,'Workerlink.html')

def workerreg(request):

    if request.POST:
        district=request.POST.get("district")
        panchayath=request.POST.get("panchayathlist")
        wnamee=request.POST.get("wnamee")
        wphnu=request.POST.get("wphnu")
        wan=request.POST.get("wan")
        waddress=request.POST.get("waddress")
        wmail=request.POST.get("wmail")
        qul=request.POST.get("qul")
        

        worker_exists="select count(*) from worker_reg where district='"+str(district)+"' and panchayath='"+str(panchayath)+"' and ward_no='"+str(wan)+"' or phone_no='"+str(wphnu)+"'"
        print("-------"+worker_exists+"-------")
        c.execute(worker_exists)
        exisist_data=c.fetchone()
        print(exisist_data)
        try:
            if exisist_data[0]>0:
                message="ashaworker already exisist"
                return render(request,"workerreg.html",{"message":message})
            else:
                
                random_num=random.randrange(1000,10000,2)
                print("--------password---- "+str(random_num))
                password="worker"+str(random_num)
                print(password)
                worker_insert="insert into worker_reg(`district`,`panchayath`,`worker_name`,`phone_no`,`ward_no`,`address`,`email`,`qualification`)values('"+str(district)+"','"+str(panchayath)+"','"+str(wnamee)+"','"+str(wphnu)+"','"+str(wan)+"','"+str(waddress)+"','"+str(wmail)+"','"+str(qul)+"')"
                worker_login="insert into login(userid,username,password,status,usertype)values((select max(wrkr_id) from worker_reg),'"+str(wphnu)+"','"+str(password)+"','1','worker')"
                c.execute(worker_insert)
                conn.commit()
                c.execute(worker_login)
                conn.commit()
                msg="Congratulations!!! Government added you as ashaworker in the "+panchayath+" panchayath for ward number :"+wan+" Username :"+wphnu+" Password: "+password
                sendsms(wphnu,msg)
                message="Added Successfully"
                return render(request,"workerreg.html",{"message":message})
        except:
            message="Such details already exisist"
            return render(request,"workerreg.html",{"message":message})

    return render(request,'workerreg.html')

def panchayathlistview(request):
  pan_list=[]
  did=request.GET.get("d_id")
  c.execute("select panchayath_id,name from panchayath_reg where district ='"+ str(did)+"'")
  data2=c.fetchall()
  for d in data2:
    pan_list.append(d[1])
  return HttpResponse(json.dumps(pan_list),content_type="application/json")

def viewworker(request):
    view_worker="select * from worker_reg"
    c.execute(view_worker)
    view_data=c.fetchall()
    return render(request,'viewworker.html',{"data":view_data})

def projectlink(request):
    return render(request,'Project_link.html')

def addproject(request):

    if request.POST:
        district=request.POST.get("district")
        panchayath=request.POST.get("panchayathlist")
        ptitle=request.POST.get("ptitle")
        pdescription=request.POST.get("pdescription")
        valiupto=request.POST.get("valiupto")
        posteddate=date.today()

        project_exists="select count(*) from projects where district='"+str(district)+"' and panchayath='"+str(panchayath)+"' and title='"+str(ptitle)+"' and posted_date='"+str(posteddate)+"'"
        print("-------"+project_exists+"-------")
        c.execute(project_exists)
        exisist_data=c.fetchone()
        print(exisist_data)
        # try:
        if exisist_data[0]>0:
                message="projects already exisist"
                return render(request,"workerreg.html",{"message":message})
        else:
                project_insert="insert into projects(`district`,`panchayath`,`title`,`details`,`posted_date`,`valid_upto`,`status`)values('"+str(district)+"','"+str(panchayath)+"','"+str(ptitle)+"','"+str(pdescription)+"','"+str(posteddate)+"','"+str(valiupto)+"','1')"
                c.execute(project_insert)
                conn.commit()
                msg="The Government added something new for your diary please check it on, don't be late posted on "+str(posteddate)
                project_sms="select phone_no from worker_reg where district='"+str(district)+"' and panchayath='"+panchayath+"'"
                c.execute(project_sms)
                phone_data=c.fetchall()
                for p in phone_data:
                    sendsms(p[0],msg)
                message="Project Added Successfully"
                return render(request,"Add_project.html",{"message":message})
        # except:
        #     message="Such details already exisist"
        #     return render(request,"Add_project.html",{"message":message})

    return render(request,'Add_project.html')

def viewprojects(request):
    view_projects="select * from projects"
    c.execute(view_projects)
    view_data=c.fetchall()
    return render(request,'viewprojects.html',{"data":view_data})

def doctorlink(request):
    return render(request,'Doctor_link.html')

def adddoctor(request):

    if request.POST:
        district=request.POST.get("district")
        panchayath=request.POST.get("panchayathlist")
        dname=request.POST.get("dname")
        dqual=request.POST.get("dqual")
        daddress=request.POST.get("daddress")
        dphnu=request.POST.get("dphnu")
        dopt=request.POST.get("dopt")
        

        doctor_exists="select count(*) from doctor where district='"+str(district)+"' and panchayath='"+str(panchayath)+"' and dname='"+str(dname)+"' and phone_no='"+str(dphnu)+"'"
        print("-------"+doctor_exists+"-------")
        c.execute(doctor_exists)
        exisist_data=c.fetchone()
        print(exisist_data)
        # try:
        if exisist_data[0]>0:
                message="Doctor already exisist"
                return render(request,"Add_Doctor.html",{"message":message})
        else:
                random_num=random.randrange(1000,10000,2)
                print("--------password---- "+str(random_num))
                password="doctor"+str(random_num)
                print(password)
                doctor_insert="insert into doctor(`district`,`panchayath`,`dname`,`qualification`,`address`,`phone_no`,`optime`)values('"+str(district)+"','"+str(panchayath)+"','"+str(dname)+"','"+str(dqual)+"','"+str(daddress)+"','"+str(dphnu)+"','"+str(dopt)+"')"
                doctor_login="insert into login(userid,username,password,status,usertype)values((select max(doctor_id) from doctor),'"+str(dphnu)+"','"+str(password)+"','1','doctor')"
                c.execute(doctor_insert)
                conn.commit()
                c.execute(doctor_login)
                conn.commit()
                msg="Congratulations!!! Government added you as doctor in the "+panchayath+" panchayath  Username :"+dphnu+" Password: "+password
                sendsms(dphnu,msg)
                message="Added Successfully"
                return render(request,"Add_Doctor.html",{"message":message})
        # except:
        #     message="Such details already exisist"
        #     return render(request,"Add_Doctor.html",{"message":message})

    return render(request,'Add_Doctor.html')

def viewdoctor(request):
    view_projects="select * from doctor"
    c.execute(view_projects)
    view_data=c.fetchall()
    return render(request,'viewdoctor.html',{"data":view_data})

def allviews(request):
    return render(request,'All_Views.html')

def view_vacc(request):
    view_vacc="SELECT v.vac_id,w.`worker_name`,w.`phone_no`,w.`panchayath`,w.`district`,v.`vac_name`,v.`details`,v.`time`,v.`posted_date`,v.`vaccination_date`,v.`location` FROM `worker_reg` w,`vaccination` v WHERE v.`wrkr_id`=w.`wrkr_id`"
    c.execute(view_vacc)
    view_data=c.fetchall()
    return render(request,'View_Vaccination.html',{"data":view_data})

def view_food(request):
    view_food="SELECT f.food_id,w.`worker_name`,w.`phone_no`,w.`panchayath`,w.`district`,f.`title`,f.`details`,f.`posted_date` FROM `worker_reg` w,`food` f WHERE f.`wrkr_id`=w.`wrkr_id`"
    c.execute(view_food)
    view_data=c.fetchall()
    return render(request,'View_food.html',{"data":view_data})

def view_disease(request):
    view_disease="SELECT d.disease_id,w.worker_name,w.panchayath,w.district,d.details,doc.dname,doc.qualification,doc.address,doc.phone_no,doc.optime FROM worker_reg w,disease d,doctor doc WHERE d.wrkr_id=w.wrkr_id AND doc.doctor_id=d.doc_id"
    c.execute(view_disease)
    view_data=c.fetchall()
    return render(request,'View_Disease.html',{"data":view_data})

def view_health(request):
    view_health="SELECT h.tipid,w.worker_name,w.panchayath,w.district,h.age_grp,h.tips,h.posted_date FROM worker_reg w,health_tips h WHERE h.wrkr_id=w.wrkr_id "
    c.execute(view_health)
    view_data=c.fetchall()
    return render(request,'View_Health.html',{"data":view_data})

def deletepanchayath(request):
    pid=request.GET.get("pid")
    del_pan="delete from panchayath_reg where panchayath_id='"+str(pid)+"'"
    c.execute(del_pan)
    return HttpResponseRedirect("/viewpanchayath")

def deleteworker(request):
    wid=request.GET.get("wid")
    del_wrkr="delete from worker_reg where wrkr_id='"+str(wid)+"'"
    del_login="delete from login where userid='"+str(wid)+"' and usertype='worker'"
    c.execute(del_wrkr)
    c.execute(del_login)
    return HttpResponseRedirect("/viewworker")

def deleteproject(request):
    pr_id=request.GET.get("pr_id")
    del_pr="delete from projects where project_id='"+str(pr_id)+"'"
    c.execute(del_pr)
    return HttpResponseRedirect("/viewprojects")

def deletedoctor(request):
    dr_id=request.GET.get("dr_id")
    del_dr="delete from doctor where doctor_id='"+str(dr_id)+"'"
    del_login="delete from login where userid='"+str(dr_id)+"' and usertype='doctor'"
    c.execute(del_login)
    c.execute(del_dr)
    return HttpResponseRedirect("/viewdoctor")