import articleLinks
import time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--blink-settings=imagesEnabled=false")
options.add_argument("--headless=new")


# Define a function to fetch an article and extract its HTML text.
# def fetch_article(url):
#     # Set up Chrome options (adjust as needed)
#     # Create a new Chrome instance for this thread
#     driver = webdriver.Chrome(options=options)
#     t = time.time()
#     driver.set_page_load_timeout(20)
#     html_text = ""

#     try:
#         print("Fetching ", url)
#         driver.get(url)
#     except TimeoutException:
#         driver.execute_script("window.stop();")

#     print(f"Page loaded in {time.time() - t} seconds")

#     t = time.time()
#     try:
#         print("locating elements")
#         article_bodies = WebDriverWait(driver, 50).until(
#             EC.presence_of_all_elements_located(
#                 (
#                     By.CSS_SELECTOR,
#                     "div.article-body p",
#                 )
#             )
#         )


#         for article_body in article_bodies:
#             html_text = html_text + article_body.text
#         print(f"Page loaded in {time.time() - t} seconds")
#         # Return the URL and the extracted text
#         return url, html_text
#     finally:
#         driver.quit()
def fetch_article(url):
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(50)
    html_text = ""
    t = time.time()

    try:
        print("Fetching ", url)
        driver.get(url)
        # Wait until the article-body div appears
        WebDriverWait(driver, 80).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.article-body"))
        )
        # Once it appears, stop further page loading
        driver.execute_script("window.stop();")
        time.sleep(1)
    except TimeoutException:
        driver.execute_script("window.stop();")

    print(f"Page loaded in {time.time() - t} seconds")

    t = time.time()
    try:
        print("Locating article paragraphs")
        article_bodies = WebDriverWait(driver, 80).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.article-body p"))
        )
        for article_body in article_bodies:
            html_text += article_body.text + "\n"
        print(f"Article content extracted in {time.time() - t} seconds")
        return url, html_text
    finally:
        driver.quit()


# Use ThreadPoolExecutor to process multiple articles concurrently.
results = {}
stories = articleLinks.fetch_articles()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # Submit a fetch task for each URL
    future_to_url = {executor.submit(fetch_article, url): url for url in stories}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            result_url, article_html = future.result()
            results[result_url] = article_html
            print(f"Fetched {result_url} ({len(article_html)} characters)")

        except Exception as exc:
            print(f"Error fetching {url}: {exc}")

# At this point, 'results' is a dictionary mapping each URL to its HTML content.
