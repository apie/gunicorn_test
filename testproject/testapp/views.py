from django.http import HttpResponse
from subprocess import call
import logging
import random


logger = logging.getLogger(__name__)

from pymemcache.client.base import Client
client = Client('memcached')


def index(request):
    logger.error(request.headers.get('X-Vhost'))
    busy_count = 0
    for n in range(1, 11):
        if client.get(f'worker_{n}_busy'):
            busy_count += 1
    print(busy_count)
    return HttpResponse(f'index done. busy workers: {busy_count}')


def slow(request):
    logger.error(request.headers.get('X-Vhost'))
    r = random.randint(1,9)
    logger.error(r)
    call(['sleep', f'0.{r}'])
    return HttpResponse('slow done')
