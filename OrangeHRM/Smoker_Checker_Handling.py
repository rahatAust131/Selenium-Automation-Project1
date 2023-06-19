from Necessary_Packages import *


def handle_smoker_checker():
    try:
        smoker_field = WebDriverWait(driver, 5, poll_frequency=1). \
            until(EC.visibility_of_element_located
                  ((By.CSS_SELECTOR,
                    ".orangehrm-edit-employee-content .oxd-form-row:nth-child(7) .oxd-grid-item--gutters:nth-of-type(2) div:nth-of-type(2) label")))

        smoker_field.click()
        write_in_file("report.txt", "Smoker: " + smoker_field.text + " selected!")

    except Exception as e:
        write_in_file("report.txt", "Smoker field exception: " + type(e).__name__)
