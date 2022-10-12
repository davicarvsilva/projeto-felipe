from django import forms

class MainForm(forms.Form):
    campo1 = forms.CharField()
    campo2 = forms.CharField()
    arquivos = forms.FileField(required=False, 
        widget=forms.ClearableFileInput(attrs={'class':'file-input', 'multiple': True})
    )

    def __init__(self, *args, **kwargs):
        super(MainForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    