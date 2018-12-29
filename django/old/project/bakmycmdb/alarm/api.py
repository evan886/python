#coding: utf-8
#author: yonghuo.x
#since: 2017-04-11

from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication

from alarm.models import alarm
from lib.send import sendEmail

def send(group,level,message):
    try:
        sendInfo = alarm.objects.get(group=group,level=level,availabity=1)
        for w in sendInfo.way.split(','):
            if w == 'email':
                title = u'运维告警系统'
                emailList = []
                for u in sendInfo.user.all():
                    emailList.append(u.email)
                return sendEmail(emailList,title,message)
    except Exception as e:
        #import traceback
        #print traceback.print_exc()
        return {'code':2,'message':u'发送失败'}

    return {'code':1,'message':'succeed'}


class alarmApi(ModelResource):
    class Meta:
        resource_name = 'alarmSend'
        authentication = ApiKeyAuthentication()

    def get_list(self,request,**kwargs):
        bundles = '111111111111111'
        return self.create_response(request,bundles)

    def post_list(self, request,**kwargs):
        deserialized = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))
        try:
            level = deserialized['level']
            message = deserialized['message']
        except:
            content = {'code':0, 'message':u'参数不正确。'}
            return self.create_response(request, content)
        if deserialized.has_key('group'):
            group = deserialized['group']
        else:
            group = 0001
        content = send(group,level,message)
        return self.create_response(request, content)