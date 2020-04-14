from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
# from django.utils.safestring import mark_safe

class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': 
                """
                <span>150 characters or fewer.</span> 
                <span>Only letters, digits and @/./+/-/_ are allowed</span>
                """,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
        
        self.fields['password1'].help_text = (
                    """
                        <span>Your password can't be too similar to your other personal information.</span>
                        <span>Your password must contain at least 8 characters.</span>
                        <span>Your password can't be a commonly used password.</span>
                        <span>Your password can't be entirely numeric.</span>
                    """
                    )    
    

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password'].widget.attrs['placeholder'] = 'password'
