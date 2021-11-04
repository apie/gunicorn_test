from django.http import HttpResponse
from subprocess import call
import logging
import random


logger = logging.getLogger(__name__)


def index(request):
    logger.error(request.headers.get('X-Vhost'))
    return HttpResponse('index done')


def slow(request):
    logger.error(request.headers.get('X-Vhost'))
    r = random.randint(1,9)
    logger.error(r)
    call(['sleep', f'0.{r}'])
    return HttpResponse('slow done')
