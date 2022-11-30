from django import forms
import datetime

from .models import FormAvis

NOTES = [
        ("1", "Nul"),
        ("2", "Passable"),
        ("3", "Assez Bien"),
        ("4", "Bien"),
        ("5", "Tres Bien")
    ]


class AvisForm(forms.Form):
    nom = forms.CharField(max_length=30, required=False)
    prenom = forms.CharField(max_length=30, required=False)
    note = forms.ChoiceField(choices=NOTES, widget=forms.RadioSelect())
    avis = forms.CharField(max_length=1500, widget=forms.Textarea())
    date = forms.DateField(label='Date', initial=datetime.date.today) #widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    rate = forms.IntegerField()



class Form_avis(forms.ModelForm):
    class Meta:
        model = FormAvis
        # fields = "__all__"
        fields = [
            "nom",
            "prenom",
            "note",
            "avis",
        ]

        widgets = {
            "note": forms.RadioSelect(),
       }
