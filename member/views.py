from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import get_template
from django.template import Context
from .models import House_data,Tenant_data,Payments_data,Old_record,Old_payment
from django import forms
from datetime import date
from django.db.models import Q
import requests
# Create your views here.
Name=""
"""def WhatsApp_message(phone,message):
    phone_number = "+91"+phone
    kit.sendwhatmsg_instantly(phone_number, message)
    print("WhatsApp message sent!")"""        
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
        Name=request.POST['username']
        username = request.POST['username']
        
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            #messages.success(request, f' welcome {username} !!')
            return redirect('/home')
        else:
            return render(request, 'login.html',{'Alert':"Username or password sahi se toh dal"})
            #messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html')
@login_required(login_url="/")    
def home(request):
    x=House_data.objects.all().count()
    y=Tenant_data.objects.all().count()
    z=Payments_data.objects.all()
    today = date.today()
    print(today)
    p=str(today)
    #print(p[5:7])
    #print(p[0:4])
    #print(today[5:7])
    Date=""
    #print(today)
    Ans=0
    for i in z:
        Date=i.Payment_date
        gg=str(Date)
        a=gg[5:7]
        c=gg[0:4]
        Data=str(today)
        b=Data[5:7]
        d=Data[0:4]
        if a==b and c==d:
            #print(i.Date)
            Ans=Ans+i.Total_Amount            
    return render(request, 'home.html',{"Count":x,"Y":y,"Amount":Ans})
@login_required(login_url="/")    
def houses(request):
    #WhatsApp_message("8010114557","Hello World")
    x=House_data.objects.all()
    return render(request, 'houses.html',{'Data':x})
@login_required(login_url="/")    
def add_house(request):
    if request.method == 'POST':
        Name=request.POST['name']
        Address=request.POST['address']
        Owner=request.POST['owner']
        Owner_phone=request.POST['phone']
        code=request.POST['Int']
        x = House_data(house_name=Name, house_address=Address, house_owner=Owner, house_owner_phone=Owner_phone,house_code=code)
        x.save()
        phone=str(Owner_phone)
        return redirect('/houses/')
    else:
        return render(request, 'add_house.html')
@login_required(login_url="/")                   
def Tenant(request):
    if request.method == 'GET':

     x=Tenant_data.objects.all().order_by('Room_No')
     return render(request, 'tenent.html',{'Data':x})
    else:
        Num=request.POST.get('Num')
        x=Tenant_data.objects.filter(Q(Room_No=Num))
        return render(request, 'tenent.html',{'Data':x})
@login_required(login_url="/")    
def add_tenent(request):
    if request.method == 'GET':
      x=House_data.objects.all()
      return render(request, 'add_tenent.html',{'House':x})

    else:
        Room_No=request.POST.get('Room')
        Email=request.POST.get('email')
        Name=request.POST.get('name')
        D_O_B=request.POST.get('dob')
        Phone=request.POST.get('phone')
        House_name=request.POST.get('house')
        Photo=request.FILES.get('photo')
        Work_detail=request.POST.get('work')
        Total_members=request.POST.get('members')
        Members_Name=request.POST.get('members_name')
        Rent=request.POST.get('rent')
        Advanced=request.POST.get('advance')
        Checkin=request.POST.get('checkin')
        Meter=request.POST.get('meter')  
        Unit=request.POST.get('unit')
        Address=request.POST.get('address')
        y=Tenant_data(Name=Name,D_O_B=D_O_B,Bill_unit=Unit,Phone_No=Phone,Room_No=Room_No,Tenant_image=Photo,Members=Total_members,Members_Name=Members_Name,Rent=Rent,Advance=Advanced,Arrived_Month=Checkin,Work_Place=Work_detail,Meater_Reading=Meter,House_Name=House_data.objects.get(house_name=House_name),Address=Address,Email=Email)
        y.save()
        subject="Tenant Registration"
        body=f"Name-{Name}\nPhone No-{Phone}\nCheckin Date-{Checkin}\nStaying in-{House_name}\nRent Amount-{Rent}\nAdvance Amount-{Advanced}\nTotal Members-{Total_members}\nMembers Name/type-{Members_Name}\nMeater Reading Now-{Meter}\nElectricity Unit Price-Rs{Unit}\nYour Registration  is done successfully\n\nThank you\n{House_name}\n9027626452"
        body1=f"Tenant Registration\n\nName-{Name}\nPhone No-{Phone}\nCheckin Date-{Checkin}\nStaying in-{House_name}\nRent Amount-{Rent}\nAdvance Amount-{Advanced}\nTotal Members-{Total_members}\nMembers Name/type-{Members_Name}\nMeater Reading Now-{Meter}\nElectricity Unit Price-Rs{Unit}\nYour Registration  is done successfully\n\nThank you\n{House_name}\n9027626452"    
        return redirect('/tenant/')
@login_required(login_url="/")        
def Tenant_details(request ,Id):
    x=Tenant_data.objects.get(id=Id)
    #print(x)
    return render(request, 'tenent_data.html',{'Data':x})
@login_required(login_url="/")    
def Tenant_payment(request,Id,name):
    if request.method == 'GET':
     x=Tenant_data.objects.get(id=Id)
     y=Payments_data.objects.filter(Tenant_Name=Tenant_data.objects.get(Name=name))
     print(x.Arrived_Month)
     today = date.today()
     print(today)
     p=str(today)
     print(p[5:7])
     today_month = int(p[5:7])
     print("Current-Month",today_month)
     p1=str(x.Arrived_Month)
     prev_month = int(p1[5:7])
     print("Prev-Month",prev_month)
     prev_year=int(p1[0:4])
     print("Prev-Year",prev_year)
     curr_year=int(p[0:4])
     print("Curr-Year",curr_year)
     curr_date=int(p[8:11])
     print("Curr-Date",curr_date)
     prev_date=int(p1[8:11])
     print("Prev-Date",prev_date)
     month_diff=today_month-prev_month
     year_diff=curr_year-prev_year
     Total_month=month_diff+year_diff*12
     if prev_date>curr_date:
        Total_month=Total_month-1
     print("Total month",Total_month)
     Rent=int(x.Rent)
     print("Rent",Rent)
     Rent_Amount=Rent*Total_month
     print("Rent_Amount",Rent_Amount)
     #print(y)
     data=0
     bill=0
     last_bill=0
     last_total=0
     last_rent=0
     Water=0
     for i in y:
         data=data+i.Rent_Amount
         bill=bill+i.Total_Bill+i.Water_Bill
         last_bill=i.Total_Bill
         Water=i.Water_Bill
         last_total=i.Total_Amount
         last_rent=i.Rent_Amount
        #print(i.Rent_Amount)
    #print(last_bill)    
    #print(bill)
     print(data)
     Balance=Rent_Amount-data
     print("Balance",Balance)
    #print(last_total)
    #print(last_rent)
     #y=Payments_data.objects.filter(Tenant_Name=Tenant_data.objects.get(Name=name)).order_by('-id')
     return render(request, 'tenant_payment.html',{'Data':x,'Payments':y,'Rent':data,'Bill':bill,'last_bill':last_bill,'last_total':last_total,'last_rent':last_rent,'Balance':Balance,"total_month":Total_month,"Water":Water})
    else:
        Name=request.POST.get('name')
        y=Tenant_data.objects.get(Name=Name)
        House=request.POST.get('house')
        Rent=request.POST.get('rent')
        Date=request.POST.get('date')
        Payment_date=request.POST.get('date1')
        Mode=request.POST.get('mode')
        Image=request.FILES.get('img')
        unit1=request.POST.get('unit1')
        unit2=request.POST.get('unit2')
        Bill_total=request.POST.get('bill')
        unit=request.POST.get('rate')
        water=request.POST.get('water')
        final=request.POST.get('total')
        Dat=request.POST.get('Hello')
        phone=str(y.Phone_No)
        #print(phone)
        Hh=int(Dat)
        good='/tenant_payment/'+str(Id)+'/'+name+'/'
        z=Tenant_data.objects.get(id=Id)
        body2=f"Payment Due\n\nRoom No-{z.Room_No} \nName-{Name}\nRent Month/date-{Date}\nRent Amount-{Rent}\nCurr Unit-{unit2}\nPrev Unit-{unit1}\nElectricity Bill-{Bill_total}\nWater Bill-{water}\nTotal Amount Due-{final}\n\nThankyou\n{House}\nMob-9027626452"
        if Hh==2:
            #WhatsApp_message(phone,body2)
            return redirect(good)
        y.Meater_Reading=unit2
        y.save()
        reciever=str(z.Email)
        x=Payments_data(Tenant_Name=Tenant_data.objects.get(Name=Name),House_Name=House_data.objects.get(house_name=House),Rent_Amount=Rent,Date=Date,Mode=Mode,Payment_Screenshot=Image,Previous_Electricity_Unit=unit1,Current_Electricity_Unit=unit2,Total_Bill=Bill_total,Unit_Price=unit,Water_Bill=water,Total_Amount=final,Payment_date=Payment_date)
        x.save()
        subject="Payment Details"
        body=f"Room No-{z.Room_No} \nName-{Name}\nRent Month/date-{Date}\nMode-{Mode}\nElectricity Bill-{Bill_total}\nWater Bill-{water}\nTotal Amount Paid-{final}\nPayment date-{date.today()}\n\nThankyou\n{House}\nMob-9027626452"
        body1=f"Payment Done Successfully\n\nPayment Details\n\nRoom No-{z.Room_No} \nName-{Name}\nRent Month/date-{Date}\nRent Amount-{Rent}\nMode-{Mode}\nElectricity Bill-{Bill_total}\nWater Bill-{water}\nTotal Amount Paid-{final}\nPayment date-{date.today()}\n\nThankyou\n{House}\nMob-9027626452"
        """if y.Phone_No is not None:
             WhatsApp_message(phone,body1)"""
        return redirect(good)
@login_required(login_url="/")         
def Payment_page(request):
    if request.method =='GET':
     y=House_data.objects.all()   
     Date=date.today()
     print(Date)
     Date=str(Date)
     print(Date[5:7])
     yy=Date[0:4]
     mm=Date[5:7]
     dd=Date[8:11]
     Date1=yy+"-"+mm
     #print(tt,tt1)
     x=Payments_data.objects.filter(Payment_date__year=yy,Payment_date__month=mm).order_by('-id')
     total=0
     Good="All"
     for i in x:
         total=total+i.Total_Amount
     return render(request, 'payment_page.html',{'Data':x,'Date1':Date1, 'TotalAmount':total,'house':y,'good':Good})
    else:
     d1=request.POST.get('hello')
     Year=request.POST.get('Year')
     Month=request.POST.get('Month')
     print(Year,Month)
     ddddd=str(d1)
     #print(d1)   
     y=House_data.objects.all()   
     Date=date.today()
     print(Date)
     Date=str(Date)
     print(Date[5:7])
     yy=Date[0:4]
     mm=Date[5:7]
     dd=Date[8:11]
     Date1=yy+"-"+mm
     #print(tt,tt1)
     if Month:
         mm=Month
         Date1=yy+"-"+str(Month)
     if Year:
        yy=Year
        Date1=str(Year)+"-"+mm    
     x=Payments_data.objects.filter(Payment_date__year=yy,Payment_date__month=mm).order_by('-id')
     if Year and Month :
         x=Payments_data.objects.filter(Payment_date__year=Year,Payment_date__month=Month).order_by('-id')
         Date1=str(Year)+"-"+str(Month)
     z=x
     if ddddd!="All":
         z=x.filter(House_Name=House_data.objects.get(house_name=d1))
         print(z)     
     total=0
     for i in z:
         total=total+i.Total_Amount
     return render(request, 'payment_page.html',{'Data':z,'Date1':Date1, 'TotalAmount':total,'house':y,'good':ddddd})

@login_required(login_url="/")    
def add_payment(request):
   if request.method == 'GET':
    x=Tenant_data.objects.all()
    y=House_data.objects.all()
    #print(x)
    return render(request, 'add_payment.html',{'Tenant':x, 'House':y})
   else:
     Name=request.POST.get('name')
     House=request.POST.get('house')
     Rent=request.POST.get('rent')
     Date=request.POST.get('date')
     Payment_date=request.POST.get('date1')
     Mode=request.POST.get('mode')
     Image=request.FILES.get('img')
     unit1=request.POST.get('unit1')
     unit2=request.POST.get('unit2')
     Bill_total=request.POST.get('bill')
     unit=request.POST.get('rate')
     water=request.POST.get('water')
     final=request.POST.get('total')
     x=Payments_data(Tenant_Name=Tenant_data.objects.get(Name=Name),House_Name=House_data.objects.get(house_name=House),Rent_Amount=Rent,Date=Date,Mode=Mode,Payment_Screenshot=Image,Previous_Electricity_Unit=unit1,Current_Electricity_Unit=unit2,Total_Bill=Bill_total,Unit_Price=unit,Water_Bill=water,Total_Amount=final,Payment_date=Payment_date)
     x.save()
     return redirect('/payment_page/')

@login_required(login_url="/")        
def house_tenant(request,Id):
    if request.method =='GET':

     x=Tenant_data.objects.filter(House_Name=House_data.objects.get(house_name=Id)).order_by('Room_No')
     y=x.count()
     print("Count",y)
     return render(request, 'house_tenant.html',{'Data': x,'house':Id,'Count':y})
    else:
        Num=request.POST.get('Num')
        y=Tenant_data.objects.filter(House_Name=House_data.objects.get(house_name=Id))
        z=y.filter(Q(Room_No=Num))
        #print(z)
        x=Tenant_data.objects.filter(House_Name=House_data.objects.get(house_name=Id))
        return render(request, 'house_tenant.html',{'Data': z,'house':Id,'Count':x.count()})

@login_required(login_url="/")    
def checkout(request,Id,name):
    if request.method == 'GET':
     x=Tenant_data.objects.get(id=Id)
     y=Payments_data.objects.filter(Tenant_Name=Tenant_data.objects.get(Name=name))
     #print(y)
     data=0
     bill=0
     last_bill=0
     last_total=0
     last_rent=0
     for i in y:
         data=data+i.Rent_Amount
         bill=bill+i.Total_Bill+i.Water_Bill
         last_bill=i.Total_Bill+i.Water_Bill
         last_total=i.Total_Amount
         last_rent=i.Rent_Amount
        #print(i.Rent_Amount)
    #print(last_bill)    
    #print(bill)
    #print(data)
    #print(last_total)
    #print(last_rent)
     good='/tenant_payment/'+str(Id)+'/'+name+'/'
     print(good)
     return render(request, 'checkout.html',{'Data':x,'Payments':y,'Rent':data,'Bill':bill,'last_bill':last_bill,'last_total':last_total,'last_rent':last_rent,'good':good})
    else:
        x=Tenant_data.objects.get(id=Id)
        print(x.Name,x.House_Name,x.D_O_B,x.Email,x.Phone_No,x.Room_No,x.Arrived_Month)
        y=Old_record(Tenant_Name=x.Name,House_Name=x.House_Name,D_O_B=x.D_O_B,Address=x.Address,Email=x.Email,Checkin_Date=x.Arrived_Month,Date=date.today(),Phone_No=x.Phone_No,Tenant_image=x.Tenant_image,Rent=x.Rent,Documents_Upload=x.Documents_Upload,Room_No=x.Room_No)
        y.save()
        z=Payments_data.objects.filter(Tenant_Name=Tenant_data.objects.get(Name=x.Name))
        print(z)
        for i in z:
            p=Old_payment(
            Tenant_Name=Old_record.objects.get(Tenant_Name=i.Tenant_Name),
            House_Name=i.House_Name,
            Rent_Amount=i.Rent_Amount,
            Date=i.Date,
            Mode=i.Mode,
            Payment_Screenshot=i.Payment_Screenshot,
            Previous_Electricity_Unit=i.Previous_Electricity_Unit,
            Current_Electricity_Unit=i.Current_Electricity_Unit,
            Total_Bill=i.Total_Bill,
            Unit_Price=i.Unit_Price,
            Water_Bill=i.Water_Bill,
            Total_Amount=i.Total_Amount)
            p.save()
        x.delete()
        return redirect('/tenant/')
@login_required(login_url="/")
def old_records(request):
    x=Old_record.objects.all().order_by('Room_No')
    return render(request,'old_record.html',{'Data':x})
@login_required(login_url="/")    
def old_record_data(request,Id):
    x=Old_record.objects.get(id=Id)
    return render(request,'oldrecord_details.html',{'Data':x})
@login_required(login_url="/")    
def old_payment(request,Id):
    x=Old_record.objects.get(id=Id)
    y=Old_payment.objects.filter(Tenant_Name=Old_record.objects.get(Tenant_Name=x.Tenant_Name))
    print(y)
    data=0
    bill=0
    last_bill=0
    last_total=0
    last_rent=0
    for i in y:
        data=data+i.Rent_Amount
        bill=bill+i.Total_Bill+i.Water_Bill
        last_bill=i.Total_Bill+i.Water_Bill
        last_total=i.Total_Amount
        last_rent=i.Rent_Amount
    return render(request,'old_payments.html',{'Data':x,'Payments':y,'Rent':data,'Bill':bill,'last_bill':last_bill,'last_total':last_total,'last_rent':last_rent})
def Dues(request):
    x=Tenant_data.objects.all().order_by('Room_No')
    print("Count->",x.count())
    for x in x:
         print(x.Name,x.House_Name,x.D_O_B,x.Email,x.Phone_No,x.Room_No,x.Arrived_Month)
         print('\n')
         y=Payments_data.objects.filter(Tenant_Name=Tenant_data.objects.get(Name=x.Name))
         #print(y)
         print(x.Arrived_Month)
         today = date.today()
         print(today)
         p=str(today)
         print(p[5:7])
         today_month = int(p[5:7])
         print("Current-Month",today_month)
         p1=str(x.Arrived_Month)
         prev_month = int(p1[5:7])
         print("Prev-Month",prev_month)
         prev_year=int(p1[0:4])
         print("Prev-Year",prev_year)
         curr_year=int(p[0:4])
         print("Curr-Year",curr_year)
         curr_date=int(p[8:11])
         print("Curr-Date",curr_date)
         prev_date=int(p1[8:11])
         print("Prev-Date",prev_date)
         month_diff=today_month-prev_month
         year_diff=curr_year-prev_year
         Total_month=month_diff+year_diff*12
         if prev_date>curr_date:
             Total_month=Total_month-1
         print("Total month",Total_month)
         Rent=int(x.Rent)
         print("Rent",Rent)
         Rent_Amount=Rent*Total_month
         print("Rent_Amount",Rent_Amount)
         data=0
         bill=0
         last_bill=0
         last_total=0
         last_rent=0
         for i in y:
             data=data+i.Rent_Amount
             bill=bill+i.Total_Bill+i.Water_Bill
             last_bill=i.Total_Bill+i.Water_Bill
             last_total=i.Total_Amount
             last_rent=i.Rent_Amount
         print("Paid Total->",data)
         print(bill)
         print(last_bill)
         print(last_total)
         print(last_rent)
         x.Balance=Rent_Amount-data
         print("Balance->",x.Balance)
         x.save()
    x=Tenant_data.objects.filter(Balance__gte=3000).order_by('Room_No')     
    return render(request,'dues.html',{'Data':x})