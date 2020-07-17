from django.shortcuts import render

# Create your views here.

def NewEntry(request):
    return render(request, 'newEntry.html')