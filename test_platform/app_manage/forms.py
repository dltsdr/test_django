from django import forms
from django.forms import widgets

class ProjectForm(forms.Form):
    name = forms.CharField(label='名称', 
                           max_length=100,
                           widget = widgets.TextInput(attrs={'class':"form-control"}))
    
    describe = forms.CharField(label="描述", 
                               widget = widgets.Textarea(attrs={'class':"form-control"}))
    
    status = forms.BooleanField(label="状态", required=False,
                                widget = widgets.CheckboxInput()
                                )

    