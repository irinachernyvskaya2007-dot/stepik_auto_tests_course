from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    # Заполняем текстовые поля
    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    first_name.send_keys("Ivan")
    
    last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    last_name.send_keys("Petrov")
    
    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email.send_keys("ivan@example.com")
    
    # Создаем временный текстовый файл
    # Получаем путь к текущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'bio.txt')
    
    # Создаем и записываем что-то в файл (можно оставить пустым)
    with open(file_path, 'w') as file:
        file.write("This is my short bio.")
    
    # Находим поле для загрузки файла и отправляем путь к файлу
    file_input = browser.find_element(By.CSS_SELECTOR, "input#file")
    file_input.send_keys(file_path)
    
    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()
    
    # Удаляем созданный файл после завершения
    os.remove(file_path)