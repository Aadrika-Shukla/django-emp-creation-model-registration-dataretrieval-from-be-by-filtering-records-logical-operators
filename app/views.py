from django.shortcuts import render
from django.http import HttpResponse


from app.models import *

# Create your views here.
#function to take  dept table data from database and then revert it back from backend and display that data in  form of table in frontend 
# FOR WORKING OF ONE VIEW CAN RENDER MULTIPLE HTML PAGES WE SHOULD NOT COMMENT THIS DEFINING OF DISPLAY METHOS FOR ALL PAGES
def display_dept(request):
    QLDO=Dept.objects.all()  #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    d={'QLDO':QLDO}              #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_dept.html',context=d)
    

#function to take  emp table data from database and then revert it back from backend and display that data in  form of table in frontend 

    

def display_emp(request):
    QLEO=Emp.objects.all()   #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    d={'QLEO':QLEO}              #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_emp.html',context=d)
    

#function to take  salgrade table data from database and then revert it back from backend and display that data in  form of table in frontend 

    


def display_salgrade(request):
    QLSO=Salgrade.objects.all()   #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    d={'QLSO':QLSO}                    #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_salgrade.html',context=d)







#INSTEAD OF RETURNING HTTP RESPONSE WE WILL DIRECTLY RETURN HTML PAGE AS MY RESPONSE ,HENCE ONE HTML PAGE CAN BE RENDERED BY MULTIPLE VIEWS



####one html page renedered by multliple views####



#getting the object by get() and filter() from our parent if it is their in our parent table 


def insert_dept(request):
    dno=input('enter dept number')
    dn=input('enter dept name')
    dl=input('enter dept location')
    DO=Dept.objects.get_or_create(deptno=dno,dname=dn,dloc=dl)[0]
    DO.save()
    QLDO=Dept.objects.all()  #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    d={'QLDO':QLDO}              #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_topics.html',context=d)



####one html page renedered by multliple views####


#getting the object by get() and filter() from our parent if it is their in our parent table 


def insert_emp(request):
    dno=int(input('enter dept number'))#foreign key
    DO=Dept.objects.filter(deptno=dno)
    if DO:
       eno=input('enter employee number/id')
       ena=input('enter employee name')
       ej=input('enter employee job')
       emgr=input('enter employee reporting manager number')
       if emgr:
           meo=Emp.objects.get(eno=int(emgr))
       else:
           emgr=None
       ehd=input('enter employee hiredate')
       esal=int(input('enter employee salary'))
       ecomm=input('enter employee commission')
       if ecomm:
           ecomm=int(ecomm)
       else:
           ecomm
       EO=Emp.objects.get_or_create(deptno=DO,empno=eno,ename=ena,job=ej,mgr=meo,hiredate=ehd,sal=esal,comm=ecomm)[0]
       EO.save()
       QLEO=Emp.objects.all()   #to take/get all the data from database where all() will return result in form of queryset of list of all objects
       d={'QLEO':Emp.objects.all()}              #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute WE CAN DIRECTLY GIVE IT LIKE THIS INSTEAD OF STORING IT TO VARIBALE QLWO USE THIS   d={'QLWO':WebPage.objects.all()} OR  d={'QLWO':QLWO}
       return render(request,'display_emp.html',context=d)
    
    else:
        return HttpResponse('above given topic name is not available ,kindly give another topic name')
    


####one html page renedered by multliple views####


#getting the object by get() and filter() from our parent if it is their in our parent table 

def insert_salgrade(request):
   
    g=input('enter grade')
    lo=input('enter losal')
    hi=input('enter hisal')
    SO=Dept.objects.get_or_create(grade=g,losal=lo,hisal=hi)[0]
    SO.save()
    QLSO=Salgrade.objects.all()  #to take/get all the data from database where all() will return result in form of queryset of list of all objects
    d={'QLSO':QLSO}              #to send data from backend to frontend we use to send that data in form of dictionary which will be passed as an argument to context attribute
    return render(request,'display_salgrade.html',context=d)

   




