from django import forms

from .models import Post

class PostForm(forms.ModelForm): #create a class that extendes forms.ModelForm
    class Meta: #create subclass meta with an obj of post and fields
        model = Post #post obj called model
        fields = ['title', 'text'] #just like destructuring in react but here with a tuple
        