'''
Based on
https://stackoverflow.com/questions/52025195/any-way-to-read-number-of-active-workers-of-gunicorn-managed-by-the-arbiter-from
'''

from pymemcache.client.base import Client
client = Client('memcached')

def pre_request(worker, req):
    worker.log.increment('busy_workers', 1)
    client.set(f'worker_{worker.nr}_busy', 'true')

def post_request(worker, req, environ, resp):
    worker.log.decrement('busy_workers', 1)
    client.set(f'worker_{worker.nr}_busy', '')
