from django import forms


class RoleForm(forms.Form):
    name = forms.CharField(label='name', max_length=10)
    password = forms.CharField(label='password', widget=forms.PasswordInput)
