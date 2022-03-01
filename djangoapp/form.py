from django import forms
from django.forms import ModelForm
from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre question'}),
        }
