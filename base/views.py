from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from .models import tables, Items
from .loadData import *


# Create your views here.

def home(request):
    return render(request, ("home.html"))

def index(request):
    return render(request, ("index.html"))

def upload_data(request):

    if request.FILES: 
        imagefile=request.FILES['excel_file']
        file_name = default_storage.save(imagefile.name, imagefile)

    
    try:

        sheets = load_data_from_excel(file_name)
        for sheet in sheets:
            new_table = tables.create(sheet['table']["table_name"])

            if new_table:

                for item in sheet['items']:
                    new_instance = Items.create(new_table, item)

    
    except Exception as e:
        print(str(e))
    
    return redirect("admin:index")


