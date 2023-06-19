

from Necessary_Packages import *

def handle_marital_status():
    # Marital Status field input checking
    try:
        marital_status_field = WebDriverWait(driver, 5, poll_frequency=1).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".orangehrm-edit-employee-content .oxd-grid-item--gutters:nth-of-type(2) [tabindex]")))
        marital_status_field.click()

        while marital_status_field.text != 'Single':
            marital_status_field.send_keys(Keys.ARROW_DOWN)
        marital_status_field.send_keys(Keys.ENTER)
        write_in_file("report.txt", "Marital Status: " + marital_status_field.text + " entered successfully!")
    except Exception as e:
        write_in_file("report.txt", "Marital Status field exception: " + type(e).__name__)