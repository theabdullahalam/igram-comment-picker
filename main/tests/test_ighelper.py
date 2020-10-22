from django.test import TestCase
from .models import Comment, Owner 
from main.instagramhelper import InstagramHelper

class IgHelperTestCase(TestCase):



    

    def test_is_fetching_public_comments(self):
        print('\nTesting that the igramscraper library is working')

        # MANSI'S POST
        test_url = 'https://www.instagram.com/p/CGXeyu4Hc97/?igshid=45j8ivv1ewpx'
        
        ighelper = InstagramHelper()
        all_comments = ighelper.get_all_comments(test_url)

        self.assertGreaterEqual(len(all_comments), 300, msg=f'Fetched only {len(all_comments)} comments...')







    def test_number_of_mentions(self):
        print('\nTest number of mentions\n')

        all_comments = [
            Comment("Brooo check this out @hamzah @mihir @sumedh @aftab", "abdullah"),
            Comment("Brooo check this out @hamzah @mihir @sumedh @aftab", "abdullah"),
            Comment("Brooo check this out @hamzah @mihir @sumedh @aftab", "abdullah"),
            Comment("Brooo check this out @hamzah @mihir @sumedh @aftab", "abdullah"),
            Comment("Brooo check this out @hamzah @mihir @sumedh @aftab", "abdullah"),
            Comment("Brooo check this out @hamzah @mihir @sumedh @aftab", "abdullah"),
            Comment("Brooo check this out @hamzah @mihir @sumedh @aftab", "abdullah"),
            Comment("Brooo check this out @hamzah @mihir @sumedh @aftab", "abdullah"),
            Comment("Brooo check this out @hamzah @aftab @zulekha", "abdullah"),
            Comment("Brooo check this out @hamzah @aftab @zulekha", "abdullah"),
            Comment("Brooo check this out @hamzah @aftab @zulekha", "abdullah"),
            Comment("Brooo check this out @hamzah @aftab @zulekha", "abdullah"),
            Comment("Brooo check this out @hamzah @mustafa", "abdullah"),
            Comment("Brooo check this out @hamzah @mustafa", "abdullah"),
            Comment("Brooo check this out @hamzah @mustafa", "abdullah"),
            Comment("Brooo check this out @hamzah @mustafa", "abdullah"),
            Comment("Brooo check this out @hamzah @mustafa", "abdullah"),
            Comment("Brooo check this out @hamzah @mustafa", "abdullah"),
            Comment("Brooo check this out @hamzah", "abdullah"),
            Comment("Brooo check this out @hamzah", "abdullah"),
            Comment("Brooo check this out", "abdullah"),
            Comment("Brooo check this out", "abdullah"),
            Comment("Brooo check this out", "abdullah")
        ]

        ighelper = InstagramHelper()

        # RUN HUNDRED TESTS FOR NO MENTIONS
        for i in range(0, 100):
            filtered = ighelper.mention_count_filter(all_comments)
            random_comment = ighelper.get_random_comment(filtered)

            self.assertIsNotNone(random_comment, msg='random_comment is None')

        # RUN HUNDRED TESTS FOR ONE TO FOUR MENTIONS
        for count in range(1, 5):
            for i in range(0, 100):
                filtered = ighelper.mention_count_filter(all_comments, count)
                random_comment = ighelper.get_random_comment(filtered)

                self.assertGreaterEqual(random_comment.text.count('@'), count, msg='There\'s a comment with less than {} mention'.format(count))

    def test_filter_contains_string(self):
        print('\nPick comment hundred times and see if string is present\n')

        all_comments = [
            Comment("Wow this is amazing!", "abdullah"),
            Comment("Nice this is amazing #amaze", "abdullah"),
            Comment("This is crazy #2020", "abdullah"),
            Comment("Ye qafi amazing hai", "abdullah"),
            Comment("Loving it!", "abdullah"),
            Comment("Very amazing, this is!", "abdullah"),
            Comment("Loving it", "abdullah"),
            Comment("Soooo amazing!", "abdullah"),
            Comment("I juuuust love it!", "abdullah"),
            Comment("Prettyyyyyy!", "abdullah"),
            Comment("Pretty!", "abdullah"),
            Comment("Meh", "abdullah"),
        ]

        filtertext = "amazing"
        ighelper = InstagramHelper()

        itworks = True

        for i in range(0,100):
            filtered_comments = ighelper.filter_comments(all_comments, filtertext)
            random_comment = ighelper.get_random_comment(filtered_comments)

            if filtertext not in random_comment.text:
                itworks = False

        self.assertEqual(itworks, True)

    def test_filter_returns(self):
        print('\nTest that filter does return values\n')

        all_comments = [
            Comment("Wow this is amazing!", "abdullah"),
            Comment("Wow this is amazing #amaze", "abdullah"),
            Comment("This is great", "abdullah"),
            Comment("Absolutely adore this", "abdullah"),
            Comment("Fucking amazing!!", "abdullah"),
            Comment("What a horrible post", "abdullah"),
            Comment("This is scum", "abdullah"),
            Comment("Soooo beautiful!", "abdullah"),
            Comment("I juuuust love it!", "abdullah"),
            Comment("Prettyyyyyy!", "abdullah"),
            Comment("Pretty!", "abdullah"),
            Comment("Meh", "abdullah"),
        ]

        filtertext = "amazing"
        nofiltertext = "laser"

        ighelper = InstagramHelper()

        # CHECK THAT COMMENST ARE RETURNED WHEN FILTER WORKS
        filtered_comments = ighelper.filter_comments(all_comments, filtertext)
        self.assertGreater(len(filtered_comments), 0)

        # CHECK THAT NO COMMENTS ARE RETURNED IF STRING IS NOT PRESENT
        nofiltered_comments = ighelper.filter_comments(all_comments, nofiltertext)
        self.assertEqual(len(nofiltered_comments), 0)