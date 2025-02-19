import newspaper
from openai import OpenAI
from technology.config import OPEN_AI_API_KEY


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
        "You are an expert news summarizer tasked with condensing an article into a concise summary of 150 words or fewer in an easy-to-read format. "
        "The person who will be reading this does not read news often and has a short attention span. You have to make it captivating. "
        "Please format your summary entirely using valid HTML, including <strong> for bold headings and <ul>/<li> for bullet points. "
        "Do not wrap your output in triple backticks or any markdown formatting markers(like **)—return the raw HTML only. "
        "Please follow these instructions: "
        "1. Structure your summary using ONE to TWO bullet points to break down the main points, but ensure that the overall summary remains cohesive and flows naturally. "
        "2. Bold key phrases or keywords in each bullet point to emphasize major themes. "
        "3. Keep the overall summary concise, limiting it to 150 words or fewer. "
        "4. Include only the essential facts of the article, ensuring the information is clear and logically organized. "
        "5. Do not include any opinions or extraneous commentary."
        "6. Add one blank line separating each list element(ul/li)."
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
