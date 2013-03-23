from apps.irgat.forms import IrgatForm
from apps.irgat.models import Atar
from django.shortcuts import render

def atar_yap(request, template="irgat/index.html"):

    if request.method == "POST":
        form = IrgatForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = IrgatForm()

    ctx = {
        'form' : form
    }

    return render(request, template, ctx)
