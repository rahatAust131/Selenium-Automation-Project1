from Necessary_Packages import *

def handle_emp_id():
    # Employee ID field input checking
    try:
        emp_id_field = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".orangehrm-edit-employee-content .oxd-form-row:nth-child(3) [class='oxd-grid-3 orangehrm-full-width-grid']:nth-of-type(1) .oxd-grid-item--gutters:nth-of-type(1) input")))
        emp_id_field.send_keys(Keys.CONTROL, 'a')
        emp_id_field.send_keys(Keys.BACKSPACE)
        emp_id_field.send_keys("4580")
        write_in_file("report.txt", "Employee id: " + emp_id_field.get_attribute('value') + " entered successfully!")
    except Exception as e:
        write_in_file("report.txt", "Employee ID field exception: " + type(e).__name__)

    # Other ID field input checking
    try:
        other_id_field = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".orangehrm-edit-employee-content .oxd-form-row:nth-child(3) [class='oxd-grid-3 orangehrm-full-width-grid']:nth-of-type(1) .oxd-grid-item--gutters:nth-of-type(2) input")))
        other_id_field.send_keys(Keys.CONTROL, 'a')
        other_id_field.send_keys(Keys.BACKSPACE)
        other_id_field.send_keys("1254")
        write_in_file("report.txt", "Other id: " + other_id_field.get_attribute('value') + " entered successfully!")
    except Exception as e:
        write_in_file("report.txt", "Other ID field exception: " + type(e).__name__)