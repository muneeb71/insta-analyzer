# from instagramy import InstagramUser
# import json
# user_name = input("Enter Username: ")
# user = InstagramUser(user_name)
# print(user.posts[0].likes)

# def hello():
#     import instaloader
#     func = instaloader.Instaloader()
#     profile = "irfanjunejo"
#     data = instaloader.Profile.from_username(func.context, profile)
#     print(data)


# import requests
# import streamlit as st
# x = requests.get('/ping')
# print("Hello world")

from flask import Flask
from flask import request


from instagram_scraper import instascraper
app = Flask(__name__)

@app.route('/')
def hello():

   scraper = instascraper(username="shabanat12", password="Vhr@12345")
   profile =  scraper.set_profile(request.args.get("username"))
   if profile == 404:
       return "404 ERROR"
   profile =  scraper.get_profile_data()
#    high = scraper.get_highlights( L = None, profile=None)
   post = scraper.get_post_and_comment()
#    stories = scraper.get_stories(L = None)
   
   return {'profile': profile, 'highlights': [], 'posts': post, 'stories': []}
#    info =  scraper.get_stories(L = None)
#    return info

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
    
     #  if request.args.get("username") and request.args.get("password"):
    #     scraper = instascraper(username="d77815381@gmail.com", password="Fop1020-25")
    #     profile =  scraper.set_profile(request.args.get("user"))
    # else:
    #     scraper = instascraper()
    # profile =  scraper.set_profile(request.args.get("user"))
    # if profile == 404:
    #     return "404 ERROR"
    # info =  scraper.get_profile_data()
    # username="d77815381@gmail.com", password="Fop1020-25"
    # return info