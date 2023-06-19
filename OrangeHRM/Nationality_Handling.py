from Necessary_Packages import *


def handle_nationality():
    # Nationality field input checking
    try:
        nationality_field = WebDriverWait(driver, 5, poll_frequency=1). \
            until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                    ".orangehrm-edit-employee-content .orangehrm-vertical-padding:nth-of-type(1) \
                                                    .oxd-grid-item--gutters:nth-of-type(1) [tabindex]")))
        nationality_field.click()

        while nationality_field.text != 'Bangladeshi':
            nationality_field.send_keys(Keys.ARROW_DOWN)
        nationality_field.send_keys(Keys.ENTER)
        write_in_file("report.txt", "nationality: " + nationality_field.text + " selected successfully!")
    except Exception as e:
        write_in_file("report.txt", "Nationality field exception: " + type(e).__name__)
