from django import forms
from web.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'phone', 'date_of_birth', 'email','image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "enter your name..."}),
            'phone': forms.NumberInput(attrs={'placeholder': "enter your phone number..."}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'placeholder': "enter your email address..."}),
        }

class ContactForm(forms.Form):
    FullName = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "    enter your name...", 'class': 'name-control'}),
        max_length=100,
        required=True
    )
    Email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': '   enter your email...', 'class': 'email-control'}),
        required=True
    )
    Description = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': '   Enter a brief description...', 
            'class': 'description-control',
            'rows': 4, 
            'cols': 50
        }),
        max_length=500,
        required=False
    )