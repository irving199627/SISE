from django import forms
from posts import models

class PostForm(forms.ModelForm):
    class Meta:
        fields = ('message',)
        model = models.Post

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user',None)
        super(PostForm, self).__init__(*args,**kwargs)
        # if user is not None:
