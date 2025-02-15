import newspaper
from openai import OpenAI
from config import OPEN_AI_API_KEY


def process_article(selected_article):
    try:
        article = newspaper.article(selected_article[1])
    except Exception as e:
        print("Error fetching article:", e)
        return None
    summary_prompt = (
        "Summarize the text delimited by triple quotes in 130 words at maximum.\n\n'''"
    )
    summary_prompt += (
        "Headline: " + article.title + "\n\nArticle:" + article.text + "'''"
    )
    developer_msg_summary = (
        "You are an expert news summarizer tasked with condensing an article into a concise summary of 120 words or fewer. Please follow these instructions:\n\n"
        "1. Read and comprehend the full article text provided below.\n"
        "2. Identify the most important points, including the main event or argument, key supporting details, and any conclusions or implications.\n"
        "3. Create a summary that captures the essence of the article clearly and concisely.\n"
        "4. Ensure your summary is written in plain language, is logically organized, and remains faithful to the original article's meaning.\n"
        "5. Do not add opinions or extraneous commentary—only include factual information from the article.\n"
        "6. Limit your summary to 130 words or less."
    )
    client = OpenAI(api_key=f"{OPEN_AI_API_KEY}")
    article_summary = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"{developer_msg_summary}"},
            {"role": "user", "content": summary_prompt},
        ],
    )
    return article_summary.choices[0].message.content
