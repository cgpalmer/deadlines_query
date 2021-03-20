from django.shortcuts import render
from .forms import CsvForm
import pandas as pd
import numpy as np
import os

# Create your views here.

# create view to take the csv and save the different assignments

def upload_csv(request):
    form = CsvForm()
    context = {
        'form': form
    }

    return render(request, 'managing_deadlines/uploading_csv.html', context)

