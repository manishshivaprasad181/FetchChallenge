import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Function call to compare weights of 2 groups of 3 bars each
def weigh_bars(driver, values_list):
    for i in range(len(values_list[0])):
        left_input_field = driver.find_element(By.ID, f'left_{i}')
        left_input_field.send_keys(values_list[0][i])
        right_input_field = driver.find_element(By.ID, f'right_{i}')
        right_input_field.send_keys(values_list[1][i])
    weigh_button = driver.find_element(By.ID, 'weigh')
    weigh_button.click()
    time.sleep(2)
    result_element = driver.find_element(By.XPATH, '//button[@id="reset"]')
    result = result_element.text
    reset_button = driver.find_element(By.XPATH, '//button[@id="reset" and text()="Reset"]')
    reset_button.click()
    return result


# weighs and return the result by comparing two elements of the group
def perform_weighing(driver, values):
    left_input_field = driver.find_element(By.ID, 'left_0')
    right_input_field = driver.find_element(By.ID, 'right_0')
    left_input_field.send_keys(values[0])
    time.sleep(1)
    right_input_field.send_keys(values[1])
    weigh_button = driver.find_element(By.ID, 'weigh')
    weigh_button.click()
    time.sleep(2)
    result_element = driver.find_element(By.XPATH, '//button[@id="reset"]')
    result = result_element.text
    time.sleep(2)
    return result


# Function to Click the Fake bar based on Fake bar number
def click_fake_bar(driver, fake_bar_number):
    fake_bar = driver.find_element(By.ID, f'coin_{fake_bar_number}')
    fake_bar.click()


# Function deciding the fake bar
def handle_result(driver, values, result):
    if result == '=':
        fake_bar_number = values[2]
    elif result == '>':
        fake_bar_number = values[1]
    else:
        fake_bar_number = values[0]
    print_weighings(driver)
    click_fake_bar(driver, fake_bar_number)


# Function call to Print the list of weighings
def print_weighings(driver):
    game_info_div = driver.find_element(By.CLASS_NAME, 'game-info')
    weighings = game_info_div.find_element(By.XPATH, './div').text
    weighings_list = game_info_div.find_elements(By.XPATH, './ol/li')
    print("List of weighings:")
    for idx, weighing in enumerate(weighings_list, start=1):
        print(f"Weighing {idx}: {weighing.text}")


# Main Method
def main():
    driver = webdriver.Safari()
    driver.get("http://sdetchallenge.fetch.com/")
    values_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]  # 9 Gold bars from 0 to 8
    result = weigh_bars(driver, values_list)  # function call to compare weights of 2 groups of 3 bars each
    if result == '=':
        values = values_list[2]
    elif result == '>':
        values = values_list[1]
    else:
        values = values_list[0]
    result = perform_weighing(driver, values)  # Function call to identify the fake bar in the single group
    handle_result(driver, values, result)
    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    main()
