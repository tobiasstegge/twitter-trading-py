from tweepy import API, OAuthHandler, TweepError


class Twitter:
    def __init__(self):
        self.API_KEY = ''
        self.API_SECRET_KEY = ''
        self.ACCESS_TOKEN = ''
        self.ACCESS_TOKEN_SECRET = ''

        try:
            auth = OAuthHandler(self.API_KEY, self.API_SECRET_KEY)
            auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)

            self.client = API(auth)

        except TweepError as e:
            print(e)
        else:
            print(f'Success! You are connected as {self.client.me().screen_name}')

    def get_last_tweet(self):
        elons_twitter = self.client.get_user('elonmusk')
        tweet = self.client.user_timeline(id=elons_twitter.id_str, count=1)
        print(tweet[0].text)


if __name__ == '__main__':
    Twitter().get_last_tweet()

