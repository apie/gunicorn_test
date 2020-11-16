from django.http import HttpResponse
from subprocess import call


def index(request):
    return HttpResponse('index done')


def slow(request):
    call(['sleep', '10'])
    return HttpResponse('slow done')
