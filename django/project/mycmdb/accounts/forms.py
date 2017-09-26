#!/usr/bin/env python2.7
#coding: utf-8
"""
============================================================================
Author: yonghuo.x
LastChange: 2017-02-23
History:
        2017-03-27: 添加用户和部门 form.
        2017-03-28: 密码form.
============================================================================
"""

from django import forms
from django.contrib.auth import authenticate,login
from accounts.models import department, myUser

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"用户名",
        error_messages={'required': u'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"用户名",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label=u"密码",
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"密码",
            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()

class deptForm(forms.ModelForm):
    class Meta:
        model = department
        fields = ('departmentName','description')

class userForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(userForm, self).__init__(*args, **kwargs)
       self.fields['department'].queryset = department.objects.filter(availabity=1)
    class Meta:
        model = myUser
        fields = ('username', 'first_name', 'email', 'wechat', 'qq', 'mobile', 'department')

class newPasswordForm(forms.ModelForm):
    newpassword = forms.CharField(required=True, max_length=128, min_length=6, label=u'新密码',widget=forms.PasswordInput)
    renewpassword = forms.CharField(required=True, max_length=128, min_length=6, label=u'确认密码',widget=forms.PasswordInput)

    class Meta:
        model = myUser
        fields = ['newpassword', 'renewpassword']
    def clean(self):
        newpassword = self.cleaned_data.get('newpassword')
        renewpassword = self.cleaned_data.get('renewpassword')
        if newpassword and renewpassword:
            if newpassword != renewpassword:
                raise forms.ValidationError(u"此处必须输入和上栏密码相同的内容")
        return renewpassword

