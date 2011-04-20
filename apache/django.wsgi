
import os, sys
sys.path.append('/usr/share/pyshared/django')
sys.path.append('/var/www/djcode')
sys.path.append('/var/www/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'djcode.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

