from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")
    
    # Считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    print(f"Найдено значение x: {x}")
    
    # Вычисляем ответ
    y = calc(x)
    print(f"Вычисленный ответ: {y}")
    
    # Находим поле для ввода ответа
    input_answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    
    # Прокручиваем страницу так, чтобы поле ввода стало видимым
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
    
    # Вводим ответ
    input_answer.send_keys(y)
    
    # Находим checkbox и прокручиваем до него перед кликом
    checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    
    # Находим radiobutton и прокручиваем до него
    radiobutton = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    
    # Находим кнопку Submit и прокручиваем до неё
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()