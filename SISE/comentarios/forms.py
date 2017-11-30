from django import forms
from comentarios import models

class ComentarioForm(forms.ModelForm):
    class Meta:
        fields = ('comentario',)
        model = models.Comentarios

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user', None)
        super(ComentarioForms, self).__init__(*args,**kwargs)
