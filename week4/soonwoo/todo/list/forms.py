from django import forms
from .models import Todo
 
class CreateTodo(forms.ModelForm):
    class Meta:
        model = Todo
 
        fields = ['body'] 