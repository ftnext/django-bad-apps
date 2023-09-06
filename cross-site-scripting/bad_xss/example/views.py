from django.http import HttpResponse
from django.template.response import TemplateResponse


def example(request):
    # return HttpResponse("Hello world")
    # return HttpResponse('<script>alert("XSSです")</script>')

    context = {"message": '<script>alert("XSSです")</script>'}
    return TemplateResponse(request, "example/index.html", context)
