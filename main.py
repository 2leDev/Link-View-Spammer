from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Function to open the link specified number of times
def open_link_multiple_times(link, num_times):
    # Set up Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    service = Service('/path/to/chromedriver.exe')  # Provide the path to your chromedriver executable
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Loop to open the link multiple times
    for _ in range(num_times):
        driver.get(link)
        # You can add additional actions here if needed
        driver.close()  # Close the current tab/window

    # Quit WebDriver
    driver.quit()

if __name__ == "__main__":
    link = input("Enter the link: ")
    num_times = int(input("Enter the number of times to open the link: "))

    open_link_multiple_times(link, num_times)
