import praw
import json
import time
import win10toast
client_id = "REDDIT_CLIENT_ID"
client_secret = "REDDIT_SECRET"
user_agent = "APPNAME"
username = "USERNAME"
password = "PASSWORD"

def create_reddit_object():
    reddit = praw.Reddit(client_id = client_id,
    client_secret= client_secret,
    username = username, password = password, user_agent = user_agent)

    return reddit

def findPrice(post_body):
    priceIndex = post_body.find('$')
    print(post_body[priceIndex:priceIndex+4])
    return 0

toaster = win10toast.ToastNotifier()

if __name__ == '__main__':
    search_limit = 25
    print('Enter subreddit to watch: ')
    userSubreddit = input()
    print('Enter term to search for: ')
    searchTarget = input()
    while True:
        reddit = create_reddit_object()
        targetSub = reddit.subreddit(userSubreddit)
        new_posts = targetSub.new(limit=search_limit)

        for submission in new_posts:
            if not submission.stickied:
                if submission.is_self:
                    if (submission.title.lower().find(searchTarget) > 0):
                        if(time.time() - submission.created_utc < 62):
                            toaster.show_toast("New GameSale Post!", submission.title)
                            print('TITLE: {}, Upvotes: {}'.format(submission.title, submission.ups))
                        else:
                            print("OLD POST:", 'TITLE: {}, Upvotes: {}'.format(submission.title, submission.ups))

        start_time = time.time()
        waitingPeriod = 60
        while True:
                current_time = time.time()
                elapsed_time = current_time - start_time
                if elapsed_time > waitingPeriod:
                    print("Checking most recent posts...")
                    break


