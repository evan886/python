#coding: utf-8
from django import forms
from domainNameManager.models import domainName

class domainForm(forms.ModelForm):
    class Meta:
        model = domainName
        fields = ('name',)
