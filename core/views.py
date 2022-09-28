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

            return render(request, 'core/index.html', {'form':form})
        else:
            print(form.errors)

    return render(request, 'core/index.html', 
		{ 'form': form})