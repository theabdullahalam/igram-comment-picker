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
            req_mentions = int(req_mentions_str)
            


        comment_text = ''
        comment_username = ''

        if len(errors) == 0:
            # USE IGHELPER
            ig_helper  = InstagramHelper()
            all_comments = ig_helper.get_all_comments(url=post_link)

            # FILTER COMMENTS
            if filter_string != '':
                all_comments = ig_helper.filter_comments(all_comments, filter_string)

            # CHECK MENTIONS
            if req_mentions > 0:
                all_comments = ig_helper.mention_count_filter(all_comments, req_mentions)

            # PICK A RANDOM COMMENT
            random_comment = ig_helper.get_random_comment(all_comments)

            # SET DATA
            if random_comment is not None:
                comment_text = random_comment.text
                comment_username = random_comment.owner.username
            else:
                errors.append('NOCOMMENT')
        

        d = {
            'comment_text': comment_text,
            'comment_username': comment_username,
            'wait': 30,
            'errors': errors
        }
        return JsonResponse(d)

    else:
        return render(request, 'nopower.html')