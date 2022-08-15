from django.contrib.auth import logout, authenticate, login
from django.db.models import Max, Q
from django.shortcuts import render, redirect
from .models import *
from datetime import date


# Create your views here.

def index(request):
    pnotice = Publicnotice.objects.all()
    return render(request, 'index.html', locals())


def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    totalclass = Class.objects.all().count()
    totalstudent = Student.objects.all().count()
    totalnotice = Notice.objects.all().count()
    totalpnotice = Publicnotice.objects.all().count()

    return render(request, 'admin_home.html', locals())


def add_Class(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == "POST":
        className = request.POST['ClassName']
        section = request.POST['Section']

        try:
            Class.objects.create(ClassName=className, Section=section)
            error = "no"
        except:
            error = "yes"

    return render(request, 'add_Class.html', locals())


def manage_Class(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    classs = Class.objects.all()
    return render(request, 'manage_Class.html', locals())


def editClass(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    classs = Class.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        className = request.POST['ClassName']
        section = request.POST['Section']

        classs.ClassName = className
        classs.Section = section

        try:
            classs.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editClass.html', locals())


def deleteClass(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    classs = Class.objects.get(id=pid)
    classs.delete()
    return redirect('manage_Class')


def add_Student(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    clss = Class.objects.all()

    stdid = 101 if Student.objects.count() == 0 else Student.objects.aggregate(max=Max('StuID'))["max"] + 1
    error = ""
    if request.method == "POST":
        clsid = request.POST['classs']
        classid = Class.objects.get(id=clsid)

        fname = request.POST['fullName']
        e = request.POST['emailid']
        gender = request.POST['Gender']
        dob = request.POST['DOB']
        image = request.FILES['Image']
        pwd = request.POST['Password']
        fatherName = request.POST['FatherName']
        motherName = request.POST['MotherName']
        contactNumber = request.POST['ContactNumber']
        altenateNumber = request.POST['AltenateNumber']
        address = request.POST['Address']

        try:
            user = User.objects.create_user(username=e, password=pwd, first_name=fname)
            Student.objects.create(user=user, classs=classid, StuID=stdid, Gender=gender, DOB=dob, Image=image,
                                   FatherName=fatherName, MotherName=motherName, ContactNumber=contactNumber,
                                   AltenateNumber=altenateNumber, Address=address, DateofAdmission=date.today())
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_Student.html', locals())


def manage_Student(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = Student.objects.all()
    return render(request, 'manage_Student.html', locals())


def editStudent(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    clss = Class.objects.all()
    student = Student.objects.get(id=pid)
    if request.method == "POST":
        clsid = request.POST['classs']
        classid = Class.objects.get(id=clsid)

        fname = request.POST['fullName']
        gender = request.POST['Gender']
        dob = request.POST['DOB']
        fatherName = request.POST['FatherName']
        motherName = request.POST['MotherName']
        contactNumber = request.POST['ContactNumber']
        altenateNumber = request.POST['AltenateNumber']
        address = request.POST['Address']

        student.user.first_name = fname
        student.classs = classid
        student.Gender = gender
        student.DOB = dob
        student.FatherName = fatherName
        student.MotherName = motherName
        student.ContactNumber = contactNumber
        student.AltenateNumber = altenateNumber
        student.Address = address

        try:
            student.save()
            student.user.save()
            error = "no"
        except:
            error = "yes"

        try:
            image = request.FILES['Image']
            student.Image = image
            student.save()
        except:
            pass
    return render(request, 'editStudent.html', locals())


def deleteStudent(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    User.objects.get(id=pid).delete()
    return redirect('manage_Student')


def add_Notice(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    clss = Class.objects.all()
    if request.method == "POST":
        clsid = request.POST['classs']
        classid = Class.objects.get(id=clsid)

        noticeTitle = request.POST['NoticeTitle']
        noticeMsg = request.POST['NoticeMsg']

        try:
            Notice.objects.create(classs=classid, NoticeTitle=noticeTitle, NoticeMsg=noticeMsg)
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_Notice.html', locals())


def manage_Notice(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    notice = Notice.objects.all()
    return render(request, 'manage_Notice.html', locals())


def editNotice(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    clss = Class.objects.all()
    notice = Notice.objects.get(id=pid)
    if request.method == "POST":
        clsid = request.POST['classs']
        classid = Class.objects.get(id=clsid)

        noticeTitle = request.POST['NoticeTitle']
        noticeMsg = request.POST['NoticeMsg']

        notice.classs = classid
        notice.NoticeTitle = noticeTitle
        notice.NoticeMsg = noticeMsg

        try:
            notice.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editNotice.html', locals())


def deleteNotice(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    notice = Notice.objects.get(id=pid)
    notice.delete()
    return redirect('manage_Notice')


def add_PublicNotice(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == "POST":
        noticeTitle = request.POST['NoticeTitle']
        noticeMsg = request.POST['NoticeMsg']

        try:
            Publicnotice.objects.create(NoticeTitle=noticeTitle, NoticeMsg=noticeMsg)
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_PublicNotice.html', locals())


def manage_PublicNotice(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    notice = Publicnotice.objects.all()
    return render(request, 'manage_PublicNotice.html', locals())


def editPubNotice(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    notice = Publicnotice.objects.get(id=pid)
    if request.method == "POST":
        noticeTitle = request.POST['NoticeTitle']
        noticeMsg = request.POST['NoticeMsg']

        notice.NoticeTitle = noticeTitle
        notice.NoticeMsg = noticeMsg

        try:
            notice.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editPubNotice.html', locals())


def deletePubNotice(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    notice = Publicnotice.objects.get(id=pid)
    notice.delete()
    return redirect('manage_PublicNotice')


def reportdate(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        fd = request.POST['FromDate']
        td = request.POST['ToDate']

        student = Student.objects.filter(Q(DateofAdmission__gte=fd) & Q(DateofAdmission__lte=td))
        return render(request, 'bwdatesReport.html', locals())
    return render(request, 'reportdate.html')


def viewStudentDetails(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = Student.objects.get(id=pid)
    return render(request, 'viewStudentDetails.html', locals())


def search(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
        user = [i.id for i in User.objects.filter(Q(first_name__icontains=sd))]
        student = Student.objects.filter(Q(StuID__icontains=sd) | Q(user__in=user))
    return render(request, 'search.html', locals())


def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changePassword.html', locals())


def Logout(request):
    logout(request)
    return redirect('index')


def student_login(request):
    error = ""
    if request.method == 'POST':
        email = request.POST['Email']
        pwd = request.POST['Password']
        user = authenticate(username=email, password=pwd)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'student_login.html', locals())

def user_home(request):

    return render(request, 'user_home.html')

def viewProfile(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    user = User.objects.get(id=request.user.id)
    student = Student.objects.get(user=user)
    return render(request, 'viewProfile.html', locals())

def viewNotice(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    user = request.user
    StudentUser = Student.objects.get(user=user)
    Userccls = StudentUser.classs
    notice = Notice.objects.filter(classs=Userccls)

    return render(request, 'viewNotice.html', locals())

def studentchangePassword(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'studentchangePassword.html', locals())
