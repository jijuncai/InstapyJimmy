"""
This template is written by @cormo1990

What does this quickstart script aim to do?
- Basic follow/unfollow activity.

NOTES:
- I don't want to automate comment and too much likes because I want to do
this only for post that I really like the content so at the moment I only
use the function follow/unfollow.
- I use two files "quickstart", one for follow and one for unfollow.
- I noticed that the most important thing is that the account from where I
get followers has similar contents to mine in order to be sure that my
content could be appreciated. After the following step, I start unfollowing
the user that don't followed me back.
- At the end I clean my account unfollowing all the users followed with
InstaPy.
"""

# imports
import time
import logging
from instapy import InstaPy
from instapy.util import smart_run
from proxy_extension import create_proxy_extension

# login credentials
insta_username = 'super_cool_star'
insta_password = 'jackychen8'

proxy = 'lum-customer-hl_648f8412-zone-static-ip-185.217.61.22:9y4lv38oag4e@zproxy.lum-superproxy.io:22225'
proxy_chrome_extension = create_proxy_extension(proxy)

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  proxy_chrome_extension=proxy_chrome_extension, 
                  nogui=False,
                  headless_browser=True)

with smart_run(session):
    while True:
       cur = time.time()
      
       time.sleep(10)
       session.like_by_tags(['love'], amount=1, interact=False)
       time.sleep(10)

       time.sleep(10)              
       session.like_by_tags(['instagood'], amount=1, interact=False)
       time.sleep(10)

       time.sleep(10)
       session.like_by_tags(['photooftheday'], amount=1, interact=False)
       time.sleep(10)

       time.sleep(10)
       session.like_by_tags(['fashion'], amount=1, interact=False)
       time.sleep(10)
