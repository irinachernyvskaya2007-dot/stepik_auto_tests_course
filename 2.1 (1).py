from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    
    # Считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    print(f"Найдено значение x: {x}")
    
    # Вычисляем ответ
    y = calc(x)
    print(f"Вычисленный ответ: {y}")
    
    # Вводим ответ в текстовое поле
    input_answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_answer.send_keys(y)
    
    # Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    checkbox.click()
    
    # Выбираем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    radiobutton.click()
    
    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()