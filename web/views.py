from django.shortcuts import render,redirect

from web.forms import StudentForm, ContactForm

from web.models import Student

from django.core.mail import send_mail

from django.conf import settings
import random

# Create your views here.
def index(request):
    students = Student.objects.all() 
    context = {
        'students': students
    }
    return render(request, "index.html", context=context)


def second(request):
    if request.method == "POST":
        data = request.POST
        form = StudentForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = random.randint(000000,999999)
            subject = 'Your Registration Was Successful!'
            message = f"""
            Dear {data['name']},

            Congratulations! You have successfully registered on our platform. Below are your login details:

            Password: {password}

            Please keep this information secure and do not share it with anyone. Thank you for joining us!

            If you have any questions or need assistance, feel free to contact our support team.

            Best regards,  
            Your Team
            """

            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect("/")
        else:
            return render(request, "second.html", {"form": form})
    else:
        form = StudentForm()

    context = {
        'form': form,
    }
    return render(request, "second.html", context=context)


def updateS(request,id):
    student=Student.objects.get(id=id)
    form=StudentForm(instance=student)
    context={
        'form':form,
        'id':id,
    }

    return render(request,"UpdateS.html",context=context)

def hsUp(request,id):
    student=Student.objects.get(id=id)
    if request.method == "POST":
        formdata =StudentForm(instance=student,data=request.POST,files=request.FILES)
        if formdata:
            formdata.save()
        else:
            print("error2")
        return redirect("/")
    else:
        print("error")


def hdel(request,id):
    student=Student.objects.get(id=id)
    if student:
        student.delete()
    else:
        print("error")
    return redirect("/")
    

def detail(request,id):
    student=Student.objects.get(id=id)
    context={
        'student':student
    }

    return render(request,"Details.html",context=context)

def contact(request):
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request,"Contact.html",context=context)

def hContact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)  
        if form.is_valid():
            name = form.cleaned_data.get('FullName')
            email = form.cleaned_data.get('Email')
            subject = 'Report Issue!'
            message = f"""

            Dear Support Team,

            I am writing to report an issue. Below are the details:

            Name: {name}
            Issue Description: {form.cleaned_data.get('Description')}

            Thank you for your assistance.

            Best regards,
            {name}
            """
            from_email = email
            recipient_list = [settings.DEFAULT_FROM_EMAIL]
            send_mail(subject, message, from_email, recipient_list)
            return redirect("/")
        else:
            return render(request, "Contact.html", {"form": form})
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, "Contact.html", context=context)
