import praw
import time


class RedditBot:
    def __init__(self, c_id, c_secret, user_agent, username, password, subreddit_name, dodgy_links, mod_names, swear_words, bandwidth='medium'):
        if bandwidth == 'medium':
            self.bandwidth = 100
        elif bandwidth == 'low':
            self.bandwidth = 150
        elif bandwidth == 'high':
            self.bandwidth = 50

        self.client_id = c_id
        self.client_secret = c_secret
        self.user_agent = user_agent
        self.username = username
        self.password = password
        self.subreddit_name = subreddit_name
        self.visited_flaired_posts = []
        self.visited_dodgy_posts = []
        self.visited_mod_comments_posts = []
        self.dodgy_links = dodgy_links
        self.mod_names = mod_names
        self.post_mod_comments = {}
        self.previous_comments = []
        self.swear_words = swear_words
        self.scanned_comments = []

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
                    try:
                        submission.reply(
                            f"{submission.author}, please may you flair your post when submitting. This post will be hidden and you will have to repost it with a flair.")
                        submission.mod.remove()
                    except:
                        pass

    # This function looks through all the recent posts in the subreddit to check whether the url of the posts is from a blacklisted website. Blacklisted websites are recorded in the dodgy_links instance variable.
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
                        try:
                            self.message_user(submission.author.name, 'Your latest post...',
                                              f"Dear {submission.author.name}, \n Your latest post, called: **{submission.title}** was from a url that is blacklisted from our subreddit. Therefore, the post has been removed. \n Please may we request that you refrain from posts from this website again in future. \n Thanks, \n the {self.subreddit_name} mod team.")
                            submission.mod.remove()
                        except:
                            pass

    # This function allows the bot to message a particular user with arguments for the message subject and content.
    def message_user(self, user, msg_subject, msg_content):
        reddit = praw.Reddit(client_id=self.client_id,
                             client_secret=self.client_secret,
                             user_agent=self.user_agent,
                             username=self.username,
                             password=self.password)

        try:
            reddit.redditor(user).message(msg_subject, msg_content)
        except:
            pass

    # This function looks at all new comments to see if they are by a moderator of the subreddit. If they are, then a stickied comment is made by the bot highlighting the comments made by the moderator(s) on teh relevant post.
    def check_for_mod_comments(self):
        reddit = praw.Reddit(client_id=self.client_id,
                             client_secret=self.client_secret,
                             user_agent=self.user_agent,
                             username=self.username,
                             password=self.password)

        sub = reddit.subreddit(self.subreddit_name)

        past_comments = []
        # change the limit depending on the number of comments the subreddit gets
        for comment in sub.comments(limit=15):
            past_comments.append(comment)
            if comment in self.previous_comments:
                pass
            else:
                if comment.submission.author != '[Deleted]':
                    if 'Here is a list of comments made my moderators of this subreddit: ' not in comment.body:
                        if comment.author in self.mod_names:
                            if comment.submission.id not in self.post_mod_comments:
                                starter = 'Here is a list of comments made my moderators of this subreddit: \n '
                                first_comment = f"* {comment.author}: {comment.body}\n"
                                bot_reply = f"{starter}{first_comment}"
                                self.post_mod_comments[comment.submission.id] = [
                                    first_comment]
                                try:
                                    actual_bot_reply = comment.submission.reply(
                                        bot_reply)
                                    actual_bot_reply.mod.distinguish(
                                        sticky=True)
                                except:
                                    pass
                                self.post_mod_comments[comment.submission.id].append(
                                    actual_bot_reply)

                            else:
                                try:
                                    bot_reply = self.post_mod_comments[comment.submission.id][0]
                                    starter = 'Here is a list of comments made my moderators of this subreddit: \n '
                                    self.post_mod_comments[comment.submission.id][1].edit(
                                        f"{starter}{bot_reply}* {comment.author}: {comment.body}\n")
                                    new_bot_reply = f"{bot_reply}* {comment.author}: {comment.body}\n"
                                    self.post_mod_comments[comment.submission.id][0] = new_bot_reply
                                except Exception as e:
                                    pass
        self.previous_comments = past_comments

    # This functions scans the latest comments to see if they contain a swear word from the list of swear words provided to the object.
    def censor_comments(self):
        reddit = praw.Reddit(client_id=self.client_id,
                             client_secret=self.client_secret,
                             user_agent=self.user_agent,
                             username=self.username,
                             password=self.password)

        sub = reddit.subreddit(self.subreddit_name)

        past_comments = []
        for comment in sub.comments(limit=15):
            past_comments.append(comment)
            if comment in self.scanned_comments:
                pass
            else:
                for swear in self.swear_words:
                    if swear in comment.body:
                        try:
                            self.message_user(comment.author.name, 'Inappropriate Language',
                                              f"Dear {comment.author}, \n Your comment, \n \"**{comment.body}**\" \n contains the word {swear}, which is banned on this subreddit. Therefore, the comment has been removed. \n Please may we request that you refrain from using this language in future. \n Thanks, \n the {self.subreddit_name} mod team.")
                            comment.mod.remove()
                            break
                        except:
                            pass

        self.scanned_comments = past_comments

    # This is the function used to allow the bot to run every self.bandwidth seconds.
    def start_cycle(self, dodgy_websites=True, new_posts_flairs=True, mod_comments=True, censor_comments=True):
        self.started = True
        while self.started is True:
            if dodgy_websites is True:
                self.remove_dodgy_website_posts()
            if new_posts_flairs is True:
                self.check_new_posts_flairs()
            if mod_comments is True:
                self.check_for_mod_comments()
            if censor_comments is True:
                self.censor_comments()

            time.sleep(self.bandwidth)
