from django.contrib import admin
from .models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']} ),
        ('Date information',{'fields':['pub_date'],'classes': ['collapse']}),

    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
"""
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date','question_text']

admin.site.register(Question,QuestionAdmin)
"""

"""
from .models import Question

admin.site.register(Question)
"""

