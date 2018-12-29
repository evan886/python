# coding:utf-8
from django import forms
from configManager.models import config

class configForm(forms.ModelForm):
    class Meta:
        model = config
        fields = ('config_name', 'config_type', 'config_dir')
