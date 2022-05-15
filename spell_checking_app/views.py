from django.shortcuts import render
from .checking import *

# Create your views here.
def index(request):
    if request.method == "POST":
        checked_text = check(request.POST.get("text"))
        checked_text = 'Checked text'
        return render(request, 'index.html', {'checked_text': checked_text})

    return render(request, 'index.html')
