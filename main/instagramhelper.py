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

    def test(self, url):
        # GET MEDIA ID
        media = self.instagram.get_media_by_url(url)
        media_id = media.identifier

        # GET COMMENTS
        comments = self.instagram.get_media_comments_by_id(media_id, 10000)
        comment_objs = comments['comments']

        # SELECT random_comment
        random_index = random.randint(0, len(comment_objs)-1)
        random_comment = comment_objs[random_index]

        # print(random_comment.owner)

        return random_comment.owner.external_url

    # HELPER STUFF
    class Comment:
        def __init__(self, textv):
            self.text = textv

    def get_mock_comments(self):
        comments = [
            self.Comment("This an amazing comment #wow #nice"),
            self.Comment("Crazy stuff buddy"),
            self.Comment("I am enjoying this Canon camera #nikon"),
            self.Comment("I am enjoying this Canon camera #canon"),
            self.Comment("Life is great!"),
            self.Comment("Kya bhenchod giveaway karte rehte"),
            self.Comment("Ek number @abud"),
            self.Comment("Ek number @abud #amaze"),
            self.Comment("Ek number @abud #amaze"),
            self.Comment("Ek number @abud #amaze"),
            self.Comment("Ek number @abud #amaze"),
            self.Comment("Ek number @abud #amaze"),
            self.Comment("Ek number @abud #amaze"),
            self.Comment("Ek number @abud @musti")
            # self.Comment("Ek number @abud @aqsa #amaze"),
            # self.Comment("Noice @abud @aqsa #amaze"),
            # self.Comment("Great @abud @aqsa #amaze"),
            # self.Comment("Perfect @abud @aqsa #amaze"),
            # self.Comment("Beautiful @abud @aqsa #amaze"),
            # self.Comment("Woah @abud @aqsa #amaze"),
            # self.Comment("Crazy @abud @aqsa #amaze"),
        ]

        return comments





    def get_all_comments(self, url=None, private=False):
        if url is None:
            return None #NOPE OUT IF URL IS NOT PASSED
        
        # REMOVE IGSHID
        if '?igshid=' in url:
            url = str(url).split('?igshid=')[0]

        # GET MEDIA ID
        media = self.instagram.get_media_by_url(url)
        media_id = media.identifier

        # GET COMMENTS
        comments = self.instagram.get_media_comments_by_id(media_id, 10000)
        all_comment_objs = comments['comments']

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


    # def get_random_comment(self, url=None, filter_string=None, req_mentions=0):
    #     # SELECT random_comment
    #     returnval = ''
    #     if len(valid_comments) > 0:
    #         random_index = random.randint(0, len(valid_comments)-1)
    #         random_comment = valid_comments[random_index]
    #         returnval = random_comment.text
    #     else:
    #         returnval = 'None'


    #     return returnval