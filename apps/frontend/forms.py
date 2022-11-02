from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(
        attrs={"id": "datetimepicker2"}), initial="")

    phone = PhoneNumberField(widget=forms.TextInput(), region="IN")

    class Meta:
        model = Appointment
        fields = "__all__"
        widgets = {
            'person': forms.Select(attrs={"class": "form-select form-control"}),

        }
