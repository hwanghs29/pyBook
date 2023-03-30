from django import forms
from .models import Question


class PollForm(forms.ModelForm):
    class Meta:
        Model = Question
        #fields = ['question_text']
        fields = '__all__'
