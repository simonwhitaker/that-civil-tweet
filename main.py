import json
import os

import requests

expected_content = (
    "Arrogant and offensive. Can you imagine having to work with these truth twisters?"
)
account_id = 1264862081301520384  # @ThatCivilTweet
url = f"https://api.twitter.com/2/users/{account_id}/tweets"
token = os.environ.get("TWITTER_API_TOKEN")
headers = {"Authorization": f"Bearer {token}"}

# CSV header
print("id,timestamp,likes,retweets")

# until_id
earliest_seen_tweet_id = None
data = []

querystring = {"tweet.fields": "public_metrics,created_at", "max_results": "100"}

while earliest_seen_tweet_id is None or len(data) < 100:
    if earliest_seen_tweet_id:
        querystring["until_id"] = earliest_seen_tweet_id
    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    tweets = data.get("data", [])
    if len(tweets) == 0:
        break

    earliest_seen_tweet_id = tweets[-1]["id"]

    # Filter out any tweets that aren't the usual content, e.g. replies,
    # retweets, etc
    tweets = filter(lambda t: t["text"] == expected_content, tweets)

    for tweet in tweets:
        print(
            ",".join(
                [
                    tweet["id"],
                    tweet["created_at"],
                    str(tweet["public_metrics"]["like_count"]),
                    str(tweet["public_metrics"]["retweet_count"]),
                ]
            )
        )
