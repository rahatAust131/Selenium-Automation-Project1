from Necessary_Packages import *


def handle_custom_field_save_button():
    # Custom field Save button checking
    try:
        save_btn = WebDriverWait(driver, 5, poll_frequency=1).until(EC.visibility_of_element_located(((By.CSS_SELECTOR,
                                                                                                       ".orangehrm-custom-fields .oxd-button--secondary"))))
        save_btn.click()
        time.sleep(3)
        write_in_file("report.txt", "Custom field Save button clicked successfully!")
    except Exception as e:
        write_in_file("report.txt", "Custom field Save button click exception: " + type(e).__name__)
