import os, sys
sys.path.append('/usr/share/pyshared/django')
sys.path.append('/usr/share/pyshared/mptt')
sys.path.append('/usr/share/pyshared/tinymce')
sys.path.append('/usr/share/pyshared')
sys.path.append('/var/www/djcode')
sys.path.append('/var/www/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'djcode.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()