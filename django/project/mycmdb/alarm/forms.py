#coding: utf-8
#author: yonghuo.x
#since: 2017-04-10

from django import forms
from alarm.models import alarm

wayChoices = (
    ('sms', u'SMS'),
    ('email', u'Email'),
)

class alarmForm(forms.ModelForm):
    #def __init__ (self, *args, **kwargs):
    #    super(alarmForm, self).__init__(*args, **kwargs)
    #    print self.fields['way'].__dict__
    #    print self.fields['level'].__dict__
    way = forms.MultipleChoiceField(choices=wayChoices, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = alarm
        fields = ('group', 'name', 'level', 'way', 'user')

    def save(self, *args, **kwargs):
        a = self.instance
        a.way = ','.join(self.cleaned_data['way'])
        a.save()
        alarmSave = super(alarmForm, self).save(*args,**kwargs)
        return alarmSave