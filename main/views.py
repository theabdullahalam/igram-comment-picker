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

    ig_helper  = InstagramHelper()
    ig_helper.test(post_link)

    returnthis = ig_helper.test(post_link)

    d = {
        'test': returnthis
    }
    return JsonResponse(d)