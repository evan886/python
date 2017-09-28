#!/usr/bin/env python2.7
#coding: utf-8

from django import template
import json

register = template.Library()

@register.filter(name='group_str2')
def groups_str2(group_list):
    groupList = []
    for group in group_list:
        #groupList.append('%s->%s' % (group.app_name.app_name, group.role_name))
        #groupList.append('%s' % (group.name))
        groupList.append(str(group))
    if len(group_list) < 3:
        return ', '.join(groupList)
    else:
        return '%s ...' % ' '.join(groupList[0:2])