from django.shortcuts import render,redirect
from students.models import Student,Teachers,Notification
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

student_register = []

# Create your views here.
def register(request):
    print(request.method,'Firsttask')
    if request.method=="POST":
        print(request.POST)
        student_name=request.POST.get('student_name')
        father_name = request.POST.get('father_name')
        email=request.POST.get('email')
        mobile_number=request.POST.get('mobile_number')
        dob=request.POST.get('dob')
        class_student=request.POST.get('class_student')
        roll_number=request.POST.get('roll_number')
        gender=request.POST.get('gender')
        if Student.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("register_url")
        s=Student()
        s.student_name=student_name
        s.father_name=father_name
        s.email=email
        s.mobile_number=mobile_number
        s.dob=dob
        s.class_student=class_student
        s.roll_number=roll_number
        s.gender=gender
        s.save()
        messages.success(request, "Student registered successfully!")
        return redirect("register_url")
            

        # return redirect('table_url')
    return render(request,'student_app/student_register.html')

@login_required(login_url='login')
def table(request):
    student_register=Student.objects.all()
    search = request.GET.get('search')

    if search:
        student_register = Student.objects.filter(
    Q(student_name__icontains=search) |
    Q(email__icontains=search) |
    Q(mobile_number__icontains=search))
    context={
        'student':student_register,
    }
    print(student_register,'students')
    return render(request,'student_app/table.html',context)


def update_statudent_view(request, sid):
    print("student id:", sid)
    interested_student  = Student.objects.get(id=sid)
    print("Gender:",interested_student.gender)
    print("DOB:",interested_student.dob)
    print(interested_student)
    if request.method=="POST":
        interested_student.student_name=request.POST.get("student_name")
        interested_student.father_name=request.POST.get("father_name")
        interested_student.mobile_number=request.POST.get("mobile_number")
        interested_student.email=request.POST.get("email")
        birth_date = request.POST.get("dob")
        interested_student.dob = datetime.strptime(birth_date, "%d-%m-%Y").date()
        interested_student.gender=request.POST.get("gender")
        interested_student.class_student=request.POST.get('class_student')
        interested_student.roll_number=request.POST.get('roll_number')
        interested_student.save()

        return redirect('table_url')
    context = {"student": interested_student}
    return  render(request, 'student_app/update_student.html', context)

def delete(request,sid):
    del_student=Student.objects.get(id=sid)
    del_student.delete()
    return redirect('table_url')

def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect("login")

    return render(request,"student_app/login.html")        


@login_required(login_url='login')
def dashboard(request):
    total_students = Student.objects.count()
    recent_students = Student.objects.order_by("-id")[:5]
    # notification_count=

    context = {
        "total_students": total_students,
        "recent_students": recent_students,


    }
    return render(request,"student_app/Dashboard.html",context)

def logout_view(request):
    logout(request)
    return redirect("login")    

def Teacher(request):
    teacher=Teachers.objects.all()
    context={
        'teacher':teacher
    }
    return render(request,"student_app/teachers.html",context)

def add_teachers(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile_number=request.POST.get('mobile_number')
        subjects=request.POST.get('subjects')
        Assigned_class=request.POST.get('Assigned_class')
        password=request.POST.get('password')
        s=Teachers()
        s.name=name
        s.email=email
        s.mobile_number=mobile_number
        s.subjects=subjects
        s.Assigned_class=Assigned_class
        s.password=password
        s.save()
        print(request.POST)
        return redirect('add_teachers')

    return render(request,"student_app/add_teacher.html")

def edit_teacher(request,tid):
    t=Teachers.objects.get(id=tid)
    print(t)
    if request.method=="POST":
        t.name=request.POST.get('name')
        t.email=request.POST.get('email')
        t.mobile_number=request.POST.get('mobile_number')
        t.subjects=request.POST.get('subjects')
        t.Assigned_class=request.POST.get('Assigned_class')
        t.save()
        return redirect('teachers')

    return render(request,"student_app/edit_teachers.html",{'t':t})

def delete_teacher(request,tid):
    t=Teachers.objects.get(id=tid)
    t.delete()
    return redirect('teachers')

# Notification
def notification(request):
    if request.method =='POST':
        send_to=request.POST.get('send_to')
        title=request.POST.get('title')
        message=request.POST.get('message')
        message_type=request.POST.get('message_type')
        date_str=request.POST.get('sceduled_date')
        if date_str:
            sceduled_date=datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            sceduled_date=None    
        attached_file=request.POST.get('attached_file')
        Notification.objects.create(
            send_to=send_to,
            title=title,
            message=message,
            message_type=message_type,
            sceduled_date=sceduled_date,
            attached_file=attached_file
        )
        return redirect('notification')

    return render(request,"student_app/notifications.html")

def attendance(request):
    selected_date=request.GET.get('selected_date')
    selected_class=request.GET.get('selected_class')
    selected_section=request.GET.get('selected_section')
    return render(request,'student_app/attendance.html')