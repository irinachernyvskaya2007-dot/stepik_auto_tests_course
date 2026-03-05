from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    
    # Находим картинку с сокровищем
    treasure_img = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    
    # Получаем значение атрибута valuex
    x = treasure_img.get_attribute("valuex")
    print(f"Значение x из атрибута: {x}")
    
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