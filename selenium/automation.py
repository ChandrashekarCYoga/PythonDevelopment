from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

# /user/local/bin 
# for installing globally

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title



show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button)
user_message = chrome_browser.find_element_by_id('user-message')

user_message.clear()
user_message.send_keys('I AM EXTRA COOOOOL')

show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')

assert 'I AM EXTRA COOOOOL' in output_message.text

user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)



# chrome_browser.close
# chrome_browser.quit()