from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")  # для selects2.html просто замените ссылку
    
    # Находим элементы с числами и получаем их текст
    num1_element = browser.find_element(By.CSS_SELECTOR, "span#num1")
    num2_element = browser.find_element(By.CSS_SELECTOR, "span#num2")
    
    # Преобразуем текст в целые числа и складываем
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    total = num1 + num2
    print(f"Найдены числа: {num1} и {num2}, сумма = {total}")
    
    # Находим выпадающий список и выбираем нужное значение
    select_element = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select_element.select_by_value(str(total))  # важно: передаем строку, а не число!
    
    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()