from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")

# Нажать на кнопку
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# Запомнить имя текущей вкладки
first_window = driver.window_handles[0]

# Получить имя новой вкладки
new_window = driver.window_handles[1]

# Переключиться на новую вкладку
driver.switch_to.window(new_window)

# Решить капчу
x_element = driver.find_element(By.ID, "input_value")
x = int(x_element.text)
y = calc(x)

input_field = driver.find_element(By.ID, "answer")
input_field.send_keys(y)

submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
submit_button.click()

time.sleep(10)
driver.quit()