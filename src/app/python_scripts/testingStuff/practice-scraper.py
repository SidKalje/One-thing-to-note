import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.youtube.com/@JohnWatsonRooney/videos"

# Set up Chrome options (using headless mode for faster loading)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Set up the service
service = Service(ChromeDriverManager().install())

# Initialize the driver with service and options
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url)

# Wait for the page to load dynamic content
time.sleep(5)

# Find all video elements (adjust the CSS selector to match the container elements)
videos = driver.find_elements(By.XPATH, '//*[@id="dismissible"]')


print(f"Found {len(videos)} videos")

for video in videos:
    try:
        # Option 1: Get title from the 'title' attribute of the <a> element
        # title_link = video.find_element(By.ID, "video-title-link")
        # video_title = title_link.get_attribute("title")

        # Option 2 (alternative): Get text from the child <yt-formatted-string>
        title_element = video.find_element(
            By.XPATH, "#video-title-link yt-formatted-string"
        )
        video_title = title_element.text

        print(video_title)
    except Exception as e:
        print("Error processing a video:")

driver.quit()
