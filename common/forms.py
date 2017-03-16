from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms


from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions,InlineRadios


class UserForm(forms.Form):
    username = forms.CharField(
        help_text="TC NO girilecek"
    )
    first_name = forms.CharField(
        help_text="AD"
    )
    last_name = forms.CharField(
        help_text="SOYAD"
    )
    email = forms.EmailField(
        help_text="email adres"
    )
    sandik = forms.IntegerField(
        help_text="Sandik aidat miktari"
    )
    dernek = forms.IntegerField(
        help_text="Dernek aidat miktari"
    )
    address = forms.CharField()

    tel = forms.CharField()

    grup = forms.ChoiceField(
        choices=(
            ("1", "Isci"),
            ("2", "Memur")
        ),
        widget=forms.RadioSelect,
        initial=1,
    )
    start_date = forms.DateField(
        help_text="Baslangic tarihi"
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('username', css_class='input-xlarge'),
        Field('first_name', css_class='input-xlarge'),
        Field('last_name', css_class='input-xlarge'),
        Field('email', css_class='input-xlarge'),
        Field('sandik', css_class='input-xlarge'),
        Field('dernek', css_class='input-xlarge'),
        Field('address', css_class='input-xlarge'),
        Field('tel', css_class='input-xlarge'),
        InlineRadios('grup'),
        Field('start_date', css_class='input-xlarge'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )





class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))