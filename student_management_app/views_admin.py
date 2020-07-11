from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from pytz import unicode

from . import forms
from . import models
from django.contrib import messages
# This views is for Admin
from django.views import View


def showPageAdmin(request):
    return render(request, 'hod_template/home_content.html')


class AddStaffView(View):
    @staticmethod
    def get(request):
        templates = 'hod_template/add_staff_templates.html'
        context = {
            'form': forms.StaffForms(),
        }
        return render(request, templates, context)

    @staticmethod
    def post(request):
        form = forms.StaffForms(data=request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(last_name)
            try:
                user = models.CustomerUser.objects.create_user(first_name=first_name,
                                                               last_name=last_name,
                                                               username=username,
                                                               password=password,
                                                               email=email,
                                                               is_staff=1,
                                                               user_type=2)
                user.staff.address = address
                user.save()
                messages.success(request, 'This staff account have been active!')
                return redirect('add_staff')
            except:
                messages.warning(request, 'Something wrong, please check again!')
                return redirect('add_staff')
        return redirect('add_staff')


def checkUsername(request):
    if request.method == 'GET' and request.is_ajax:
        username = request.GET.get('username', None)
        if models.CustomerUser.objects.filter(username=username).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({'valid': True}, status=200)
    return JsonResponse({}, status=400)


class AddCourseView(View):
    @staticmethod
    def get(request):
        form = forms.CourseForms()
        context = {
            'form': form,
        }
        return render(request, 'hod_template/add_course_templates.html', context)

    @staticmethod
    def post(request):
        form = forms.CourseForms(data=request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Success add this course')
                return redirect('add_course')
            except:
                messages.warning(request, 'Something wrong! Please check again')
                return redirect('add_course')
        messages.warning(request, 'This course name have been exists')
        return redirect('add_course')


def checkCourseName(request):
    if request.method == 'GET' and request.is_ajax:
        name = request.GET.get('course_name', None)
        if models.Course.objects.filter(course_name=name).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({'valid': True}, status=200)
    return JsonResponse({}, status=400)


class AddStudentView(View):
    form_student = forms.StudentForms()
    form_customer = forms.CustomerForms()

    def get(self, request):
        context = {
            'form_student': self.form_student,
            'form_customer': self.form_customer,
        }
        return render(request, 'hod_template/add_student_templates.html', context)

    @staticmethod
    def post(request):
        form_student = forms.StudentForms(data=request.POST)
        form_customer = forms.CustomerForms(data=request.POST)
        if form_customer.is_valid() and form_student.is_valid():
            last_name = form_customer.cleaned_data['last_name']
            first_name = form_customer.cleaned_data['first_name']
            username = form_customer.cleaned_data['username']
            password = form_customer.cleaned_data['password']
            email = form_customer.cleaned_data['email']
            user = models.CustomerUser.objects.create_user(username=username,
                                                           password=password,
                                                           last_name=last_name,
                                                           first_name=first_name,
                                                           email=email,
                                                           user_type=3)
            user.student.gender = form_student.cleaned_data['gender']
            user.student.address = form_student.cleaned_data['address']
            user.student.profile = form_student.cleaned_data['profile']
            user.student.session_start_year = form_student.cleaned_data['session_start_year']
            user.student.session_end_year = form_student.cleaned_data['session_end_year']
            user.student.course_id = models.Course.objects.get(course_name=form_student.cleaned_data['course_id'])
            user.save()
            messages.success(request, 'Success')
            return redirect('add_student')
        messages.warning(request, 'Warning')
        return redirect('add_student')


class AddSubjectView(View):
    @staticmethod
    def get(request):
        form_subject = forms.SubjectForms()
        context = {
            'form': form_subject,
        }
        return render(request, 'hod_template/add_subject_templates.html', context)

    @staticmethod
    def post(request):
        form_subject = forms.SubjectForms(data=request.POST)
        if form_subject.is_valid():
            subject_name = form_subject.cleaned_data['subject_name']
            subject = models.Subject.objects.create(subject_name=subject_name,
                                                    staff_id=request.user,
                                                    course_id=models.Course.objects.get(
                                                        course_name=form_subject.cleaned_data['course_id']))
            subject.save()
            return HttpResponse("Success")
        else:
            return HttpResponse("Error")


def add_subject(request):
    context = {
        'course': models.Course.objects.all()
    }
    return render(request, 'hod_template/add_subject_nul.html', context)


def do_add_sub(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        subject_names = request.POST.getlist('subject_name')
        for subject_name in subject_names:
            new_subject = models.Subject.objects.create(
                subject_name=subject_name,
                staff_id=request.user,
                course_id_id=course_id)
            new_subject.save()
        return HttpResponse(models.Subject.objects.all())
    return HttpResponse('Not valid')