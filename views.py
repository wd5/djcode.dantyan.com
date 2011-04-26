# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

class BaseView(TemplateView):
	template_name = "template.djhtml"

def welcome(request):
	""" show index page """
	return render_to_response('welcome.djhtml')


#import datetime
#
#
#def hello(request):
#	return HttpResponse("Здравствуй, Мир")
#
#def current_datetime(request):
#	now = datetime.datetime.now()
#	return render_to_response('current_datetime.html', {'current_date': now})
#
#
#def hours_ahead(request, offset):
#	try:
#		offset = int(offset)
#	except ValueError:
#		raise Http404()
#	
#	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#	return HttpResponse(html)
