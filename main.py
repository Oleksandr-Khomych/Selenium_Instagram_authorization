import config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    login = config.login
    password = config.password
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "username"))
        )
    finally:
        input_login = driver.find_element_by_name('username')
        input_login.clear()
        input_login.send_keys(login)
        input_password = driver.find_element_by_name('password')
        input_password.clear()
        input_password.send_keys(password, Keys.RETURN)
    input()     # --- window doesn't close


if __name__ == '__main__':
    main()
