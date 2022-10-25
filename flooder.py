from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import os
import time
import random

bot_num = int(input("How many bots do you want? "))
pin = input("What is the pin? ")
PATH = r"PATH to chromedriver"
driver = webdriver.Chrome(PATH)


def kahoot_cheese(num):
    driver.get("https://kahoot.it")
    driver.implicitly_wait(3)
    # JOINING GAME
    element = driver.find_element(By.ID, "game-input")
    element.send_keys(pin)  # Make this number the PIN
    element.send_keys(Keys.RETURN)
    # MAKING USERNAME
    try:
        element = driver.find_element(By.ID, "nickname")
        # You can change bob to whatever name you want
        element.send_keys(f"bob{num}")
        element.send_keys(Keys.RETURN)
    except:
        driver.close()


for x in range(bot_num):
    kahoot_cheese(x)
    if x != bot_num - 1:
        driver.switch_to.new_window("tab")  # Open new tab
    time.sleep(0.1)
driver.maximize_window()  # MAKE WINDOW BIGGER
os.system("cls" if os.name == "nt" else "clear")

current_window = driver.current_window_handle
windows = driver.window_handles
action = ActionBuilder(driver)
y_answers = [800, 200]
x_answers = [100, 1700]
while True:
    if (
        driver.current_url == "https://kahoot.it/ranking"
        or driver.current_url == "https://kahoot.it"
    ):
        break
    if driver.current_url == "https://kahoot.it/gameblock":
        for w in windows:
            x = 0
            y_answers = [800, 200]
            driver.switch_to.window(w)
            while driver.current_url == "https://kahoot.it/gameblock":
                if x > 0:
                    y_answers = [650]
                action.pointer_action.move_to_location(
                    random.choice(x_answers), random.choice(y_answers)
                )
                action.perform()
                ActionChains(driver).click(None).perform()
                x += 1

print("All done!")
driver.quit()
