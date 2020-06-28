import praw
import time

class RedditBot:
    def __init__(self, c_id, c_secret, user_agent, username, password, subreddit_name):
        self.client_id = c_id
        self.client_secret = c_secret
        self.user_agent = user_agent
        self.username = username
        self.password = password
        self.subreddit_name = subreddit_name
        self.visited_flaired_posts = []
        self.visited_dodgy_posts = []
        self.visited_mod_comments_posts = []
        self.dodgy_links = ['pornhub.com', 'brazzers.com', 'porn', 'xvideos.com']
        self.mod_names = ['tozzer7']
        self.post_mod_comments = {}
        self.previous_comments = []

        print('Saved credentials...')


    # This function looks through all the recent posts in the subreddit and checks if they have a flair. If they do, then the bot comments on the post to inform the user what they did wrong, and then hides the post.
    # Changes to do: Message user to alert them as well.
    def check_new_posts_flairs(self):
        reddit = praw.Reddit(client_id=self.client_id,
                    client_secret=self.client_secret,
                    user_agent=self.user_agent,
                    username=self.username,
                    password=self.password)

        sub = reddit.subreddit(self.subreddit_name)
        for submission in sub.new():
            if submission.id not in self.visited_flaired_posts:
                self.visited_flaired_posts.append(submission.id)
                if submission.link_flair_text is None:
                    print(submission, 'has no flair')
                    try:
                        submission.reply(str(submission.author)+', please may you flair your post when submitting. This post will be hidden and you will have to repost it with a flair.')
                        submission.hide()
                    except:
                        pass

    #This function looks through all the recent posts in the subreddit to check whether the url of the posts is from a blacklisted website. Blacklisted websites are recorded in the dodgy_links instance variable.
    def remove_dodgy_website_posts(self):
        reddit = praw.Reddit(client_id=self.client_id,
                    client_secret=self.client_secret,
                    user_agent=self.user_agent,
                    username=self.username,
                    password=self.password)

        sub = reddit.subreddit(self.subreddit_name)
        for submission in sub.new():
            if submission.id not in self.visited_dodgy_posts:
                self.visited_dodgy_posts.append(submission.id)
                for dodgy_link in self.dodgy_links:
                    if dodgy_link in submission.url:
                        self.message_user(submission.author.name, 'Your latest post...', 'Dear '+str(submission.author.name)+', \n Your latest post, called: **'+str(submission.title)+'** was from a url that is blacklisted from our subreddit. Therefore, the post has been removed. \n Please may we request that you refrain from posts from this website again in future. \n Thanks, \n the '+str(self.subreddit_name)+' mod team.')
                        submission.mod.remove()

    #This function allows the bot to message a particular user with arguments for the message subject and content.
    def message_user(self, user, msg_subject, msg_content):
        reddit = praw.Reddit(client_id=self.client_id,
                    client_secret=self.client_secret,
                    user_agent=self.user_agent,
                    username=self.username,
                    password=self.password)

        reddit.redditor(user).message(msg_subject, msg_content)

    #This function looks at all new comments to see if they are by a moderator of the subreddit. If they are, then a stickied comment is made by the bot highlighting the comments made by the moderator(s) on teh relevant post.
    def check_for_mod_comments(self):
        reddit = praw.Reddit(client_id=self.client_id,
                    client_secret=self.client_secret,
                    user_agent=self.user_agent,
                    username=self.username,
                    password=self.password)

        sub = reddit.subreddit(self.subreddit_name)
        
        past_comments = []
        #change the limit depending on the number of comments the subreddit gets
        for comment in sub.comments(limit=15):
            past_comments.append(comment)
            if comment in self.previous_comments:
                print('comment already seen')
                pass
            else:
                if comment.submission.author != '[Deleted]':
                    if 'Here is a list of comments made my moderators of this subreddit: ' not in comment.body:
                        if comment.author in self.mod_names:
                            if comment.submission.id not in self.post_mod_comments:
                                starter = 'Here is a list of comments made my moderators of this subreddit: \n '
                                first_comment = '* '+str(comment.author)+': '+str(comment.body)+'\n'
                                bot_reply = starter+first_comment
                                self.post_mod_comments[comment.submission.id] = [first_comment]
                                actual_bot_reply = comment.submission.reply(bot_reply)
                                actual_bot_reply.mod.distinguish(sticky=True)
                                self.post_mod_comments[comment.submission.id].append(actual_bot_reply)

                            else:
                                print('seen this post already')
                                try:
                                    bot_reply = self.post_mod_comments[comment.submission.id][0]
                                    starter = 'Here is a list of comments made my moderators of this subreddit: \n '
                                    self.post_mod_comments[comment.submission.id][1].edit(starter + bot_reply + '* '+str(comment.author)+': '+str(comment.body)+'\n')
                                    new_bot_reply = bot_reply + '* '+str(comment.author)+': '+str(comment.body)+'\n'
                                    self.post_mod_comments[comment.submission.id][0] = new_bot_reply
                                except Exception as e:
                                    pass
        self.previous_comments = past_comments

    def start_cycle(self):
        self.started = True
        while self.started is True:
            print('starting...')
            self.check_for_mod_comments()
            print('sleeping...')
            time.sleep(60)
