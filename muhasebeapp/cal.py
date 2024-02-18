from fileinput import filename
import io
from xml.dom.minidom import DocumentFragment

from django.http import HttpResponse
from django.shortcuts import render

from .forms import DocumentForm


def OnlyCAL(request):
    if request.method == "POST":
        form = DocumentFragment(request.POST, request.FILES)
        if form.is_valid():
            output = io.BytesIO()
            newdoc = request.FILES['docfile']
                #pandas calculations

            response = HttpResponse(
                output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=%s' % filename
            return response
    else:
        form = DocumentForm()
    return render(request, 'muhasebeapp/cal.html', { 'form': form})

