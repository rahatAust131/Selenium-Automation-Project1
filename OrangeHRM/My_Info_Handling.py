from Necessary_Packages import *

def handle_my_info():
    # my info button click
    try:
        my_info_btn = WebDriverWait(driver, 5, poll_frequency=1).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".oxd-sidepanel-body .oxd-main-menu-item-wrapper:nth-of-type(6) .oxd-main-menu-item")))
        my_info_btn.click()
        write_in_file("report.txt", "My Info button clicked successfully!")
        assert "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7" in driver.current_url, f"My Info URL mismatched!"
        write_in_file("report.txt", "My Info Page opened successfully!")
    except Exception as e:
        write_in_file("report.txt", "My Info button click exception: " + type(e).__name__)