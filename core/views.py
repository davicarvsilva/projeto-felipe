from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from . import forms

def home(request):
    form = forms.MainForm()

    if request.method == 'POST':
        form = forms.MainForm(request.POST)
        if form.is_valid():

            # campos do formulário
            campo1 = request.POST['campo1']
            campo2 = request.POST['campo2']

            print(campo1)
            print(campo2)

            for f in request.FILES.getlist('arquivos'):    
                fs = FileSystemStorage()
                filename = fs.save(f.name, f) # arquivo vindo do formulário
                uploaded_file_url = fs.url(filename)
            
                print(filename)

            # objeto context receberá os dados que serão tratados e retornados pelo usuário
            context = {
                'campo1':campo1,
                'campo2':campo2,
                'arquivos':request.FILES.getlist('arquivos')
            }

            return render(request, 'core/index.html', {'form':form, 'context':context})
        else:
            print(form.errors)

    return render(request, 'core/index.html', 
		{ 'form': form})