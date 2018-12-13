from django import forms
from .models import Employee4
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee4
        fields = "__all__"