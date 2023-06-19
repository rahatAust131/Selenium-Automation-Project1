from OrangeHRM.Necessary_Packages_Module.Necessary_Packages import *


def handle_blood_type():
    # Blood type field input checking
    try:
        blood_type_field = WebDriverWait(driver, 5, poll_frequency=1). \
            until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                    ".orangehrm-custom-fields [tabindex]")))
        blood_type_field.click()

        while blood_type_field.text != 'B+':
            blood_type_field.send_keys(Keys.ARROW_DOWN)
        blood_type_field.send_keys(Keys.ENTER)
        write_in_file("Log/report.txt", "Blood Type: " + blood_type_field.text + " selected successfully!")
    except Exception as e:
        write_in_file("Log/report.txt", "Blood Type field exception: " + type(e).__name__)
