# Reddit Bot Class

**This is a class that can be used to create multiple different reddit bots.**

![GitHub](https://img.shields.io/github/license/tom-pettit/RedditBotClass?style=for-the-badge)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/tom-pettit/RedditBotClass?style=for-the-badge)

## Table of Contents 
- [Installation](#installation)
- [Setup](#setup)
- [Features](#features)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)


---

## Installation

> Can be installed via pip.

```terminal
pip install RedditBotClass
```

> PyPi link: https://pypi.org/project/RedditBotClass/

---

### Setup
> Before you can use this class, you have to have created a bot associated to a reddit account. I have written a guide on how to do this: https://github.com/tom-pettit/CreatingARedditBotGuide 

> It's also a requirement that the bot has moderator permissions for the subreddit it is intended to run upon.

```python
bot = RedditBot(CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD, SUBREDDIT, [LIST_OF_DODGY_SITES], [LIST_OF_MODERATORS], BANDWIDTH)
```
- CLIENT_ID, CLIENT_SECRET, USER_AGENT: These are obtained from following the tutorial I have linked above. The USER_AGENT is typically just a short description of what your bot does, or a name that identifies your bot. 

> A more detailed description of USER_AGENT can be found in the PRAW docs: https://praw.readthedocs.io/en/latest/getting_started/quick_start.html#:~:text=User%20Agent%3A,For%20example%2C%20android%3Acom.

- USERNAME, PASSWORD: These are the login credentials for the reddit account the bot will be running on.

- SUBREDDIT: This is the subreddit that the bot you want to create has moderator permissions for and is intended to operate upon. 

- [LIST_OF_DODGY_SITES]: This is a list of websites that you don't want users to be able to post to your subreddit with. eg ['pornhub.com', 'porn.com'] 

- [LIST_OF_MODERATORS]: This is a list of the moderators on the subreddit you want the bot to run on. This is specifically for the method: 
```python
check_for_mod_comments(self) 
```

- BANDWIDTH: This has a default value set to 'medium'. This is for people who may not have a lot of compute power on which to run their bot, or they want to cut costs, or would want the bot to run more frequently. A value of 'low' means the bot runs every 150 seconds. A value of 'medium' means the bot runs every 100 seconds. A value of 'high' means the bot runs every 150 seconds.

**Running the bot**
> In order to run the bot, instantiate the object, and then call the method: start_cycle. As shown: 
```python
bot = RedditBot(CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD, SUBREDDIT, [LIST_OF_DODGY_SITES], [LIST_OF_MODERATORS], BANDWIDTH)
bot.start_cycle()
```
> Remember to use your own credentials instead of these placeholder arguments!

> However, as will be explained later, if you only want to run certain methods, then you have to define this in the arguments of start_cycle. See the explanation of this in the Features section below, and scroll down to the start_cycle method.

---

## Features
> There are many different methods that each RedditBot object can access

**Check if new posts are flaired**

```python
check_new_posts_flair(self) 
```
> When this method is run, it iterates through the newest posts to the subreddit. It then checks if these new posts have flairs. If they do, it leaves the post alone. However, if the post has no flair, the bot comments on the post to let the user know that they need to flair their post next time, and then it automatically makes the post hidden.

> To improve efficiency, an instance object is used to save the ID of posts that the bot has checked for a flair:

```python
self.visited_flaired_posts
```

> This means that when the bot checks the newest posts each time the method is called, it won't go through all its logic twice for the same post, as it saves the IDs of previously checked posts, and doesn't fulfill its logic if it has seen a post's ID before.

**Removing posts from URLs that are blacklisted**

```python
remove_dodgy_website_posts(self)
```
> When this method is run, it iterates through the newest posts to the subreddit. It then compares the URLs of these new posts to the links provided in the [LIST_OF_DODGY_SITES] argument. If the URL of the submission contains / is the same as any of the links in this argument, then the author of the post is private messaged to ask them to not post from that URL again, and to tell them their post has been removed.

> Again, to improve efficiency, an instance object is created to save the ID of posts it has already checked the URLs of:

```python
self.visited_dodgy_posts
```
> This means it does not have to go through its logic for the same post each time the method is run, saving compute resources.

**Messaging a user**

```python
message_user(self, user, msg_subject, msg_content)
```
> When this method is run, a private message is sent to the *user*, with the subject *msg_subject* and message content *msg_content*. This function is ordinarily used in the remove_dodgy_website_posts method, but can also be used as a standalone method.

**Checking a post for comments from a moderator**

```python
check_for_mod_comments(self):
```
> When this method is called, it iterates through the most recent comments made in the subreddit. It then checks if the author of the comment is one of the moderators provided in the [LIST_OF_MODERATORS] argument given when the object was instantiated. If it isn't, then the comment is left alone. If it is made by a moderator, then if the post has not previously been detected to have a moderator comment, then the bot makes a stickied comment on the post, outlining all the comments made my moderators on that post. If the post has been detected to have a moderator comment already, then the stickied comment will be edited to include the new comment made by the moderator. Here is an example screenshot:

[![MOD COMMENTS](https://snipboard.io/Kk4USo.jpg)]()

> To improve efficiency, each time the method is run, it stores the last batch of comments it went through in the instance variable: self.previous_comments. Then, when the method is run again, it checks to see if the new batch of comments contains any of the comments saved in memory from the previous batch it looked at. If any of the comments has been already seen, it skips it, and so avoids doing the same logic twice on the same comment, saving compute power.
> Also, the logic checks to see whether the comment has been posted on a post that has since been deleted, in which case, it is not necessary to consider this comment as the post cannot be seen on the subreddit. This saves from doing unnecessary computation.

**Starting the bot**

```python
start_cycle(self, dodgy_websites=True, new_posts_flairs=True, mod_comments=True)
```
> When this method is called, an infinite loop is set up to allow the bot to run forever. The arguments passed to the method determine which functions the bot will run. Setting the value to True (which is by default) will cause the methods to be run, and setting them to False will mean the methods won't be run. This gives the user a choice on which methods they would like their bot to run. This is also where the BANDWIDTH argument is used, as it defines the amount of time for which the bot will pause between running all of its functions again. The code to do this is as shown:
[![START CYCLE](https://snipboard.io/kgpw2t.jpg)]()

---

## FAQ

- **Will there be new features coming soon?**
    - Absolutely! If you think there is a feature that should be added, then let me know!

> Please feel free to tell me any questions you think should be put here to help other people in the future!
---

## Support

Reach out to me at one of the following places!

- Reddit at <a href="https://www.reddit.com/user/TheGeeezer" target="_blank">`TheGeeezer`</a>
- Twitter at <a href="https://twitter.com/tozzzer" target="_blank">`@tozzzer`</a>

> I'm really not expecting any donations, but if you are feeling in a very generous mood, any donations would be greatly appreciated!

> [![PAYPAL](https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-200px.png)](https://paypal.me/tompettit7)



## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
