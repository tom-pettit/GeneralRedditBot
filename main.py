import praw

class RedditBot:
    def __init__(self, c_id, c_secret, user_agent, username, password, subreddit_name):
        self.client_id = c_id
        self.client_secret = c_secret
        self.user_agent = user_agent
        self.username = username
        self.password = password
        self.subreddit_name = subreddit_name
        self.visited_posts = []
        self.dodgy_links = ['pornhub.com', 'brazzers.com', 'porn', 'xvideos.com']

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
            if submission.id not in self.visited_posts:
                self.visited_posts.append(submission.id)
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
            for dodgy_link in self.dodgy_links:
                if dodgy_link in submission.url:
                    submission.reply(str(submission.author) + ', this post is from a url that is blacklisted on this subreddit. Thus, this post has been removed.')
                    submission.delete()

