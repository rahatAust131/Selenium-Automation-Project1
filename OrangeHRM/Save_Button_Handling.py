from Necessary_Packages import *


def handle_save_button():
    # Save button checking
    try:
        save_btn = WebDriverWait(driver, 5, poll_frequency=1).until(EC.visibility_of_element_located(((By.CSS_SELECTOR,
                                                                                                       ".orangehrm-edit-employee-content .orangehrm-vertical-padding:nth-of-type(1) .oxd-button--secondary"))))
        save_btn.click()
        time.sleep(3)
        write_in_file("report.txt", "Save button clicked successfully!")
    except Exception as e:
        write_in_file("report.txt", "Save button click exception: " + type(e).__name__)
