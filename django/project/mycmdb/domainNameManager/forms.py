#coding: utf-8
from django import forms
from domainNameManager.models import domainName

class domainForm(forms.ModelForm):
    class Meta:
        model = domainName
        #fields = ('name', 'nameDistributor','exptresDate','user','email','organization','availabity',)
        #fields = ['group', 'server_type', 'ip', 'intraip', 'other_ip', 'port', 'is_monitoring', 'is_backup', 'config','app_name', 'role_name', 'editor']
        #fields = ['name','nameDistributor'，'exptresDate']
        #fields = ['name', 'nameDistributor', 'exptresDate', 'user', 'email', 'organization', 'availabity']
        fields = ['name', 'nameDistributor', 'exptresDate', 'user', 'email', 'organization']
        #fields = ('name',)  #bak  原来 是元组 改为列表 就好了 20171010
