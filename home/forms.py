from django import forms
from .models import Complain

class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ['gurdian_name', 'gurdian_email', 'student_name', 'class_name', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
