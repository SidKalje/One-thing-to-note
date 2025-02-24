# from technology.news_api_client import get_everything_headlines, process_headlines
# from technology.headline_selector import build_prompt, select_headline
# from technology.article_processor import process_article
# from newsapi import NewsApiClient
# from dotenv import load_dotenv
# import os

# load_dotenv()


# def run_workflow():
#     # Get headlines from the news API
#     source_headline_titles, source_headlines = get_everything_headlines()
#     processed_headlines = process_headlines(source_headlines)
#     # Build the prompt for headline selection
#     prompt = build_prompt(processed_headlines)

#     developer_msg = (
#         " You are a highly discerning news editor with a deep understanding of what makes a headline both engaging and informative. I have a list of headlines for today's [insert topic or category] news, "
#         + "and your task is to select the best one based on the following criteria:"
#         + "1. Clarity and Conciseness: The headline should be clear, succinct, and immediately convey the main point of the story."
#         + "2. Relevance and Timeliness: It should capture a significant, timely news event that matters to the audience."
#         + "3. Engagement and Entertainment Value: The headline should be written in a way that is both engaging and entertaining, sparking curiosity or emotional interest."
#         + "4. Originality and Impact: It should stand out from the rest by offering a unique or impactful angle on the news."
#     )

#     # Use the headline selector to choose the best headline
#     selected_article = select_headline(prompt, developer_msg, processed_headlines)

#     if selected_article is None:
#         print("Error selecting article.")
#         return None, None

#     # Process the selected article to generate a summary
#     summary = process_article(selected_article)
#     print("Summary: ", summary)

#     return summary, selected_article


# def main():
#     try:
#         summary, article = run_workflow()
#         print(summary)
#         print(article)
#     except Exception as e:
#         print("Error running workflow:", e)


# # if __name__ == "__main__":
# #     main()

from technology.news_api_client import get_everything_headlines, process_headlines
from technology.headline_selector import build_prompt, select_headline
from technology.article_processor import process_article
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()


def run_workflow(category="technology"):
    # Get headlines from the news API
    source_headline_titles, source_headlines = get_everything_headlines(category)
    processed_headlines = process_headlines(source_headlines)

    developer_msg = (
        " You are a highly discerning news editor with a deep understanding of what makes a headline both engaging and informative. I have a list of headlines for today's [insert topic or category] news, "
        + "and your task is to select the best one based on the following criteria:"
        + "1. Clarity and Conciseness: The headline should be clear, succinct, and immediately convey the main point of the story."
        + "2. Relevance and Timeliness: It should capture a significant, timely news event that matters to the audience."
        + "3. Engagement and Entertainment Value: The headline should be written in a way that is both engaging and entertaining, sparking curiosity or emotional interest."
        + "4. Originality and Impact: It should stand out from the rest by offering a unique or impactful angle on the news."
    )

    while True:
        print("Trying")
        if not processed_headlines:
            print("No accessible headlines remain.")
            raise Exception("No headlines available.")

        # Build the prompt for headline selection using the current processed_headlines
        try:
            prompt = build_prompt(processed_headlines, category)
            print("Prompt: ", prompt)
        except Exception as e:
            raise Exception("Error building prompt:", e)

        # Use the headline selector to choose the best headline

        selected_article = select_headline(prompt, developer_msg, processed_headlines)
        if selected_article is None:
            print("Error selecting article.")
            raise Exception("Error selecting article.")

        # Process the selected article to generate a summary
        summary = process_article(selected_article)

        # If summary is successfully generated, return it along with the selected article
        if summary and summary.strip():
            print("Returned summary: ", summary)
            print("Returned article: ", selected_article)
            return summary, selected_article
        else:
            print("Failed headline, trying again.")
            # Remove the failed headline by matching its title (assumed to be the first element)
            processed_headlines = {
                key: value
                for key, value in processed_headlines.items()
                if value[0].strip().lower() != selected_article[0].strip().lower()
            }
            print("Remaining headlines", processed_headlines)


def main():
    try:
        summary, article = run_workflow()
        print(summary)
        print(article)
    except Exception as e:
        print("Error running workflow:", e)


if __name__ == "__main__":
    main()
