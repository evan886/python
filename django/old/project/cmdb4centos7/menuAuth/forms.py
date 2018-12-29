from django import forms
from menuAuth.models import menu

class menuForm(forms.ModelForm):
    class Meta:
        model = menu
        fields = ('name', 'htmlID', 'fatherID', 'icon', 'htmlClass', 'url')