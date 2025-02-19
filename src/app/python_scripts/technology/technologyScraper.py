import newspaper
import datetime
from newsapi import NewsApiClient
from openai import OpenAI
from dotenv import load_dotenv
import os

# use news api to get the top headlines
# choose 10 reliable sources for politics
# find out how to get articles from the sources using newspaper3k
# get top 3 headlines
# ask AI to pick the better headline from both
# ask AI to summarize the article
# Link summary and python code to the frontend

load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

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


# write code to get just the names of the headlines in an array
# top_headline_titles = [
#     article["title"]
#     for article in top_headlines["articles"]
#     if article["source"]["id"] in preferred_sources
# ]
def get_everything_headlines():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(
        "%Y-%m-%d"
    )
    source_headlines = api.get_everything(
        q="technology OR tech OR innovation OR 'artificial intelligence' OR AI OR 'machine learning' OR cybersecurity OR 'cloud computing' OR 'big data' OR blockchain OR 'internet of things' OR IoT OR 'virtual reality' OR VR OR 'augmented reality' OR AR OR 'quantum computing' OR startups",
        # sources="techcrunch, the-verge, wired, ars-technica, engadget, techradar, the-next-web",
        language="en",
        sort_by="relevancy",
        from_param=(yesterday),
    )
    source_headline_titles = [
        article["title"] for article in source_headlines["articles"]
    ]
    return source_headline_titles, source_headlines


source_headline_titles, source_headlines = get_everything_headlines()
# source_headlines = get_top_headlines()
# print(source_headlines)
# process the headlines into a dictionary
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

# prompt to gpt
prompt = (
    "I have the following headlines for today's technology news. "
    "Please choose the best and most technologically informative headline from the list and provide only its index (starting at 1) along with a short explanation.\n\n"
)

for i in range(len(processed_headlines.keys())):
    prompt += f"{i+1}. {processed_headlines[i][0]}\n"
prompt += "\nWhich headline is the best and why?"

# print(len(prompt))
# print(prompt)
# chatgpt call
client = OpenAI(api_key=f"{OPEN_AI_API_KEY}")
developer_msg = (
    " You are a highly discerning news editor with a deep understanding of what makes a headline both engaging and informative. I have a list of headlines for today's [insert topic or category] news, "
    + "and your task is to select the best one based on the following criteria:"
    + "1. Clarity and Conciseness: The headline should be clear, succinct, and immediately convey the main point of the story."
    + "2. Relevance and Timeliness: It should capture a significant, timely news event that matters to the audience."
    + "3. Engagement and Entertainment Value: The headline should be written in a way that is both engaging and entertaining, sparking curiosity or emotional interest."
    + "4. Originality and Impact: It should stand out from the rest by offering a unique or impactful angle on the news."
)

# print(prompt)
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"{developer_msg}"},
        {"role": "user", "content": prompt},
    ],
)

headline_number = response.choices[0].message.content
# print("Selected Headline Number:", headline_number)
try:
    selected_index = (
        int("".join(filter(str.isdigit, headline_number.split()[0]))) - 1
    )  # convert to 0-based index
    # print(selected_index)
    selected_article = processed_headlines[selected_index]
    # print("Selected Headline:", selected_article[0])
    # print("URL:", selected_article[1])
except Exception as e:
    print("Error parsing selected index:", e)

try:
    article = newspaper.article(selected_article[1])
except Exception as e:
    print("Error fetching article:", e)
# print(article.title)
# print(article.text)
# print(selected_article[3])

summary_prompt = (
    "Summarize the text delimited by triple quotes in 130 words at maximum.\n\n'''"
)

summary_prompt += "Headline: " + article.title + "\n\nArticle:" + article.text + "'''"
# print(summary_prompt)

developer_msg_summary = (
    "You are an expert news summarizer tasked with condensing an article into a concise summary of 120 words or fewer. Please follow these instructions:\n\n"
    "1. Read and comprehend the full article text provided below.\n"
    "2. Identify the most important points, including the main event or argument, key supporting details, and any conclusions or implications.\n"
    "3. Create a summary that captures the essence of the article clearly and concisely.\n"
    "4. Ensure your summary is written in plain language, is logically organized, and remains faithful to the original article's meaning.\n"
    "5. Do not add opinions or extraneous commentary—only include factual information from the article.\n"
    "6. Limit your summary to 130 words or less."
)

article_summary = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"{developer_msg_summary}"},
        {"role": "user", "content": summary_prompt},
    ],
)

print(article_summary.choices[0].message.content)
