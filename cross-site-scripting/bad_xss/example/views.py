from django.http import HttpResponse


def example(request):
    # return HttpResponse("Hello world")
    return HttpResponse('<script>alert("XSSです")</script>')
