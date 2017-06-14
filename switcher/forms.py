from django import forms


class PkgNameForm(forms.Form):
    pkg_name = forms.CharField(label='pkg_name', max_length=10)
