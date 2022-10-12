from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd

from . import forms

def home(request):
    form = forms.MainForm()

    if request.method == 'POST':
        form = forms.MainForm(request.POST)
        if form.is_valid():

            # campos do formulário
            campo1 = request.POST['campo1']
            campo2 = request.POST['campo2']

            resultados = []

            for f in request.FILES.getlist('arquivos'):    
                fs = FileSystemStorage()
                filename = fs.save(f.name, f) # arquivo vindo do formulário
                uploaded_file_url = fs.url(filename)
            
                resultados.append(tratar_arquivo(filename))

            # objeto context receberá os dados que serão tratados e retornados pelo usuário
            context = {
                'campo1':campo1,
                'campo2':campo2,
                'resultados':resultados
            }

            return render(request, 'core/index.html', {'form':form, 'context':context})
        else:
            print(form.errors)

    return render(request, 'core/index.html', 
		{ 'form': form})

def tratar_arquivo(file):
    df = pd.read_excel(file, engine='openpyxl')
    df.fillna("-",inplace=True)

    field = {
        'headers':list(df.columns.values)[:10], # pega apenas as 10 primeiras colunas
        'rows':tranformar_linhas_dataframe_em_lista(df, 10) # pega as linhas das 10 primeiras colunas
    }

    return field

def tranformar_linhas_dataframe_em_lista(df, numero_colunas):
    rows_lista = []

    for index, row in df.iterrows():
        linha = []

        for coluna in list(df.columns.values)[:numero_colunas]:
            linha.append(row[coluna])

        rows_lista.append(linha)

    return rows_lista