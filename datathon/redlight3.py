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
    driver.get("https://level3-dot-secure-bonus-377122.uc.r.appspot.com/decrypt")
    
    time.sleep(0.5)

    # Submit use/pass

    user_field = driver.find_element(By.ID, "username")
    pass_field = driver.find_element(By.ID, "password") 
    submit_button = driver.find_element(By.CLASS_NAME, "submit-btn") 

    user_field.send_keys("young-hee-admin")
    pass_field.send_keys("squidgame2025")
    submit_button.click()

    divs = driver.find_elements(By.CLASS_NAME, "card-row")
    count = 0

    number1 = "1"
    number132 = "132"
    number1bool = False
    number132bool = False
    first_name_132 = ""
    last_name_132 = ""
    first_name_1 = ""
    last_name_1 = ""

    # Then collect all divs
    divs = driver.find_elements(By.CLASS_NAME, "card-row")
    print(len(divs))
    for div in divs:
        html = div.get_attribute("innerHTML")
        soup = BeautifulSoup(html, "html.parser")
        lines = soup.get_text(separator=" ", strip=True)
        parts = lines.split()
        player_number = ""
        first_name = ""
        last_name = ""
        for i in range(len(parts)):
            if parts[i] == "first_name:":
                first_name = parts[i + 1]
            elif parts[i] == "last_name:":
                last_name = parts[i + 1]
            elif parts[i] == "player_number:":
                player_number = parts[i + 1]
        print(lines)
        if player_number == "1":
            print("✅ Found Player 1")
            first_name_1 = first_name
            last_name_1 = last_name
            number1bool = True

        elif player_number == "132":
            print("✅ Found Player 132")
            first_name_132 = first_name
            last_name_132 = last_name
            number132bool = True
        
        if first_name_1 and first_name_132:
            break

        count += 1
        print(f"Searched through {count} rows")
        if number1bool and number132bool:
            break
        
    print(first_name_1, last_name_1)
    print(first_name_132, last_name_132)
    time.sleep(1)
    
    # Go to encrypted page
    change_page = driver.find_element(By.ID, "toggle-tab")
    change_page.click()
    encrypted_divs = driver.find_elements(By.CLASS_NAME, "player")
    for i in encrypted_divs:
        hashed = i.text
        print(hashed)

        encrypted_input = driver.find_element(By.ID, "encryptedInput")
        decrypt = driver.find_element(By.ID, "decryptBtn")

        encrypted_input.clear()
        encrypted_input.send_keys(hashed)
        decrypt.click()

        output = driver.find_element(By.ID, "decryptedOutput")
        output_text = output.text

        # Name
        names = output_text.split()
        first_name_output = names[0]
        last_name_output = names[1]
        hash_1_found = False
        hash_132_found = False


        if (first_name_output == first_name_1 and last_name_output == last_name_1):
            hash_1 = hashed
            hash_1_found = True
        if (first_name_output == first_name_132 and last_name_output == last_name_132):
            hash_132 = hashed
            hash_132_found = True
        if hash_1_found and hash_132_found:
            break


    print(f"hash1: {hash_1}, hash132: {hash_132}")
    print(f"Player 1 Name: {first_name_1 + " " + last_name_1} and Player 132 Name: {first_name_132 + " " + last_name_132}")





except Exception as e:
    print(f"Error: {e}")

finally:
    time.sleep(2) 
    driver.quit()

