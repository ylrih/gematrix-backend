from django.http import HttpResponse


def test_view(request):
    return HttpResponse(status=200)
