from .models import Stud
from django.forms import ModelForm, TextInput, NumberInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudForm(ModelForm):
    class Meta:
        model=Stud
        fields = ['name', 'surname', 'age', 'gpa', 'comment']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Surname'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age'
            }),
            "GPA": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'GPA'
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Comment'
            }),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def init(self, args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserCreationForm, self).init(args, **kwargs)

        username_widget = forms.TextInput(attrs={'placeholder': 'Username'})
        username_field = forms.CharField(label="Username", widget=username_widget)
        self.fields["username"] = username_field

        login_widget = forms.EmailInput(attrs={'placeholder': 'Email'})
        login_field = forms.EmailField(label="Email", widget=login_widget)
        self.fields["email"] = login_field

        pass1_widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        pass1_field = forms.CharField(label="Password", widget=pass1_widget)
        self.fields["password1"] = pass1_field

        pass2_widget = forms.PasswordInput(attrs={'placeholder': 'Re-Password'})
        pass2_field = forms.CharField(label="Re-Password", widget=pass2_widget)
        self.fields["password2"] = pass2_field
