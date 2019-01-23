from django import forms


class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45, widget=forms.TextInput(
        attrs={'id': 'todo_text', 'class': 'validate', 'placeholder': 'E.g, Wash my car',
               'aria-label': 'Todo', 'aria-describeby': 'add-btn'}
    ))
