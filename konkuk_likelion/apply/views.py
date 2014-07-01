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
from konkuk_likelion.apply.models import Apply

@csrf_exempt
def apply(request):
	msg = {}
	msg['name'] = request.POST['name'];
	msg['service'] = request.POST['service'];
	msg['introduction'] = request.POST['introduction'];
	msg['phone'] = request.POST['phone'];
	msg['colleage'] = request.POST['colleage'];
	msg['email'] = request.POST['email'];

	print msg
	r = Apply(user=msg['name'],phone=msg['phone'],colleage=msg['colleage'],email=msg['email'],introduction=msg['introduction'],service=msg['service'])
	r.save()

	return HttpResponse("<script>alert('ok'); location.href='/';</script>")
#	return render_to_response('index.html')
#	print request.POST['name'];
	
#def send_smpt(self)

