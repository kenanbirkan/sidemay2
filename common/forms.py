from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from django.contrib.auth.forms import AuthenticationForm



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
    iban = forms.CharField(
        help_text="IBAN NO"
    )
    sandik = forms.IntegerField(
        help_text="Sandik aidat miktari"
    )
    dernek = forms.IntegerField(
        help_text="Dernek aidat miktari"
    )
    address = forms.CharField()

    tel = forms.CharField()

    start_date = forms.DateField(
        help_text="Baslangic tarihi",
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('username', css_class='input-xlarge'),
        Field('first_name', css_class='input-xlarge'),
        Field('last_name', css_class='input-xlarge'),
        Field('email', css_class='input-xlarge'),
        Field('iban', css_class='input-xlarge'),
        Field('sandik', css_class='input-xlarge'),
        Field('dernek', css_class='input-xlarge'),
        Field('address', css_class='input-xlarge'),
        Field('tel', css_class='input-xlarge'),
        Field('start_date', css_class='input-xlarge'),
        FormActions(
            Submit('save_changes', 'Kaydet', css_class="btn-primary"),
            Submit('Vazgec', 'Vazgec'),
        )
    )

class DuesForm(forms.Form):
    tc = forms.CharField(
        help_text="TC NO girilecek"
    )
    value = forms.IntegerField(
        help_text="miktar"
    )
    insert_date = forms.DateField(
        help_text="Kayit tarihi",
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('tc', css_class='input-xlarge',width="50px" ,height="50px"),
        Field('value', css_class='input-xlarge'),
        Field('insert_date', css_class='input-xlarge'),
        FormActions(
            Submit('save_changes', 'Kaydet', css_class="btn-primary"),
            Submit('Vazgec', 'Vazgec'),
        )
    )


class TCrequestForm(forms.Form):
    tc = forms.IntegerField(label="TC NO giriniz", required=True)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Field('tc', css_class='input-sm'),
        FormActions(Submit('SORGULA', 'SORGULA', css_class='btn-primary'))
    )


class karPayirequestForm(forms.Form):
    kar_payi = forms.CharField(label="Kar payi giriniz", required=True)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Field('kar_payi', css_class='input-sm'),
        FormActions(Submit('SORGULA', 'SORGULA', css_class='btn-primary'))
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))