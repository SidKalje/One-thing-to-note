from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import threading


def fetch_articles():
    # run chrome headless
    options = Options()

    # stop image rendering
    options.add_argument("--blink-settings=imagesEnabled=false")

    # set the options to use Chrome in headless mode
    options.add_argument("--headless=new")

    url = "https://www.espn.com/"
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(40)
    t = time.time()

    try:
        driver.get(url)
    except TimeoutException:
        driver.execute_script("window.stop();")

    print(f"Page loaded in {time.time() - t} seconds")

    # headlines = driver.find_element(
    #     By.CSS_SELECTOR, "div.headlineStack.top-headlines ul.headlineStack__list"
    # )

    headlines = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.headlineStack.top-headlines ul.headlineStack__list")
        )
    )

    headlineNames = headlines.find_elements(By.TAG_NAME, "li")

    print(f"Found {len(headlineNames)} headlines")

    stories = []
    for line in headlineNames:
        try:
            a_tag = line.find_element(By.TAG_NAME, "a") or "No headline"
            link = a_tag.get_attribute("href") or "No link"

            if link != "No link":
                stories.append(link)

            # print(f"Headline: {a_tag.text}")
            # print(f"Link: {link}")

        except Exception as e:
            print("Error processing a headline")

    driver.quit()
    return stories
