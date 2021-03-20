from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import CsvForm
import os

# Create your views here.

# create view to take the csv and save the different assignments

def upload_csv(request):

    if request.method == 'POST':
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(reverse('home'))
    else:
        form = CsvForm()
        context = {
            'form': form
        }

    return render(request, 'managing_deadlines/uploading_csv.html', context)

