from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/run_task')
def run_task():
    # Set up Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    service = Service('path/to/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Perform your Selenium task
    driver.get('https://www.facebook.com')
    # title = driver.title
    locate_profile = driver.find_element(By.CLASS_NAME, "x78zum5")
    locate_profile.click()

    # Close the browser
    driver.quit()

    return f"Task completed. Page title: {title}"

if __name__ == '__main__':
    app.run(port=5000)