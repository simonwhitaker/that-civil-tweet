# Introduction

On 24 May, 2020, a rogue staffer posted a [highly critical tweet](https://www.theguardian.com/politics/2020/may/24/can-you-imagine-having-to-work-with-these-truth-twisters) on the UK Civil Service twitter account. Ever since, [@ThatCivilTweet](https://twitter.com/ThatCivilTweet) has been tweeting the same text twice a day, every day, to keep it fresh in our minds.

The code in this repository queries the Twitter API for the public stats (e.g. like counts) for every tweet from the @ThatCivilTweet account, then offers a Jupyter Notebook for visualising the data in an interactive plot.

# Getting started

To run the code, first register for the [Twitter API](https://developer.twitter.com/en/docs/platform-overview) and generate a bearer token, then export it to your environment:

```
export TWITTER_API_TOKEN=<your bearer token here>
```

Now run the code.

```
poetry install
poetry run python3 main.py > data.csv
```

Now open viz.ipynb and run it to generate an interactive plot. If you've never used a .ipynb file before, the easiest way to get started is to open it in VS Code with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) installed.
