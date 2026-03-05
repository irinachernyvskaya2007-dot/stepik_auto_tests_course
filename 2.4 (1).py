from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

# Ждем, пока цена не станет $100 (не меньше 12 секунд)
price = WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

# Нажимаем кнопку Book
book_button = driver.find_element(By.ID, "book")
book_button.click()

# Решаем математическую задачу
x_element = driver.find_element(By.ID, "input_value")
x = int(x_element.text)
y = calc(x)

input_field = driver.find_element(By.ID, "answer")
input_field.send_keys(y)

submit_button = driver.find_element(By.ID, "solve")
submit_button.click()

# Ждем результат и копируем число из алерта
time.sleep(5)
alert = driver.switch_to.alert
print(alert.text.split()[-1])
alert.accept()

driver.quit()