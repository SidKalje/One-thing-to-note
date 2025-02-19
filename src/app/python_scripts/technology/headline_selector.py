from openai import OpenAI
from technology.config import OPEN_AI_API_KEY

client = OpenAI(api_key=f"{OPEN_AI_API_KEY}")


def build_prompt(processed_headlines):
    prompt = (
        "I have the following headlines for today's technology news. "
        "Please choose the best and most technologically informative headline from the list and provide only its index (starting at 1) along with a short explanation.\n\n"
    )
    for i in range(len(processed_headlines.keys())):
        prompt += f"{i+1}. {processed_headlines[i][0]}\n"
    prompt += "\nWhich headline is the best and why?"
    return prompt


def select_headline(prompt, developer_msg, processed_headlines):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"{developer_msg}"},
            {"role": "user", "content": prompt},
        ],
    )
    headline_number = response.choices[0].message.content
    try:
        selected_index = (
            int("".join(filter(str.isdigit, headline_number.split()[0]))) - 1
        )  # convert to 0-based index
        selected_article = processed_headlines[selected_index]
        return selected_article
    except Exception as e:
        print("Error parsing selected index:", e)
        return None
