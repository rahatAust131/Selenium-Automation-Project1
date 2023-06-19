from OrangeHRM.Necessary_Packages_Module.Necessary_Packages import *


def handle_military_service_field():
    try:
        military_service_field = WebDriverWait(driver, 5, poll_frequency=1). \
            until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                    ".orangehrm-edit-employee-content .oxd-form-row:nth-child(7) .oxd-grid-item--gutters:nth-of-type(1) input")))
        military_service_field.send_keys(Keys.CONTROL, 'a')
        military_service_field.send_keys(Keys.BACKSPACE)
        military_service_field.send_keys(2)
        write_in_file("Log/report.txt", "Military Service field value: " + military_service_field.get_attribute('value') + " entered successfully!")
    except Exception as e:
        write_in_file("Log/report.txt", "Military Service Field Exception: " + type(e).__name__)
