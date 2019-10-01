# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from requests.models import PreparedRequest



from .form import value_forms



def addparameters(value1,value2,value3):
    return


def post_form(request):
    form = value_forms(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        value1=int(cd['value1'])
        value2 = int(cd['value2'])
        value3 = int(cd['value3'])

        return redirect('api/{}/{}/{}'.format(value1,value2,value3))
    else:
        form = value_forms()

    return render(request, 'post.html', {'form': form})

class result_add(APIView):
    def get(self, request,value1,value2,value3):
        addition_result=sum([value1,value2,value3])
        return Response({"result":addition_result})


# Create your views here.
