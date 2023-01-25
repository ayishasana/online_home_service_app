from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from onlinehomeservice_app.forms import Login_form, register_form, register_form1, FeedbackForm, ScheduleForm, \
    work_form, AddBill, creditcardform
from onlinehomeservice_app.models import register, Login, register1, complaints, Schedule_add, work, Take_appointment, \
    Bill, CreditCard


# Create your views here.


def index(request):
    return render(request,"index.html")

def index1(request):
    return render(request,"index1.html")



def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            if user.is_staff :
                return redirect("base")
            if user.is_customer :
                return redirect("customerbase")
            if user.is_worker :
                return redirect("workerbase")
        else :
            messages.info(request,"Invalid credentials")

    return render(request,"login.html")




#################admin################

def adminbase(request):
    return render(request,"admin/admin base.html")


def feedbacks(request):
    n = complaints.objects.all()
    return render(request,"admin/feedbacks.html",{"feedbacks":n})

#this is for admin to view feedback data


def reply_feedback(request,id):
    feedback = complaints.objects.get(id=id)
    if request.method == 'POST' :
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request,'Reply send for complaints')
        return redirect('feedbacks')
    return render(request,'admin/reply_feedback.html',{'feedback' : feedback})

#this is the reply given by admin to customer



def view_schedule(request):
    data = Schedule_add.objects.all()
    print(data)
    return render(request,"admin/view_schedule.html",{"data":data})

#this is for admin to view schedules of workers


def work_add(request):
    form = work_form()
    if request.method =='POST':
        form = work_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work_view")
    return render(request,'admin/work_add.html',{'form':form})


#this is for admin to add different types of work ..so it will come in the dropdown menu in worker registration form so they can select it

def work_view(request):
    data = work.objects.all()
    return render(request,'admin/work_view.html',{'data':data})

#this is for admin to view different types of work he added and its amount.


def delete_work_view(request,id):
    wm = work.objects.get(id=id)
    wm.delete()
    return redirect("work_view")

#this is to delete work


def update_work_view(request,id):
    a = work.objects.get(id=id)
    form = work_form(instance=a)
    if request.method == 'POST':
        form = work_form(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('work_view')

    return render(request,'admin/update_work_view.html',{'form':form})

#this is to update work



def admin_view_appointment(request):
    a = Take_appointment.objects.all
    return render(request,"admin/admin_view_appointment.html",{"app":a})

#this is for admin to see the appointment status of workers


def approve_appointment(request,id):
    n = Take_appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request,'Appointment Confirmed')
    return redirect('admin_view_appointment')

#this is for admin to approve appointment


def reject_appointment(request,id):
    n = Take_appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request,'Appointment Rejected')
    return redirect('admin_view_appointment')

#this is for admin to reject appointment




def bill(request):
    form = AddBill()
    if request.method == 'POST' :
        form = AddBill(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bill')
    return render(request,'admin/generate_bill.html',{'form':form})

#this is for admin to generate bill for customers


def view_bill(request):
    bill = Bill.objects.all()
    print(bill)
    return render(request, 'admin/view_payment_details.html',{'bill':bill})



#admin to view the payment details of customers


def customers_data(request):
    data=register1.objects.all
    print(data)
    return render(request,"admin/customers_data.html",{"data": data})

#this is for admin to see the customers data


def delete_it(request,id):
 wm=register1.objects.get(id=id)
 wm.delete()
 return redirect("customers_data")

#this is to delete the customers data


def workers_data(request):
    data=register.objects.all
    print(data)
    return render(request,"admin/workers_data.html",{"data": data})

#this is for admin to see the workers data



def delete(request,id):
 wm=register.objects.get(id=id)
 wm.delete()
 return redirect("workers_data")

#this is to delete workers data



def update(request,id):
    a = register.objects.get(id=id)
    form = register_form(instance=a)
    if request.method == 'POST':
        form = register_form(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('workers_data')

    return render(request,'admin/update.html',{'form':form})

#this is to update workers data































#########################customer###########################################################


def customers(request):
    return render(request,"customer/customers.html")


def customerbase(request):
    return render(request,"customer/customerbase.html")

#this is the dashboard of customers


def customer_registration(request):
    form1=Login_form()
    form2=register_form1()
    if request.method == "POST":
        form1 = Login_form(request.POST)
        form2 = register_form1(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
               a = form1.save(commit=False)
               a.is_customer = True
               a.save()
               user1 = form2.save(commit=False)
               user1.user = a
               user1.save()
               return redirect('loginpage')

    return render(request,"customer/customers.html",{'form1': form1, 'form2': form2})


#this is for customer registration


def feedback(request):
    form = FeedbackForm()
    u = request.user
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect("view")

    return render(request,"customer/feedback.html",{"form":form})

#this is the feedback form for customers to write their feedbacks

def view(request):
    data = complaints.objects.filter(user=request.user)
    print(data)
    return render(request, "customer/view.html",{"data":data})

#this is to view the reply given by admin for the feedbacks of customer



def deletefeedback(request,id):
    wm=complaints.objects.get(id=id)
    wm.delete()
    return redirect ("view")
 #this is to delete the feedback

def delete_schedule(request,id):
    wm = Schedule_add.objects.get(id=id)
    wm.delete()
    return redirect("view_schedule")

#this is to delete schedule

def customer_view_schedule(request):
    data = Schedule_add.objects.all()
    print(data)
    return render(request,"customer/customer_view_schedule.html",{"data":data})

#this is to view the schedule given by worker

def customer_view_worker(request):
    data=register.objects.all
    print(data)
    return render(request,"customer/customer_view_worker.html",{"data": data})

#this is for customers to view the workers


def take_appointment(request,id):
    s = Schedule_add.objects.get(id=id)
    c = register1.objects.get(user=request.user)
    app = Take_appointment.objects.filter(user=c,schedule=s)
    if app.exists():
        messages.info(request,"Already booked")
        return redirect("customer_view_schedule")
    else:
        if request.method == 'POST':
            obj = Take_appointment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request,"Appointment is successfully booked")
            return redirect("view_appointment")
    return render(request,"customer/take_appointment.html",{"s":s})

#this is for customers to book appointment of workers


def view_appointment(request):
    # c = register1.objects.get(user = request.user)
    a = Take_appointment.objects.all
    return render(request,"customer/view_appointment.html",{"app":a})


#this is for customer to see the appointment status of the worker



def customer_view_payment(request):
    u = register1.objects.get(user=request.user)
    a = Bill.objects.filter(name=u)
    return render(request, 'customer/customer_view_payment.html',{'a':a})

#this is for customer to view the payment details




def creditcard_pay_cus(request):
    form = creditcardform()
    if request.method == 'POST':
        form = creditcardform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_creditcard_details')
    return render(request,"customer/creditcard_add.html",{'form':form})

#this is for creditcard payment for customers

def view_creditcard_details(request):
    a = CreditCard.objects.all()
    print(a)
    return render(request,'customer/view_creditcard_details.html',{'a':a})

#this is to view the credit card details

def pay_bill(request,id):
    bi = Bill.objects.get(id=id)
    form = AddBill()
    if request.method == 'POST':
        card = request.POST.get('card')
        c = request.POST.get('cvv')
        da = request.POST.get('exp')
        CreditCard(card_no=card,card_cvv=c,expiry_date=da).save
        bi.status = 1
        bi.save()
        messages.info(request,'Bill paid Successfully')
        return redirect('view_bill')
    return render(request,'customer/pay_bill.html',)

#this is for customer to pay the bill


def pay_in_direct(request,id):
    bi = Bill.objects.get(id=id)
    bi.status = 2
    bi.save()
    messages.info(request, 'choosed to Pay Fee Direct in office')
    return redirect('bill_history')

#this is for customer to pay in direct

def bill_history(request):
    u = register1.objects.get(user=request.user)
    bill =Bill.objects.filter(name=u,status__in=[1,2])

    return render(request,'customer/customer_view_bill_history.html',{'bill':bill })

#this is for customer to see the bill history only if he/she is paid












##################worker###########################

def workers(request):
    return render(request,"worker/workers.html")

def workerbase(request):
    return render(request,"worker/workerbase.html")

#this is the dashboard of workers


def worker_registration(request):
    form1=Login_form()
    form2=register_form()
    if request.method == "POST":
        form1 = Login_form(request.POST)
        form2 = register_form(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
               a = form1.save(commit=False)
               a.is_worker = True
               a.save()
               user1 = form2.save(commit=False)
               user1.user = a
               user1.save()
               return redirect('loginpage')

    return render(request,"worker/workers.html",{'form1': form1, 'form2': form2})

#this is for worker registration









def Schedule(request):
        form = ScheduleForm()
        # u = request.user
        if request.method == "POST":
            form = ScheduleForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.worker=register.objects.get(user=request.user)
                obj.save()
                return redirect("view_schedule")

        return render(request, "worker/Schedule.html", {"form": form})



def worker_view_schedule(request):
    data = Schedule_add.objects.all()
    print(data)
    return render(request,"worker/worker_view_schedule.html",{"data":data})


def worker_view_appointment(request):
    a = Take_appointment.objects.filter(status=1)

    return render(request,"worker/worker_view_appointment.html",{"app":a})

def worker_update(request,id):
    a = register.objects.get(id=id)
    form = register_form(instance=a)
    if request.method == 'POST':
        form = register_form(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('workers_data')

    return render(request,'worker/worker_view_workerdata.html',{'form':form})












