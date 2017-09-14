# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import View
from django.shortcuts import render
from django.shortcuts import render_to_response
#from django.template.context import RequestContext
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
#
from alipay import create_direct_pay_by_user
# Create your views here.

class IndexView(View):
    template = 'IndexTemplate.html'
    def get(self,request):
        context={}
        info=create_direct_pay_by_user(122313423434,"book","product",100)
        context["info"]=info
        return render_to_response(self.template,context)
