from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
from bs4 import BeautifulSoup

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Path to ChromeDriver
driver_path = "path/to/chromedriver"

# Start the driver
driver = webdriver.Chrome()

try:
    # Load the target website
    driver.get("https://secure-bonus-377122.uc.r.appspot.com/level4")

    player1_hash = "4b6c244d68296a6569"
    # Get the player buttons and store them
    # buttons = driver.find_elements(By.CLASS_NAME, "player")

    # Variable to store Player 1 button
    player_1_buttons = driver.find_element(By.CSS_SELECTOR, ".\\34 b6c244d68296a6569.player")




        # Example: Extract the scheduledPlayerIndex from JavaScript
    scheduled_player_index = driver.execute_script("return scheduledPlayerIndex;")

    # Print the scheduledPlayerIndex
    print(f"Scheduled Player Index: {scheduled_player_index}")

    time.sleep(3.5)


    def get_scheduled_player():
        light_color = driver.find_element(By.ID, "light").get_attribute("style")
        if "red" in light_color:  # Assuming light turns red when nudging happens
            # Check which player is the scheduled one (nudged player)
            scheduled_player = None
            for button in buttons:
                player_index = button.get_attribute("data-player-index")
                if player_index != "0":  # Player 1 is not the scheduled player
                    scheduled_player = button
                    break
            return scheduled_player
        return None

    # Main loop to monitor the red light and find the scheduled player
    while True:
        scheduled_player = get_scheduled_player()
        if scheduled_player:
            print("Scheduled Player is: ", scheduled_player.text)
        time.sleep(1)  


except Exception as e:
    print(f"Error: {e}")

finally:
    time.sleep(2) 
    driver.quit()


