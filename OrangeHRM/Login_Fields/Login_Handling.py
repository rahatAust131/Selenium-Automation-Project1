from OrangeHRM.Necessary_Packages_Module.Necessary_Packages import *


def handle_login_info(username, password):
    # username field checking
    try:
        username_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='username']")))
        username_field.send_keys(username)
        write_in_file("Log/report.txt", "username typed successfully!")
    except Exception as e:
        write_in_file("Log/report.txt", "username field exception: " + type(e).__name__)

    # password field checking
    try:
        password_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='password']")))
        password_field.send_keys(password)
        write_in_file("Log/report.txt", "password typed successfully!")
    except Exception as e:
        write_in_file("Log/report.txt", "password field exception: " + type(e).__name__)

    # button checking
    try:
        login_btn = WebDriverWait(driver, 5, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))
        login_btn.click()
        write_in_file("Log/report.txt", "Login button clicked successfully!")

        assert "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index" in driver.current_url, f"Dashboard URL mismatched!"
        write_in_file("Log/report.txt", "Dashboard page opened successfully!")

    except Exception as e:
        write_in_file("Log/report.txt", "button click exception: " + type(e).__name__)
