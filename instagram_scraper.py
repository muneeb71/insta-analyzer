import instaloader
from instaloader import Post
# from sentiment_analysis import SentimentAnalysis

class instascraper():
    def __init__(self, username=None, password=None, session_user=None):
        self.L = instaloader.Instaloader(
            dirname_pattern="posts/{profile}/{date}")
        # self.analizer = SentimentAnalysis()
        if session_user is None and username and password is not None:
            print('logging in ... ')
            try:
                self.L.load_session_from_file(username)
                name = self.L.test_login()
                if(name is None):
                    self.L.login(username, password)
                    print('logged in -> ', username)
                    self.L.save_session_to_file()   
                    self.Logged = True
                    print(name, "name")
                    print('logged in using session-> ', username)
            except Exception as e:
                print('New User')
                try:
                    self.L.login(username, password)
                    print('logged in -> ', username)
                    self.L.save_session_to_file()   
                    self.Logged = True
                except Exception as ex:
                    print(ex)
                    self.Logged = ex
        else:
            pass
    
    #SET PROFILE FOR THE CURRENT SESSION
    def set_profile(self ,username_profile):
        try:
            self.profile = instaloader.Profile.from_username(self.L.context, username_profile)
            print("PROFILE -->", self.profile)
            return self.profile
        except Exception as ex:
            return 404
    
    #RETURN PROFILE DATA
    def get_profile_data( self, profile = None):
        if profile is None:
            profile = self.profile
        if profile.is_private == True and profile.followed_by_viewer == True and self.Logged:
            print("here")
            try:
                temp_has_public_story = profile.has_public_story
                temp_has_viewable_story = profile.has_viewable_story
            except Exception as ex:
                print("EXECPTION -->", ex)
                temp_has_public_story = None
                temp_has_viewable_story = None
            dict_profile_data = {
            'user_id': profile.userid,
            'username': profile.username,
            'followed_by_viewer': profile.followed_by_viewer,
            'post_count': profile.mediacount,
            'igtv_count': profile.igtvcount,
            'n_follower': profile.followers,
            'n_followees': profile.followees,
            'external_url': profile.external_url,
            'is_bussines': profile.is_business_account,
            'business_Category': profile.business_category_name,
            'biography': profile.biography,
            'blocked_by_viewer': profile.blocked_by_viewer,
            'follows_viewer': profile.follows_viewer,
            'full_name': profile.full_name,
            'has_blocked_viewer': profile.has_blocked_viewer,
            'has_public_story': temp_has_public_story,
            'has_viewable_story': temp_has_viewable_story,
            'has_requested_viewer': profile.has_requested_viewer,
            'is_verified': profile.is_verified,
            'requested_by_viewer': profile.requested_by_viewer,
            'profile_pic_url': profile.profile_pic_url,
            'has_higlighted_reels': profile.has_highlight_reels,
            'followed_by_viewer': profile.followed_by_viewer
            }
            return dict_profile_data
        if profile.is_private == True:
            dict_profile = {
                 'username': profile.username,
                 'n_follower': profile.followers,
                 'n_followees': profile.followees,
                 'post_count': profile.mediacount,
                 'profile_pic_url': profile.profile_pic_url,
                 'full_name': profile.full_name,
                 
             }
            print('PRIVINFO NOT AVAILABLE')
            return dict_profile
        

        dict_profile_data = {
            'user_id': profile.userid,
            'username': profile.username,
            'followed_by_viewer': profile.followed_by_viewer,
            'post_count': profile.mediacount,
            'igtv_count': profile.igtvcount,
            'n_follower': profile.followers,
            'n_followees': profile.followees,
            'external_url': profile.external_url,
            'is_bussines': profile.is_business_account,
            'business_Category': profile.business_category_name,
            'biography': profile.biography,
            'blocked_by_viewer': profile.blocked_by_viewer,
            'follows_viewer': profile.follows_viewer,
            'full_name': profile.full_name,
            'has_blocked_viewer': profile.has_blocked_viewer,
            'has_requested_viewer': profile.has_requested_viewer,
            'is_verified': profile.is_verified,
            'requested_by_viewer': profile.requested_by_viewer,
            'profile_pic_url': profile.profile_pic_url,
            'has_higlighted_reels': profile.has_highlight_reels,
            'followed_by_viewer': profile.followed_by_viewer
            }
        # temp_vect.append(dict_profile_data)
        # profile_data = pd.DataFrame(temp_vect, index = ['data_profile'])

        return dict_profile_data

    # GET DATA POST FROM SHORTCODE
    # def get_post_from_shortcode( self, SHORTCODE: str, MAX_COMMENT: int):
    #     post = Post.from_shortcode(self.L.context, SHORTCODE)
    #     try:
    #         accessibility_caption = str(post._asdict()['accessibility_caption'])
    #     except Exception as ex:
    #         print(ex)
    #     try:
    #         location = post.location
    #     except Exception as ex:
    #         print(ex)
    #         location = None
    #         #INFORMATION OF THE POST GOING INTO THE CSV
    #         post_info_dict = {
    #             'title': post.title,
    #             'owner_username': post.owner_username,
    #             'date_and_time': post.date,
    #             'type_of_post': post.typename,
    #             'mediacount': post.mediacount,
    #             'caption': post.caption,
    #             'n_caption_hashatags': len(post.caption_hashtags),
    #             'caption_hashtags': post.caption_hashtags,
    #             'n_mentions_post': len(post.caption_mentions),
    #             'n_tagged_users': len(post.tagged_users),
    #             'is_video': post.is_video,
    #             'n_likes': post.likes,
    #             'n_comments': post.comments,
    #             'is_sponsored': post.is_sponsored,
    #             'sponsors': post.sponsor_users,
    #             'location': location,
    #             'url_link': post.url,
    #             'url_insta': 'instagram.com/p/{}/'.format(post.shortcode),
    #             'description_of_post': accessibility_caption,
    #         }
    #         comments_vect = []
    #         # DOWNLOAD AND STORE COMMENT
    #         print('Start Comments', end='')

    #         comment_count = 0
    #         for comment in post.get_comments():
    #             answer_count = 0
    #             for answer in comment.answers:
    #                 answer_count += 1
    #                 if answer_count == 50:
    #                     break
    #             analisys, score = self.analizer.return_sentiment(
    #                 str(comment.text).strip())
    #             comment_info_dict = {
    #                 'date_and_time': comment.created_at_utc,
    #                 'profile': comment.owner.username,
    #                 'text': str(comment.text).strip(),
    #                 'n_likes': comment.likes_count,
    #                 'answer_count': answer_count,
    #                 'sentiment_analysis': analisys,
    #                 'score': score
    #             }

    #             comments_vect.append(comment_info_dict)
    #             if comment_count == MAX_COMMENT:
    #                 break
    #             comment_count += 1
    #             print('.', end='')
    #         print('End Comments')
    #         comment_df = pd.DataFrame(comments_vect)
    #         post_df = pd.DataFrame([post_info_dict])

    #         return post_df, comment_df

    #GET POST OF THE SETTET PROFILE OR SET profile input to set a new one
    def get_highlights(self, L = None, profile=None):
            if profile is None:
                profile = self.profile
            if L is None:
                L = self.L
            info = []
            for item in L.get_highlights(profile):
                profile_highlights = {"hightlight_info": {}, "items": []}
                high_info_dict = {
                    'owner': item.owner_username,
                    'title': item.title,
                    'count': item.itemcount,
                    'cover': item.cover_url
                         }
                profile_highlights['highlight_info'] = high_info_dict
                for ht in item.get_items():
                    highlight_story = {
                        'url': ht.url,
                        'date': ht.date_local,
                        'is_video': ht.is_video,
                        'video_url': ht.video_url,
                        }
                    profile_highlights['items'].append(highlight_story)
                info.append(profile_highlights)
            return info  
                
        
    def get_post_and_comment(self, MAX_COMMENT = 4, L = None, MAX_POST=2, profile=None):
        if profile is None:
            profile = self.profile
        if L is None:
            L = self.L
        counter_post = 1
        post_profile = {"profile": profile.username, 'posts': []}
        for post in profile.get_posts():
            print("POST n:", counter_post, "MAX_COMMENT_SET:", MAX_COMMENT)
            comments_vect = []
            try:
                accessibility_caption = str(
                    post._asdict()['accessibility_caption'])
            except Exception as ex:
                print(ex)
                accessibility_caption = None
            try:
                location = post.location
            except Exception as ex:
                print(ex)
                location = None
            #INFORMATION OF THE POST GOING INTO THE CSV
            post_info_dict = {
                'title': post.title,
                'owner_username': post.owner_username,
                'date_and_time': post.date,
                'type_of_post': post.typename,
                'mediacount': post.mediacount,
                'caption': post.caption,
                'n_caption_hashatags': len(post.caption_hashtags),
                'caption_hashtags': post.caption_hashtags,
                'n_mentions_post': len(post.caption_mentions),
                'n_tagged_users': len(post.tagged_users),
                'is_video': post.is_video,
                'video_views': post.video_view_count,
                'n_likes': post.likes,
                'n_comments': post.comments,
                'is_sponsored': post.is_sponsored,
                'sponsors': post.sponsor_users,
                'location': location,
                'url_link' : post.url,
                'url_insta': 'instagram.com/p/{}/'.format(post.shortcode),
                'description_of_post': accessibility_caption,
                'engagement_rate': ((int(post.likes) + int(post.comments)) / int(profile.followers))   * 100
            }

            # DOWNLOAD AND STORE COMMENT
            print('Start Comments')

            comment_count = 0
            for comment in post.get_comments():
                # answer_count = 0
                # """
                # for answer in comment.answers:
                #     answer_count += 1
                #     if answer_count == 5:
                #         break
                # """
                # analisys, score = self.analizer.return_sentiment(
                #     str(comment.text).strip())
                comment_info_dict = {
                    'date_and_time': comment.created_at_utc,
                    'profile': comment.owner.username,
                    'text': comment.text,
                    'n_likes': comment.likes_count,
                }
                comments_vect.append(comment_info_dict)
                if comment_count == MAX_COMMENT:
                    print("MAX COMMENT")
                    break
                comment_count += 1
                print(comment_count, '.', end='')
            
            print('End Comments')

            #L.download_pic(path_pic_jpg, post.url, post.date_utc)

            #STORING DATA SCRAPED AND UPLOAD RELATIVE CSVs
            # comment_df = pd.DataFrame(comments_vect)
            # post_df = pd.DataFrame([post_info_dict], index=['post_data'])

            post = {'post_info': post_info_dict, 'comments': comments_vect}
            post_profile['posts'].append(post)
            print("END__POST")
            #IF MAX POST DOWNLOADED BREAK
            if counter_post == MAX_POST:
                print('Post Reached')
                break
            counter_post += 1

        return post_profile
    
    def get_stories(self, L = None):
        info = []
        if L is None:
            L = self.L
        for items in L.get_stories([self.profile.userid]):
            for item in items.get_items():
                story = {
                    'id': item.mediaid,
                    'profile': item.profile,
                    'url': item.url,
                    'type': item.typename,
                    'video_url': item.video_url
                }
                info.append(story)
        return info
if __name__ == '__main__':
    scraper = instascraper(username='test_lorenz', password='provaprova')
    profile = scraper.set_profile(username_profile="joridelli")
    print(scraper.get_profile_data())
    post_profile = scraper.get_post_and_comment(scraper, 50, 5, profile)
    print(post_profile['posts'][1]['comments'])
