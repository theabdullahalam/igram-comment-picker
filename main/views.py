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

    post_link = request.POST['postlink']
    filter_string = request.POST['filter']

    ig_helper  = InstagramHelper()
    returnthis = ig_helper.get_random_comment(post_link, filter_string)

    if returnthis is None:
        returnthis = "NOURL"

    d = {
        'test': returnthis
    }
    return JsonResponse(d)