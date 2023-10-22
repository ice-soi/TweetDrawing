import random
from django.shortcuts import render
import tweepy
 
def index(request):
    
    consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
    consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
    access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
    access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
    bearer_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"

    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    client = tweepy.Client(bearer_token    = bearer_token,
                        consumer_key    = consumer_key,
                        consumer_secret = consumer_secret,
                        access_token    = access_token,
                        access_token_secret = access_token_secret,
                        )

    #tweetを取得
    screen_name = "" #取得したいユーザーのユーザーIDを代入
    # tweets = api.user_timeline(screen_name = screen_name)

    targetId = "ターゲットのIDを設定"

    users = client.get_retweeters(id=int(targetId)).data

    count = 1
    # 結果加工
    rt_users = []
    if users != None:
        for i in range(len(users)):
            username = users[i].username
            if username != "除外したいID":
                obj = {}
                obj["no"]       = count
                obj["user_id"]  = users[i].id
                obj["name"]     = users[i].name
                obj["username"] = users[i].username    
                rt_users.append(obj)
                count += 1
    else:
        rt_users.append("")

    quoteTweets = client.get_quote_tweets(id=int(targetId), expansions=["author_id"], user_fields=["username"])

    if quoteTweets != None:
            obj = {}
            obj["no"]       = count
            obj["user_id"]  = quoteTweets.includes["users"][0].id
            obj["name"]     = quoteTweets.includes["users"][0].name
            obj["username"] = quoteTweets.includes["users"][0].username
            rt_users.append(obj)
            count += 1
    else:
        rt_users.append("")

    winners = []
    numbers = []
    index   = 0
    while len(numbers) < 3:
        no = random.randint(0, count - 2)
        if not no in numbers:
            user = rt_users[no]
            winner = {}
            winner["count"] = index
            winner["no"]    = user['no']
            winner["name"]  = user['name']
            winners.append(winner)
            numbers.append(no)
            index += 1

    return render(request, 'index.html', {'rt_users' :rt_users, 'winners' :winners })