from django import forms
from .models import BlogPost, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name',  'class': 'form-control',}))
    last_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control', }))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control',}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email',    'class': 'form-control',}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password','id': 'password',}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']



class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', }))
    
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', 'name': 'password',}))
    
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

      
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook',
                  'instagram', 'linkedin', 'image', )


class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(), max_length = 150)
    
    class Meta:
        model = BlogPost
        fields = ( 'category', 'title', 'slug','content', 'body', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Copy the title with no space and a hyphen in between'}),
            # 'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Blog'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
