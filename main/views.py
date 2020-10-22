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

        # print(request.POST)

        # SANITIZE EVERYTHING
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


        # MAKE SURE USERNAME AND PASSWORD ARE BOTH SET IF EITHER ARE SET
        username = request.POST['username']
        password = request.POST['password']

        if len(username) > 0 and len(password) == 0:
            errors.append('NOPASS')

        if len(password) > 0 and len(username) == 0:
            errors.append('NOUSER')
            


        comment_text = ''
        comment_username = ''

        if len(errors) == 0:
            # USE IGHELPER
            random_comment = None
            ig_helper  = InstagramHelper()

            # LOGIN IF USERNAME AND PASS ARE SET
            if len(username) > 0 and len(password) > 0:
                try:
                    ig_helper.set_credentials(username, password)
                except Exception as e:
                    print(e)
                    errors.append('NOLOGIN')


            # FETCH ALL THE COMMENTS
            all_comments = ig_helper.get_all_comments(url=post_link)

            # ERROR HANDLING AND FILTERS
            if len(all_comments) == 0:
                # IF NO COMMENTS RETURNED THEN JUST GIVE UP
                errors.append('NOCOMMENT')

            elif 'NOLOGIN' not in errors:
                # IF SOME COMMENTS WERE RETURNED, THEN PASS THEM THROUGH THE FILTERS

                # FILTER WITH STRING
                if filter_string != '':
                    all_comments = ig_helper.filter_comments(all_comments, filter_string)

                # CHECK MENTIONS
                if req_mentions > 0:
                    all_comments = ig_helper.mention_count_filter(all_comments, req_mentions)

                # CHECK THAT WE DO HAVE COMMENTS
                if len(all_comments) > 0:
                    # PICK A RANDOM COMMENT
                    random_comment = ig_helper.get_random_comment(all_comments)
                else:
                    errors.append('NOMATCH')

                # SET DATA
                if random_comment is not None:
                    comment_text = random_comment.text
                    comment_username = random_comment.owner.username
        

        d = {
            'comment_text': comment_text,
            'comment_username': comment_username,
            'wait': 30,
            'errors': errors
        }
        return JsonResponse(d)

    else:
        return render(request, 'nopower.html')