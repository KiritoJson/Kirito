"""Twitter."""


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old and has 64 retweets.
    >Tweet2 is 3.12 hours old and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """
    tweets.sort(key=lambda tweet: tweet.retweets / tweet.time, reverse=True)

    return tweets[0]


def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.

    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    tweets.sort(key=lambda tweet: tweet.retweets, reverse=True)
    return tweets


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    import re

    new_list = [i for i in tweets if re.search(hashtag, i.content) is not None]

    return new_list


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    content_retweets = {}

    for tweet in tweets:  # Making dict {content1: retweets1, content2: retweets2, ... }
        content_retweets[tweet.content] = tweet.retweets

    import re
    import operator

    # Sorting dict by descending value (retweets)
    sorted_d = dict(sorted(content_retweets.items(), key=operator.itemgetter(1), reverse=True))

    regex = r"\B(\#[a-zA-Z]+\b)"

    hash_retweets = []  # Making list of hashtags
    for key, value in sorted_d.items():
        hashtag = re.findall(regex, key)  # Find all hashtags
        hashtag = list(dict.fromkeys(hashtag))  # Eliminate hashtag duplicates in same tweet
        if "#" not in key:
            pass
        else:
            hash_retweets.append(hashtag[0])

    return hash_retweets


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3]

    print(find_fastest_growing(tweets).user)  # -> "@elonmusk"

    filtered_by_popularity = sort_by_popularity(tweets)
    print(filtered_by_popularity[0].user)  # -> "@CIA"
    print(filtered_by_popularity[1].user)  # -> "@elonmusk"
    print(filtered_by_popularity[2].user)  # -> "@realDonaldTrump"

    filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags[0])  # -> "#heart"

    test_tweet2 = Tweet("@Teet", "Tere #B #A", 20, 1337)
    test_tweet1 = Tweet("@Mari", "Hello #A #B", 30, 1337)
    test_tweet3 = Tweet("@Agooo", "Python #C #C #C", 10, 2000)
    test_tweet4 = Tweet("@Cappy", "Orange", 10, 2000)
    test_tweets = [test_tweet1, test_tweet2, test_tweet3, test_tweet4]
    print([tweet for tweet in sort_hashtags_by_popularity(test_tweets)])
    # ['#A', '#B', '#C']
