from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

import httplib, json
import smtplib
from email.mime.text import MIMEText


def index(request):
	return render_to_response('index.html')

