from django import forms

class MainForm(forms.Form):
    campo1 = forms.CharField()
    campo2 = forms.CharField()
    arquivos = forms.FileField(required=False, 
        widget=forms.ClearableFileInput(attrs={'class':'file-input', 'multiple': True})
    )

    