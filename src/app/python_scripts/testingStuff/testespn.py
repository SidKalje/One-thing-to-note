from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By


url = "https://www.espn.com/"
driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
t = time.time()

try:
    driver.get(url)
except TimeoutException:
    driver.execute_script("window.stop();")

print(f"Page loaded in {time.time() - t} seconds")
headlines = driver.find_element(
    By.XPATH, '//*[@id="main-container"]/div/section[3]/div[1]/section/ul'
)
# headlines = driver.find_element(By.CSS_SELECTOR, "ul.headlineStack__listContainer")
headlineNames = headlines.find_elements(By.TAG_NAME, "li")

print(f"Found {len(headlineNames)} headlines")

for line in headlineNames:
    try:
        a_tag = line.find_element(By.TAG_NAME, "a")
        if a_tag.text:
            print(a_tag.text)
        else:
            print("FAILED: " + a_tag)

    except Exception as e:
        print("Error processing a headline")
