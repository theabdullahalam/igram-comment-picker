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

