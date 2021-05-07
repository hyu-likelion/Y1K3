from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['work']
        widgets = {
            'work': forms.TextInput(attrs={'placeholder': '추가할 할일을 입력하세요.'})
        }
