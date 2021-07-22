from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Please insert Username.'
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Please insert Password.'
    }))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Please insert Email.'
    }))
    phone = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Please insert Phone Number.'
    }))
