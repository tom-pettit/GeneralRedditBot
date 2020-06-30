# Reddit Bot Class

**This is a class that can be used to create multiple different reddit bots.**

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org) 
[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger)

## Table of Contents 
- [Installation](#installation)
- [Setup](#setup)
- [Features](#features)
- [FAQ](#faq)
- [License](#license)


---

## Installation

- To be done


### Setup
> Before you can use this class, you have to have created a bot associated to a reddit account. I have written a guide on how to do this: https://github.com/tozzzer/CreatingARedditBotGuide 

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

---

## Features
> There are many different methods that each RedditBot object can access

- The first function is:

```python
check_new_posts_flair(self) 
```
> When this method is run, it collects the newest posts to the subreddit. It then checks if these new posts have flairs. If they do, it leaves the post alone. However, if the post has no flair, the bot comments on the post to let the user know that they need to flair their post next time, and then it automatically makes the post hidden.

> To maximise efficiency, an instance object is used to save the ID of posts that the bot has checked for a flair:

```python
self.visited_flaired_posts
```

> This means that when the bot checks the newest posts each time the method is called, it won't go through all its logic twice for the same post, as it saves the IDs of previously checked posts, and doesn't fulfill its logic if it has seen a post's ID before.


## Usage (Optional)
## Documentation (Optional)
## Tests (Optional)

- Going into more detail on code and technologies used
- I utilized this nifty <a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet" target="_blank">Markdown Cheatsheet</a> for this sample `README`.

---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/joanaz/HireDot2.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/joanaz/HireDot2/compare/" target="_blank">`https://github.com/joanaz/HireDot2/compare/`</a>.

---

## Team

> Or Contributors/People

| <a href="http://fvcproductions.com" target="_blank">**FVCproductions**</a> | <a href="http://fvcproductions.com" target="_blank">**FVCproductions**</a> | <a href="http://fvcproductions.com" target="_blank">**FVCproductions**</a> |
| :---: |:---:| :---:|
| [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com)    | [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) | [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com)  |
| <a href="http://github.com/fvcproductions" target="_blank">`github.com/fvcproductions`</a> | <a href="http://github.com/fvcproductions" target="_blank">`github.com/fvcproductions`</a> | <a href="http://github.com/fvcproductions" target="_blank">`github.com/fvcproductions`</a> |

- You can just grab their GitHub profile image URL
- You should probably resize their picture using `?s=200` at the end of the image URL.

---

## FAQ

- **How do I do *specifically* so and so?**
    - No problem! Just do this.

---

## Support

Reach out to me at one of the following places!

- Website at <a href="http://fvcproductions.com" target="_blank">`fvcproductions.com`</a>
- Twitter at <a href="http://twitter.com/fvcproductions" target="_blank">`@fvcproductions`</a>
- Insert more social links here.

---

## Donations (Optional)

- You could include a <a href="https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png" target="_blank">Gratipay</a> link as well.

[![Support via Gratipay](https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png)](https://gratipay.com/fvcproductions/)


---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2015 © <a href="http://fvcproductions.com" target="_blank">FVCproductions</a>.
