import os
import django
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")

django.setup()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
})
