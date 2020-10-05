import os

from django.contrib.sites.models import Site
from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.templatetags.static import static
from django.urls import reverse

from .instagramhelper import InstagramHelper

import time


def index(request):
    return render(request, 'index.html')

def pickwinner(request):

    if request.method == 'POST':    

        print(request.POST)
        # print(request.method)


        # SANITIZE EVERYTHING
        returnthis = ''
        errors = []

        # INSTA POST URL
        post_link = request.POST['postlink']
        if post_link == '':
            errors.append('NOURL')

        # FILTERS
        filter_string = request.POST['filter']

        # REQUIRED NUMBER OF MENTIONS
        req_mentions_str = request.POST['mentions']
        if req_mentions_str == '':
            req_mentions = 0
        else:
            req_mentions = 0

        # CONTACT IGHELPER
        ig_helper  = InstagramHelper()
        returnthis = ig_helper.get_random_comment(url=post_link, filter_string=filter_string, req_mentions=req_mentions)

        if returnthis is None:
            returnthis = "NOURL"

        d = {
            'test': returnthis,
            'errors': errors
        }
        return JsonResponse(d)

    else:
        return render(request, 'nopower.html')