from OrangeHRM.Necessary_Packages_Module.Necessary_Packages import *


def handle_ssn_and_sin_number():
    # SSN number field input checking
    try:
        ssn_field = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".orangehrm-edit-employee-content [class='oxd-grid-3 orangehrm-full-width-grid']:nth-of-type(3) .oxd-grid-item--gutters:nth-of-type(1) input")))
        ssn_field.send_keys(Keys.CONTROL, 'a')
        ssn_field.send_keys(Keys.BACKSPACE)
        ssn_field.send_keys("778899")
        write_in_file("Log/report.txt", "SSN number: " + ssn_field.get_attribute('value') + " entered successfully!")
    except Exception as e:
        write_in_file("Log/report.txt", "SSN number field exception: " + type(e).__name__)

    # SIN number field input checking
    try:
        sin_field = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".orangehrm-edit-employee-content [class='oxd-grid-3 orangehrm-full-width-grid']:nth-of-type(3) .oxd-grid-item--gutters:nth-of-type(2) input")))
        sin_field.send_keys(Keys.CONTROL, 'a')
        sin_field.send_keys(Keys.BACKSPACE)
        sin_field.send_keys("998877")
        write_in_file("Log/report.txt", "SIN number: " + sin_field.get_attribute('value') + " entered successfully!")
    except Exception as e:
        write_in_file("Log/report.txt", "SIN number field exception: " + type(e).__name__)
