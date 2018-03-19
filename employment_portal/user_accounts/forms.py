from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserSignUp(UserCreationForm):
    #email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.', required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email',)
        widgets={
        'username' : forms.TextInput (attrs={'cols':40,'rows':1,'class': "form-control",'placeholder':'Username'}),
        'password1' : forms.TextInput (attrs={'cols':40,'rows':1,'class': "form-control",'placeholder':'Password'}),
        'password2' : forms.TextInput (attrs={'cols':40,'rows':1,'class': "form-control",'placeholder':'Password'}),
        }




class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True,widget=forms.TextInput(attrs={'placeholder':"Username",'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Password",'class': "form-control"}), required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
