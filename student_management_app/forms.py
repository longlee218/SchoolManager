from django import forms
from . import models


class StaffForms(forms.ModelForm):
    first_name = forms.CharField(max_length=255, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    last_name = forms.CharField(max_length=255, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}))
    username = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username', 'id': 'id_username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'id': 'id_password'}), required=True)
    password_again = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password again', 'id': 'id_password_again'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Enter email', 'id': 'email', 'type': 'email'}), required=True
    )

    def __init__(self, *args, **kwargs):
        super(StaffForms, self).__init__(*args, **kwargs)
        for i in self.fields.keys():
            self.fields[i].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = models.Staff
        fields = ['address']


class CourseForms(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['course_name']

    def __init__(self, *args, **kwargs):
        super(CourseForms, self).__init__(*args, **kwargs)
        for i in self.fields.keys():
            self.fields[i].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Enter course name',
                'id': 'id_course_name',
            })


class CustomerForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}))
    first_name = forms.CharField(max_length=255, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    last_name = forms.CharField(max_length=255, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}))
    username = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username', 'id': 'id_username'}))

    class Meta:
        model = models.CustomerUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        help_texts = {
            'username': None,
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForms, self).__init__(*args, **kwargs)
        for i in self.fields.keys():
            self.fields[i].widget.attrs.update({
                'class': 'form-control',
            })


class StudentForms(forms.ModelForm):
    session_start_year = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'mm/dd/YYYY', 'type': 'date'}))
    session_end_year = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'mm/dd/YYYY', 'type': 'date'}))
    profile = forms.FileField(required=False)

    class Meta:
        model = models.Student
        fields = ['gender', 'profile', 'address', 'session_start_year', 'session_end_year', 'course_id']

    def __init__(self, *args, **kwargs):
        super(StudentForms, self).__init__(*args, **kwargs)
        for i in self.fields.keys():
            self.fields[i].widget.attrs.update({
                'class': 'form-control'
            })


class SubjectForms(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = ['subject_name', 'course_id']

    def __init__(self, *args, **kwargs):
        super(SubjectForms, self).__init__(*args, **kwargs)
        for i in self.fields.keys():
            self.fields[i].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Enter',
            })