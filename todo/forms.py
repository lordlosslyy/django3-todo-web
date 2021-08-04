from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo 
        # fields that you want the user to fill it 
        fields = ['title', 'memo', 'important']