# # TODO: Importing Modules
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# # TODO: Opening the websites
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # path = 'C:\Program Files (x86)/chromedriver.exe'
# #driver = webdriver.Chrome(path)
#driver.get('https://in.indeed.com/')
# #driver.maximize_window()
# #time.sleep(2)
#website_title = driver.title
#print(website_title)


# # TODO: First of all open Chrome(local host) in background so as to continue the further process and to do so run these two commands in cmd
    # * cd C:\Program Files\Google\Chrome\Application
    # * chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\WebDrivers\localhost"

# #? setting custom path for driver so as to avoid denial of administrator access in C Drive
# #? Add user agent to mimic non automated behaviour for bypassing google login auth.


# # TODO: Opening the website and printing the title of website
import os
# Specify the custom path to the directory containing the WebDriver executable
custom_path = r'D:\WebDrivers'
# Add the custom path to the PATH environment variable
os.environ['PATH'] += os.pathsep + custom_path
option = webdriver.ChromeOptions()
option.add_experimental_option('debuggerAddress','localhost:9222')

driver = webdriver.Chrome(options = option)
driver.get('https://in.indeed.com/')
website_title = driver.title
print(website_title)
print('Window : ', driver.window_handles)

try:
    # # TODO: Clicking on Sign-In button
    signIn_btn = driver.find_element(By.LINK_TEXT, "Sign in")
    signIn_btn.click()


    # # * email's input box id = 'ifl-InputFormField-3'
    # # * continue with google button class = 'css-zneog5.e1wnkr790'
    # # * continue button's class = 'dd-privacy-allow.css-jorj5j.e8ju0x51'

    username = 'aviralm522@gmail.com'
    pswd = 'Aviral$1234'

    try:

        # # TODO: Continue with Google
        continue_with_google_btn = driver.find_element(By.CLASS_NAME, 'css-zneog5.e1wnkr790')
        continue_with_google_btn.click()


        # # TODO: Switching focus from parent window to child window / pop-up window to perform action on it
        # * Parent window
        main_window_handle = driver.window_handles[0]
        # * Child window 
        pop_up_window_handle = driver.window_handles[1]
        # * switching to pop-up window
        driver.switch_to.window(pop_up_window_handle) 


        # # TODO: Login Script
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'identifierId')))  #! used for waiting for 10 sec

        # * email
        sleep(3)
        try:
            email_input = driver.find_element(By.XPATH, "//input[@type='email']")
            email_input.send_keys(username)
            driver.find_element(By.XPATH,'//*[@id="identifierNext"]').click()
        except:
            email_input = driver.find_element(By.CLASS_NAME, 'd2laFc')
            email_input.click()
        sleep(2)
        # * pswd
        # ! When we will enter password it will give error "This browser or app may not be secure"
            # ! This is due to CEF(Chromium Embedded Framework) browser based OAuth Authnetication
        
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'whsOnd.zHQkBf'))
        )   # ! wait for 10sec to let element visible and if not then give timeout
        
        pswd_input = driver.find_element(By.XPATH, '//input[@type="password"]')
        # pswd_input = driver.find_element(By.CLASS_NAME, 'whsOnd.zHQkBf')
        pswd_input.send_keys(pswd)

        pswd_btn = driver.find_element(By.XPATH, '//*[@id="passwordNext"]')
        sleep(2)
        pswd_btn.click()
        # driver.close()
        driver.switch_to.window(main_window_handle) # ! switching focus back to main window
        print('On main window')

    except:
        driver.switch_to.window(main_window_handle)

except:
    pass

job_profile = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#text-input-what'))
)
# driver.find_element(By.CLASS_NAME,'css-p1lp5i.e1jgz0i3').send_keys('Python Developer')
job_profile.send_keys('Python Developer')
sleep(5)
