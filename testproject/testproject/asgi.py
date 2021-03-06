import os
import django

from channels.routing import ProtocolTypeRouter
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")

django.setup()
application = ProtocolTypeRouter({
    # (http->django views is added by default)
})
