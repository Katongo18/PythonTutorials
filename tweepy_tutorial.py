import tweepy
from tweepy import OAuthHandler
import csv

CONSUMER_KEY = "jy7S717iGol86vUw1dWsvLzVk"
CONSUMER_SECRET = "gaktUNFMjiDYLqyzpxiDpTA2hYXAeeIwIOokBTyhoAoEVJQ19J"
ACCESS_KEY = "3477517995-xWKJ5HhxizLNR2tChqNQqTOZeXrgaQ4lWHaO32A"
ACCESS_SECRET = "nRD5Bq5KDifIyAQrS773WcVOkYtHAlxSMuvtohtl1mRzH"
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)  # wait_on_rate_limit = True

mentions = api.mentions_timeline()
(mentions[0].__dict__.keys())
# print(mentions[0].text) gets the first(key) value in the mentions value and makes it readable with .text
pub = api.home_timeline()
# for tweet in pub:
#   print(tweet)  #Prints tweets on my timeline
user = api.get_user('TYasinti')
# user2 = api.get_user('MumbaRyan')

# user = api.get_user('twitter')
# print(user.followers_count)
# print(user2.followers_count)
# print(user.screen_name)
# for friend in tweepy.Cursor(api.friends).items():
#         Process the friend here
#    with open('out.txt', 'w') as file:
#        file.write(friend)
# for status in tweepy.Cursor(api.friends_timeline).items(200):
# Process the status here
#   print(status)

# for friend in user.friends():
#    pass
#     print(friend.screen_name)
# print(timeit.timeit('"-".join(str(n) for n in range(10*100))', number=10000))

a = []
for status in tweepy.Cursor(api.user_timeline).items(10):
    with open('out2.csv', 'a') as file:
        csv_w = csv.writer(file)
        # csv_w.writerow([status.text])
#       print(csv_w)

# Open/Create a file to append data

csvFile = open('dmfz_28.csv', 'a')
# Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search, q="#DateMyFamilyZambia", count=10,
                           lang="en",
                           since="2019-03-03").items(10):
    #    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    for tweet1 in tweepy.Cursor(api.search, q="#DateMyFamilyZambia", count=10, lang="en", since="2019-03-28").items(10):

                                # print(tweet1.created_at, tweet1.text)

        csvWriter.writerow([tweet1.created_at, tweet1.text.encode('utf-8')])
