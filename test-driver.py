SERVER_ADDRESS = ''
USER_ID = ''
USER_PW = ''

COLLABORATORS = 10
TEST_TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lobortis tellus urna, quis semper ante tristique sodales. Vestibulum bibendum ligula elit, eget ultricies turpis finibus sit amet. Integer bibendum neque in aliquam vehicula. Donec finibus lacinia mauris et dictum. Ut interdum, nibh ut finibus finibus, sapien nisi pretium nulla, non scelerisque tortor tortor a nunc. Etiam feugiat metus ac varius sagittis. Nam nec lectus consectetur, posuere dolor et, tincidunt tellus. Aenean augue mauris, porta eu scelerisque quis, elementum at nunc. Aliquam malesuada erat pellentesque enim aliquet, scelerisque auctor neque dapibus. Vivamus justo sem, efficitur nec elit nec, malesuada congue lectus. Morbi ipsum turpis, cursus eget arcu non, ultricies faucibus lorem. Suspendisse est dui, tristique ac elit non, maximus condimentum justo. Sed sit amet risus sapien. Phasellus hendrerit efficitur rhoncus. Etiam in consectetur dui. Sed fermentum mauris ut metus molestie, ac porttitor ex ullamcorper."

import time
from selenium import webdriver
from random import randrange
import threading

def type_test(URL):
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.implicitly_wait(10) # seconds
    driver.get(URL)
    user_id = driver.find_element_by_id('id_login')
    user_pw = driver.find_element_by_id('id_password')
    user_id.send_keys(USER_ID)
    user_pw.send_keys(USER_PW)
    login_button = driver.find_element_by_css_selector('button[type="submit"]')
    login_button.click()
    document_contents = driver.find_element_by_css_selector('.ProseMirror-content')
    time.sleep(3)
    document_contents.click()
    time.sleep(1)
    document_contents.click()
    for char in TEST_TEXT:
        document_contents.send_keys(char)
        time.sleep(randrange(1,20)/10.0)
    time.sleep(5) # Let the user actually see something!
    driver.quit()

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.implicitly_wait(10) # seconds
driver.get(SERVER_ADDRESS)
#time.sleep(5) # Let the user actually see something!
user_id = driver.find_element_by_id('id_login')
user_pw = driver.find_element_by_id('id_password')
user_id.send_keys(USER_ID)
user_pw.send_keys(USER_PW)
login_button = driver.find_element_by_css_selector('button[type="submit"]')
login_button.click()
create_new_button = driver.find_element_by_css_selector('.createNew')
create_new_button.click()
document_contents = driver.find_element_by_css_selector('.ProseMirror-content')
time.sleep(3)
URL = driver.current_url
for _ in range(COLLABORATORS):
    t = threading.Thread(target=type_test, args=(URL, ))
    t.start()
driver.quit()
