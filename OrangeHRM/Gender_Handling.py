from Necessary_Packages import *


def handle_gender():
    # Gender Field checking
    try:
        gender_male_field = WebDriverWait(driver, 5, poll_frequency=1). \
            until(EC.visibility_of_element_located
                  ((By.CSS_SELECTOR, ".--gender-grouped-field .oxd-input-field-bottom-space:nth-of-type(1) label")))

        gender_female_field = WebDriverWait(driver, 5, poll_frequency=1). \
            until(EC.visibility_of_element_located
                  ((By.CSS_SELECTOR, ".--gender-grouped-field .oxd-input-field-bottom-space:nth-of-type(2) label")))

        gender_female_field.click()
        write_in_file("report.txt", "Gender: " + gender_female_field.text + " selected!")

    except Exception as e:
        write_in_file("report.txt", "Gender field exception: " + type(e).__name__)
