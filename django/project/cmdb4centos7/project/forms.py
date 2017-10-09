# coding:utf-8
from django import forms
from project.models import app, appRole




class appForm(forms.ModelForm):
    class Meta:
        model = app
        fields = ['name', 'another_name', 'roles', 'architecture']

class appRoleForm(forms.ModelForm):
    class Meta:
        model = appRole
        fields = ['name']