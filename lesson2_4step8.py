from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    # говорим Selenium проверять в течение 5 секунд, пока цена не будет равна 100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element(
            (By.ID, 'price'), '100'))

    # Нажать на кнопку "Book"
    button = browser.find_element_by_id('book')
    button.click()

    # Проскроллить страницу вниз.
    #browser.execute_script("return arguments[0].scrollIntoView(true);")
    browser.execute_script("window.scrollBy(0, 200);")

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    # Считать значение для переменной x.
    input_x = browser.find_element_by_id('input_value')
    x = input_x.text

    # Посчитать математическую функцию от x.
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    # Нажать на кнопку Submit.
    button_submit = browser.find_element_by_id('solve')
    button_submit.click()

finally:
    # Успеть скопировать код за 10 секунд 29.004254778475246
    time.sleep(10)

    # Закрыть окно браузер
    browser.quit()

# не забываем оставить пустую строку в конце файла