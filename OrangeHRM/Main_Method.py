# importing necessary packages and modules
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
from Blood_Type_Handling import handle_blood_type
from Custom_Field_Save_Button_Handling import handle_custom_field_save_button


def login_and_save_my_info():
    # checking if the title of the current url matches the homepage url
    try:
        write_in_file("report.txt", "\n----Data starts here----\n")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert "https://opensource-demo.orangehrmlive.com" in driver.current_url, f"URL " \
                                                                                  f"mismatched!"

        write_in_file("report.txt", "Homepage opened successfully!")
        """
        user login is checked here with the username and password information
        """
        handle_login_info("Admin", "admin123")
        """
        my info button click is checked here
        """
        handle_my_info()
        """
        usernames (firstname, middlename and lastname) fields are checked here
        """
        handle_names()
        """
        employee id and other id fields are checked here
        """
        handle_emp_id()
        """
        driving license field and license expiry date field are checked here
        """
        handle_driving_license()
        """
        ssn and sin number fields are checked here
        """
        handle_ssn_and_sin_number()
        """
        nationality (dropdown) field is checked here
        """
        handle_nationality()
        """
        marital status (dropdown) field is checked here
        """
        handle_marital_status()
        """
        Date of birth field is checked here
        """
        handle_date_of_birth()
        """
        Gender field is checked here
        """
        handle_gender()
        """
        Military service field is checked here
        """
        handle_military_service_field()
        """
        Smoker Checker field is checked here
        """
        handle_smoker_checker()
        """
        Save button click is checked here
        """
        handle_save_button()

        """
        Custom field : Blood Type (dropdown) field is checked here
        """
        handle_blood_type()
        """
        Custom field save button click is checked here
        """
        handle_custom_field_save_button()

        time.sleep(3)
        write_in_file("report.txt", "\n-----Data ends here-----\n")

    except Exception as e:
        write_in_file("report.txt", "URL Exception:  " + type(e).__name__)


login_and_save_my_info()
