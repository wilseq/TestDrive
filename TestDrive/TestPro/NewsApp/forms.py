from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100,
                widget=forms.TextInput(attrs={
                    'class': 'form_control',
                    'placeholder':'Username'
                }))

    password = forms.CharField(max_length=100,
                widget = forms.PasswordInput(attrs={
                'class': 'form_control',
                'placeholder': 'Password'
                }))
    email = forms.CharField(max_length=100,
                widget=forms.EmailInput(attrs={
                'class': 'form_control',
                'placeholder': 'Email'
                }))
    phone = forms.CharField(max_length=100,
                widget = forms.NumberInput(attrs={
                'class': 'form_control',
                'placeholder': 'Phone number'
                }))