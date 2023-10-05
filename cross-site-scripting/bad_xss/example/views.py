from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.html import escape


def example(request):
    return TemplateResponse(request, "example/index.html")


def alert(request):
    # return HttpResponse("Hello world")
    return HttpResponse('<script>alert("XSSです")</script>')
    # Correct implementation:
    # return HttpResponse(escape('<script>alert("XSSです")</script>'))

    # context = {"message": '<script>alert("XSSです")</script>'}
    # return TemplateResponse(request, "example/alert.html", context)
