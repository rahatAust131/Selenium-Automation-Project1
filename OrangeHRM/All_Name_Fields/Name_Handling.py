
from OrangeHRM.Necessary_Packages_Module.Necessary_Packages import *


def handle_names():
    # firstname field input checking
    try:
        firstname_field = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='firstName']")))
        firstname_field.send_keys(Keys.CONTROL, 'a')
        firstname_field.send_keys(Keys.BACKSPACE)
        firstname_field.send_keys("Rahat")
        write_in_file("Log/report.txt", "First Name: " + firstname_field.get_attribute('value') + " entered successfully!")
    except Exception as e:
        write_in_file("Log/report.txt", "Firstname field exception: " + type(e).__name__)

    # Middle name field input checking
    try:
        middlename_field = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='middleName']")))
        middlename_field.send_keys(Keys.CONTROL, 'a')
        middlename_field.send_keys(Keys.BACKSPACE)
        middlename_field.send_keys("Chowdhury")
        write_in_file("Log/report.txt",
                      "middle Name: " + middlename_field.get_attribute('value') + " entered successfully!")
    except Exception as e:
        write_in_file("Log/report.txt", "Middle name field exception: " + type(e).__name__)

    # lastname field input checking
    try:
        lastname_field = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='lastName']")))
        lastname_field.send_keys(Keys.CONTROL, 'a')
        lastname_field.send_keys(Keys.BACKSPACE)
        lastname_field.send_keys("Zisan")
        write_in_file("Log/report.txt", "Last Name: " + lastname_field.get_attribute('value') + " entered successfully!")
    except Exception as e:
        write_in_file("Log/report.txt", "Last name field exception: " + type(e).__name__)

    # Nickname field input checking
    try:
        nickname_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".orangehrm-edit-employee-content .oxd-form-row:nth-of-type(1) [class='oxd-grid-3 orangehrm-full-width-grid'] input")))
        nickname_field.send_keys(Keys.CONTROL, 'a')
        nickname_field.send_keys(Keys.BACKSPACE)
        nickname_field.send_keys("Zisan")
        write_in_file("Log/report.txt", "Nickname: " + nickname_field.get_attribute('value') + " entered successfully!")
    except Exception as e:
        write_in_file("Log/report.txt", "Nickname field exception: " + type(e).__name__)
