from django import forms
from .models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('__all__')

        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'price': 'Price',
            'email': 'Email ID',
            'addr': 'Address',
        }

        widgets = {
            'fname': forms.TextInput(attrs={'placeholder': 'eg. Prosenjeet'}),
            'lname': forms.TextInput(attrs={'placeholder': 'eg. Shil'}),
            'price': forms.NumberInput(attrs={'placeholder': 'eg. 10000'}),
            'email': forms.EmailInput(attrs={'placeholder': 'eg. abc@xyz.com'}),
            'addr': forms.Textarea(attrs={'placeholder': 'eg. IN'}),
        }
