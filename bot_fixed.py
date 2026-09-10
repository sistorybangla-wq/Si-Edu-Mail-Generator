import time
import re
import string
import random
import sys
import colorama
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import seleniumwire.undetected_chromedriver.v2 as uc
from random import randint
from __constants.const import *
from __banner.myBanner import bannerTop
from __colors__.colors import *
from helper import EduHelper

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########
######## Version: 2.0 FIXED (September 2026) ########
######## Github Repo - https://git.io/JJisT/ ########

def postFix(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def random_phone_num_generator():
    first = str(random.choice(country_codes))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)

def random_registration_number():
    """Generate random registration number (2026 Update)"""
    return str(random.randint(1000000, 9999999))

def random_roll_number():
    """Generate random roll/student ID number (2026 Update)"""
    prefix = random.randint(19, 24)  # Year prefix
    suffix = str(random.randint(10000, 99999)).zfill(5)
    return f"{prefix}{suffix}"

def interceptor(request):
    if request.method == 'POST' and request.url == 'https://www.openccc.net/f-vs-stand-I-hat-of-yout-ands-Banquoh-Cumberland?d=www.openccc.net':
        request.abort(403)

def safe_find_element(driver, by, value, timeout=10):
    """Safe element finder with error handling"""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    except Exception as e:
        print_debug(f"Element not found: {by} = {value}, Error: {e}")
        return None

def safe_click_element(driver, by, value, timeout=10):
    """Safe element click with error handling"""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()
        return True
    except Exception as e:
        print_debug(f"Click failed: {by} = {value}, Error: {e}")
        return False

def print_debug(message):
    """Print debug messages if DEBUG is enabled"""
    if DEBUG:
        print(f"[DEBUG] {message}")

def start_bot(start_url, email, college, collegeID, cookies, token):
    """Main bot function with improved error handling"""
    
    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Parsing Incap Cookies (success)')
    cookies['reese84'] = token

    studentPhone = random_phone_num_generator()
    registrationNo = random_registration_number()  # 2026 Update
    rollNo = random_roll_number()  # 2026 Update

    ex_split = studentAddress.split("\n")
    streetAddress = ex_split[0]

    if(re.compile(',').search(ex_split[1]) != None):
        ex_split1 = ex_split[1].split(', ')
        cityAddress = ex_split1[0]
        ex_split2 = ex_split1[1].split(' ')
        stateAddress = ex_split2[0]
        postalCode = ex_split2[1]
    else:
        ex_split3 = ex_split[1].split(' ')
        cityAddress = ex_split3[0]
        stateAddress = ex_split3[1]
        postalCode = ex_split3[2]

    random.seed()
    letters = string.ascii_uppercase
    middleName = random.choice(letters)

    # Browser selection with error handling
    try:
        fp = open('prefBrowser.txt', 'r')
        typex = fp.read().strip()
        fp.close()
    except Exception as e:
        print(fr + f'Error reading browser preference: {e}')
        return

    driver = None
    try:
        if typex == 'chrome':
            driver = webdriver.Chrome(r'./webdriver/chromedriver')
        elif typex == 'firefox':
            driver = webdriver.Firefox(executable_path=r'./webdriver/geckodriver')
        elif typex == 'chrome_undetected':
            driver = uc.Chrome()
        elif typex == '':
            print(fr + 'Error - Run setup.py first')
            return
        else:
            print(fr + f'Unknown browser type: {typex}')
            return
    except Exception as e:
        print(fr + f'Error initializing driver: {e}')
        return

    try:
        driver.request_interceptor = interceptor
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Interceptor Addition (success)')
        driver.maximize_window()

        driver.get('https://www.openccc.net')
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Injecting Incap Cookies', end='')
        for cookie in cookies.keys():
            ck = {'name': cookie, 'value': cookies[cookie], 'domain': '.openccc.net'}
            try:
                driver.add_cookie(ck)
            except Exception as e:
                print_debug(f'Could not add cookie {cookie}: {e}')
        print(fg + ' (success)')

        print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Incapsula Bypass Successfull')
        print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Hold on Starting now, Keep checking this terminal for instructions')

        driver.get(start_url)
        time.sleep(1)

        # Wait for form
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "inputFirstName"))
            )
        except:
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "accountFormSubmit"))
                ).click()
            except Exception as e:
                print(fr + f'Error waiting for form: {e}')
                return

        time.sleep(5)
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Account Progress - 1/3', end='')

        try:
            # Fill personal information
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, "inputFirstName"))
            ).send_keys(firstName)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, "inputMiddleName"))
            ).send_keys(middleName)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, "inputLastName"))
            ).send_keys(LastName)
            time.sleep(0.5)

            # Click radio buttons
            driver.find_element(By.XPATH, '//*[@id="hasOtherNameNo"]').click()
            time.sleep(0.3)
            driver.find_element(By.XPATH, '//*[@id="hasPreferredNameNo"]').click()
            time.sleep(0.5)

            # Set birth date
            WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, f'#inputBirthDateMonth option[value="{randomMonth}"]'))
            ).click()
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, f'#inputBirthDateDay option[value="{randomDay}"]'))
            ).click()
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputBirthDateYear'))
            ).send_keys(str(randomYear))
            time.sleep(0.5)

            # Confirm birth date
            WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, f'#inputBirthDateMonthConfirm option[value="{randomMonth}"]'))
            ).click()
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, f'#inputBirthDateDayConfirm option[value="{randomDay}"]'))
            ).click()
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputBirthDateYearConfirm'))
            ).send_keys(str(randomYear))
            time.sleep(0.5)

            # SSN question
            WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.ID, '-have-ssn-no'))
            ).click()
            time.sleep(2)

            # Submit page 1
            element = driver.find_element(By.ID, 'accountFormSubmit')
            desired_y = (element.size['height'] / 2) + element.location['y']
            window_h = driver.execute_script('return window.innerHeight')
            window_y = driver.execute_script('return window.pageYOffset')
            current_y = (window_h / 2) + window_y
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            time.sleep(0.5)
            element.click()

            print(fg + ' (Success)')
        except Exception as e:
            print(fr + f' (Failed: {e})')
            return

        # Page 2 - Contact and Address
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Account Progress - 2/3', end='')

        try:
            time.sleep(1)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputEmail'))
            ).send_keys(email)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputEmailConfirm'))
            ).send_keys(email)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputSmsPhone'))
            ).send_keys(studentPhone)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputStreetAddress1'))
            ).send_keys(streetAddress)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputCity'))
            ).send_keys(cityAddress)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, f'#inputState option[value="{stateAddress}"]'))
            ).click()
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputPostalCode'))
            ).send_keys(postalCode)
            time.sleep(1)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'accountFormSubmit'))
            ).click()

            # Handle phone validation errors
            try:
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="messageFooterLabel"]').click()

                retry_count = 0
                while retry_count < 3:
                    chkInputPhone = driver.find_element(By.ID, 'inputSmsPhone')
                    chkError = chkInputPhone.get_attribute('class')
                    if 'error' in chkError:
                        print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + f'Invalid Number (Retry {retry_count+1}), Trying new one....')
                        chkInputPhone.clear()
                        studentPhone = random_phone_num_generator()
                        chkInputPhone.send_keys(studentPhone)
                        time.sleep(0.5)
                        try:
                            WebDriverWait(driver, 60).until(
                                EC.presence_of_element_located((By.ID, 'inputAlternatePhone_auth_txt'))
                            ).click()
                            time.sleep(2)
                            WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="messageFooterLabel"]'))
                            ).click()
                            retry_count += 1
                        except:
                            break
                    else:
                        break
            except Exception as e:
                print_debug(f'Phone validation: {e}')

            time.sleep(2)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'accountFormSubmit'))
            ).click()

            # Address validation override
            try:
                time.sleep(1)
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'messageFooterLabel'))
                ).click()
                time.sleep(0.5)

                WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.ID, 'inputAddressValidationOverride'))
                ).click()
                time.sleep(1)

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'accountFormSubmit'))
                ).click()
            except:
                pass

            print(fg + ' (Success)')
        except Exception as e:
            print(fr + f' (Failed: {e})')
            return

        # Page 3 - Credentials
        userName = firstName + str(postFix(7))
        pwd = LastName + str(postFix(5))
        pin = postFix(4)

        try:
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputUserId'))
            ).send_keys(userName)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputPasswd'))
            ).send_keys(pwd)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputPasswdConfirm'))
            ).send_keys(pwd)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputPin'))
            ).send_keys(str(pin))
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputPinConfirm'))
            ).send_keys(str(pin))
            time.sleep(0.5)

            # Security questions
            WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#inputSecurityQuestion1 option[value="5"]'))
            ).click()
            time.sleep(0.5)

            random.seed(10)
            letters = string.ascii_lowercase
            sec_ans1 = LastName + ''.join(random.choices(letters, k=4))
            sec_ans2 = LastName + ''.join(random.choices(letters, k=4))
            sec_ans3 = LastName + ''.join(random.choices(letters, k=4))

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputSecurityAnswer1'))
            ).send_keys(sec_ans1)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#inputSecurityQuestion2 option[value="6"]'))
            ).click()
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputSecurityAnswer2'))
            ).send_keys(sec_ans2)
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#inputSecurityQuestion3 option[value="7"]'))
            ).click()
            time.sleep(0.5)

            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, 'inputSecurityAnswer3'))
            ).send_keys(sec_ans3)

            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Please fill the captcha in webdriver to proceed further')

            # Wait for captcha
            solved = 0
            for attempt in range(1, 200):
                try:
                    xx = driver.find_element(By.NAME, 'captchaResponse')
                    tdt = xx.get_attribute('value')
                    if tdt != '':
                        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Captcha Solved, Executing Further')
                        solved = 1
                        break
                    else:
                        time.sleep(2)
                except Exception as e:
                    time.sleep(2)

            if solved == 1:
                time.sleep(1)

                element = driver.find_element(By.ID, 'accountFormSubmit')
                desired_y = (element.size['height'] / 2) + element.location['y']
                window_h = driver.execute_script('return window.innerHeight')
                window_y = driver.execute_script('return window.pageYOffset')
                current_y = (window_h / 2) + window_y
                scroll_y_by = desired_y - current_y
                driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
                time.sleep(0.5)

                WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.ID, "accountFormSubmit"))
                ).click()

                print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Account Progress - 3/3' + fg + ' (Success)')

                # 2026 Update - Save with all details
                try:
                    fp = open('myccAcc.txt', 'a', encoding='utf-8')
                    birthDay = f"{randomMonth}/{randomDay}/{randomYear}"
                    account_data = (
                        f'Email - {email} '
                        f'Password - {pwd} '
                        f'UserName - {userName} '
                        f'First Name - {firstName} '
                        f'Middle Name - {middleName} '
                        f'Last Name - {LastName} '
                        f'College - {college} '
                        f'Phone - {studentPhone} '
                        f'Birth Date - {birthDay} '
                        f'Registration No - {registrationNo} '
                        f'Roll No - {rollNo} '
                        f'Address - {streetAddress}, {cityAddress}, {stateAddress} {postalCode}\n'
                    )
                    fp.write(account_data)
                    fp.close()

                    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Account Created Successfully')
                    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + f'Registration No: {registrationNo}')
                    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + f'Roll No: {rollNo}')
                    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Details saved in myccAcc.txt')
                except Exception as e:
                    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + f'Error saving details: {e}')

                # Continue with application
                time.sleep(1)
                try:
                    WebDriverWait(driver, 60).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="registrationSuccess"]/main/div[2]/div/div/button'))
                    ).click()
                    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Application form submission completed' + fg + ' (Success)')
                except Exception as e:
                    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Account creation completed')

            else:
                print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Timeout while waiting for captcha')

        except Exception as e:
            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + f'Error during credentials: {e}')

    except Exception as e:
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + f'Critical error: {e}')
    finally:
        if driver:
            try:
                driver.close()
            except:
                pass

def main():
    sys.stdout.write(bannerTop())

    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Si-Edu-Mail-Generator v2.0 FIXED (September 2026)')
    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Select a college from all available colleges to proceed...\\n')

    time.sleep(0.4)

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]

    for index, college in enumerate(allColleges):
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + str(index + 1) + ' - ' + random.choice(colors) + college)
    
    isIDError = True
    
    while isIDError != False:
        print('\\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Enter college id for ex - 1 or 2 or 3.... : ', end='')
        try:
            userInput = int(input())
            if userInput > len(allColleges) or userInput < 1:
                print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Wrong College id')
            else:
                userInput = userInput - 1
                isIDError = False
        except ValueError:
            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Please enter a valid number')

    time.sleep(0.4)

    print('\\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Selected College: ' + fy + allColleges[userInput])

    time.sleep(0.4)

    print('\\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Enter Your Email: ', end='')
    userEmail = input().strip()

    if not userEmail:
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Email cannot be empty!')
        return

    time.sleep(0.4)
    
    print('\\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Performing Incapsula Bypass (v2.0 FIXED)')
    fg_lp = EduHelper(clg_ids[userInput])
    result = fg_lp._tryHarder()
    
    if result[0] is None:
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Failed to bypass Incapsula. Please try again later.')
        return
    
    start_url, cookies, token = result

    time.sleep(1)
    
    start_bot(start_url, userEmail, allColleges[userInput], userInput + 1, cookies, token)

if __name__ == '__main__':
    main()
