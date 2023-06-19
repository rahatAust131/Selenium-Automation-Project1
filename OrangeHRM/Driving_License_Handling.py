

from Necessary_Packages import *

def handle_driving_license():
    # Driver's license number field input checking
    try:
        driver_license_field = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".orangehrm-edit-employee-content .oxd-form-row:nth-child(3) [class='oxd-grid-3 orangehrm-full-width-grid']:nth-of-type(2) .oxd-grid-item--gutters:nth-of-type(1) input")))
        driver_license_field.send_keys(Keys.CONTROL, 'a')
        driver_license_field.send_keys(Keys.BACKSPACE)
        driver_license_field.send_keys("1254")
        write_in_file("report.txt", "Driver license number: " + driver_license_field.get_attribute(
            'value') + " entered successfully!")
    except Exception as e:
        write_in_file("report.txt", "Driver license number field exception: " + type(e).__name__)

    # License Expiry Date field input checking
    try:
        license_expiry_date_field = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".orangehrm-edit-employee-content .oxd-form-row:nth-child(3) [placeholder]")))
        license_expiry_date_field.send_keys(Keys.CONTROL, 'a')
        license_expiry_date_field.send_keys(Keys.BACKSPACE)
        license_expiry_date_field.send_keys("2024-05-25")
        write_in_file("report.txt", "license Expiry date field: " + license_expiry_date_field.get_attribute(
            'value') + " entered successfully!")
    except Exception as e:
        write_in_file("report.txt", "license Expiry date field exception: " + type(e).__name__)