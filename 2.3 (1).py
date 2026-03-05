from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    
    # 1. Нажимаем на кнопку "I want to go on a magical journey!"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # 2. Переключаемся на confirm окно и принимаем его (нажимаем OK)
    confirm = browser.switch_to.alert
    confirm.accept()
    
    # 3. Теперь мы на новой странице, решаем капчу для роботов
    # Считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    
    # Вычисляем ответ
    y = calc(x)
    
    # Вводим ответ в текстовое поле
    input_answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_answer.send_keys(y)
    
    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()