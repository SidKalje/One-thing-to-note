import datetime
from newsapi import NewsApiClient
from technology.config import NEWS_API_KEY

api = NewsApiClient(api_key=f"{NEWS_API_KEY}")


def get_top_headlines():
    th = api.get_top_headlines(category="technology", language="en", country="us")
    return th


preferred_sources = [
    "techcrunch",
    "the-verge",
    "wired",
    "ars-technica",
    "engadget",
    "techradar",
    "the-next-web",
]
# top_headlines = get_top_headlines()


def get_everything_headlines():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=3)).strftime(
        "%Y-%m-%d"
    )
    source_headlines = api.get_everything(
        q="technology",
        # sources="techcrunch, the-verge, wired, ars-technica, engadget, techradar, the-next-web",
        language="en",
        sort_by="relevancy",
        from_param=(yesterday),
    )
    source_headline_titles = [
        article["title"] for article in source_headlines["articles"]
    ]
    return source_headline_titles, source_headlines


def process_headlines(source_headlines):
    processed_headlines = {}
    i = 0
    for article in source_headlines["articles"]:
        processed_headlines[i] = [
            article["title"],
            article["url"],
            article["source"]["name"],
            article["urlToImage"],
        ]
        i += 1
    return processed_headlines
