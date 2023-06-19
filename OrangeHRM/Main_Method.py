from Necessary_Packages import *
from Name_Handling import handle_names
from Login_Handling import handle_login_info
from My_Info_Handling import handle_my_info
from Employee_ID_Handling import handle_emp_id
from Driving_License_Handling import handle_driving_license
from SSN_Info_Handling import handle_ssn_and_sin_number
from Nationality_Handling import handle_nationality
from Marital_Status_Handling import handle_marital_status
from Date_Of_Birth_Handling import handle_date_of_birth
from Save_Button_Handling import handle_save_button
from Gender_Handling import handle_gender
from Military_Field_Handling import handle_military_service_field
from Smoker_Checker_Handling import handle_smoker_checker


def login_and_save_my_info():
    # checking if the title of the current url matches the homepage url
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert "https://opensource-demo.orangehrmlive.com" in driver.current_url, f"URL " \
                                                                                  f"mismatched!"

        write_in_file("report.txt", "----Data starts here----")
        write_in_file("report.txt", "Homepage opened successfully!")

        handle_login_info("Admin", "admin123")
        handle_my_info()
        handle_names()
        handle_emp_id()
        handle_driving_license()
        handle_ssn_and_sin_number()
        handle_nationality()
        handle_marital_status()
        handle_date_of_birth()
        handle_gender()
        handle_military_service_field()
        handle_smoker_checker()

        handle_save_button()

        write_in_file("report.txt", "-----Data ends here-----")

    except Exception as e:
        write_in_file("report.txt", "URL Exception:  " + type(e).__name__)


login_and_save_my_info()
