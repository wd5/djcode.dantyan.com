import os, sys
sys.path.append('/usr/share/pyshared/django')
sys.path.append('/usr/share/pyshared/mptt')
<<<<<<< HEAD
sys.path.append('/usr/share/pyshared/tinymce')
sys.path.append('/usr/share/pyshared')
=======
>>>>>>> 581f6faf81bccb4b0a78a1074926e90e866c1305
sys.path.append('/var/www/djcode')
sys.path.append('/var/www/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'djcode.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
