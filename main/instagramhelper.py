'''
    Author: Abdullah Alam
    Creationg Date: 2020-10-01
    What: A helper class for dealing with the igramscraper module
'''

from igramscraper.instagram import Instagram
import random

class InstagramHelper:

    instagram = None

    def __init__(self):
        self.instagram = Instagram()

    def set_credentials(self, username, password):
        self.instagram.with_credentials(username, password)
        self.instagram.login()


    def get_all_comments(self, url=None, private=False):
        if url is None:
            return None #NOPE OUT IF URL IS NOT PASSED

        all_comment_objs = []
        
        try:
            # REMOVE IGSHID
            if '?igshid=' in url:
                url = str(url).split('?igshid=')[0]


            # GET MEDIA ID
            media = self.instagram.get_media_by_url(url)
            media_id = media.identifier

            # GET COMMENTS
            comments = self.instagram.get_media_comments_by_id(media_id, 10000)
            all_comment_objs = comments['comments']
        except Exception as e:
            print(e)
            pass

        return all_comment_objs


    def filter_comments(self, comments, filter_string):
        valid_comments = []

        # filter is assumed to be a comma seperated list of filters
        # they can be hashtags as well

        # remove inconsistent spaces after commas
        filter_string = filter_string.replace(', ', ',')        
        filters = filter_string.split(',')

        for comment in comments:
            valid_comment = True

            for f in filters:
                if str(f).lower() not in str(comment.text).lower():
                    valid_comment = False

            if valid_comment:
                valid_comments.append(comment)


        return valid_comments



    def mention_count_filter(self, comments, required_count=0):
        valid_comments = []

        for comment in comments:
            if str(comment.text).count('@') >= required_count:
                valid_comments.append(comment)               
            
        return valid_comments

    def get_random_comment(self, comments):
        return comments[random.randint(0, len(comments) - 1 )]