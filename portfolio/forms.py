# forms.py

from django import forms
from .models import Project,Document,Feedback

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'description', 'link', 'technologies']



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file',)



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
