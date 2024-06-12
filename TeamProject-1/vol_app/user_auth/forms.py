from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.contrib.auth.models import User 



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']  # Corrected field names
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']  # Corrected field name
        user.last_name = self.cleaned_data['last_name']  # Corrected field name
        if commit:
            user.save()
        return user
    
class UpdateUserForm(UserChangeForm):
    firstname = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    lastname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label=('Username'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(required=True, label=('Email'))
    password = forms.CharField(label=('New Password'), required=False, widget=forms.PasswordInput(attrs={'placeholder':'New Password','class': 'form-input'}))
    confirm_password = forms.CharField(label=('Confirm Password'), required=False, widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(('Passwords do not match.'))

        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data['email']
        first_name = self.cleaned_data['firstname']  # Use square brackets to access cleaned data
        last_name = self.cleaned_data['lastname']  # Use square brackets to access cleaned data

        if commit:
            user.email = email
            user.first_name = first_name  
            user.last_name = last_name  

            # Check if a new password has been provided
            password = self.cleaned_data.get('password')
            if password:
                user.set_password(password)

            user.save()

        return user