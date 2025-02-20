from openai import OpenAI
from technology.config import OPEN_AI_API_KEY

client = OpenAI(api_key=f"{OPEN_AI_API_KEY}")


def build_prompt(processed_headlines):
    prompt = (
        "I have the following headlines for today's technology news. "
        "Please choose the best and most technologically informative headline from the list and "
        "provide only its index (starting at 1) along with a short explanation. DO NOT put anything but the index (starting at 1). "
        "For example, your output should look like this: 4. <HeadlineTextHere>. Here are the headlines:\n\n"
    )
    for idx, headline in enumerate(processed_headlines.values(), start=1):
        prompt += f"{idx}. {headline[0]}\n"
    prompt += "\nWhich headline is the best and why?"
    return prompt


def select_headline(prompt, developer_msg, processed_headlines):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": developer_msg},
            {"role": "user", "content": prompt},
        ],
    )
    headline_number = response.choices[0].message.content
    print("Headline number: ", headline_number)
    try:
        # Extract the number, convert to 0-based index.
        selected_index = (
            int("".join(filter(str.isdigit, headline_number.split()[0]))) - 1
        )
        # Convert the dictionary to a list so that the ordering matches the prompt.
        headlines_list = list(processed_headlines.values())
        selected_article = headlines_list[selected_index]
        print("Selected article: ", selected_article)
        return selected_article
    except Exception as e:
        print("Error parsing selected index:", e)
        return None
