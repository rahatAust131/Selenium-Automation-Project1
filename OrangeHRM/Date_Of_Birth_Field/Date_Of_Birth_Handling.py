from OrangeHRM.Necessary_Packages_Module.Necessary_Packages import *


def handle_date_of_birth():
    # Date of Birth field input checking
    try:
        date_of_birth_field = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".orangehrm-edit-employee-content .oxd-form-row:nth-child(5) [placeholder]")))
        date_of_birth_field.send_keys(Keys.CONTROL, 'a')
        date_of_birth_field.send_keys(Keys.BACKSPACE)
        date_of_birth_field.send_keys("1999-11-28")     # YYYY-MM-DD format
        write_in_file("Log/report.txt",
                      "Date of Birth field: " + date_of_birth_field.get_attribute('value') + " entered successfully!")
    except Exception as e:
        write_in_file("Log/report.txt", "Date of Birth field exception: " + type(e).__name__)
