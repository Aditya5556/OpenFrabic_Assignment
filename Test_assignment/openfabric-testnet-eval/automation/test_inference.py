from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_inference():
    driver = webdriver.Chrome()
    driver.get("https://openfabric.dev")
    driver.find_element(By.LINK_TEXT, "Login with Metamask").click()
    time.sleep(15)  # Allow wallet auth
    driver.find_element(By.LINK_TEXT, "Marketplace").click()
    driver.find_element(By.CSS_SELECTOR, ".app-card:first-child .create-instance").click()
    time.sleep(5)
    driver.find_element(By.ID, "test-input").send_keys("Hello AI")
    driver.find_element(By.ID, "send-button").click()
    output = driver.find_element(By.ID, "output").text
    print("Output:", output)
    driver.quit()

test_inference()