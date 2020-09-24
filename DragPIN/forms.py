from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Profile

class Profileform(forms.ModelForm):
    """A form for creating new DragPIN profiles. Includes all the required
    fields"""
    Identifiers =  (("A", "A"),("B", "B"),("C", "C"),("D", "D"),("E", "E"))
    DragID = forms.CharField()
    PIN    =  forms.CharField(widget=forms.PasswordInput)
    #extras are not allways good
    #Identifier = forms.ChoiceField(choices=Identifiers)
    class Meta:
        model = Profile
        fields = ['DragID', 'PIN', 'Identifier']

class Drag(forms.Form):
        DragID = forms.CharField()

        def __init__(self, *args, **kwargs):
            super(Drag, self).__init__(*args, **kwargs)
            ## add a "form-control" class to each form input
            ## for enabling bootstrap
            for name in self.fields.keys():
                self.fields[name].widget.attrs.update({
                    'class': 'form-control',
                })
