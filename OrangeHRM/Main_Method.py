# importing necessary packages and modules
from OrangeHRM.Necessary_Packages_Module.Necessary_Packages import *
from OrangeHRM.All_Name_Fields.Name_Handling import handle_names
from OrangeHRM.Login_Fields.Login_Handling import handle_login_info
from OrangeHRM.My_Info_Button.My_Info_Handling import handle_my_info
from OrangeHRM.Employee_ID_Field.Employee_ID_Handling import handle_emp_id
from OrangeHRM.Driving_License_Field.Driving_License_Handling import handle_driving_license
from OrangeHRM.SSN_And_SIN_Number_Fields.SSN_Info_Handling import handle_ssn_and_sin_number
from OrangeHRM.Nationality_Field.Nationality_Handling import handle_nationality
from OrangeHRM.Marital_Status_Field.Marital_Status_Handling import handle_marital_status
from OrangeHRM.Date_Of_Birth_Field.Date_Of_Birth_Handling import handle_date_of_birth
from OrangeHRM.Save_Button.Save_Button_Handling import handle_save_button
from OrangeHRM.Gender_Field.Gender_Handling import handle_gender
from OrangeHRM.Military_Service_Field.Military_Field_Handling import handle_military_service_field
from OrangeHRM.Smoker_Checker_Field.Smoker_Checker_Handling import handle_smoker_checker
from OrangeHRM.Blood_Type_Field.Blood_Type_Handling import handle_blood_type
from OrangeHRM.Custom_Field_Save_Button.Custom_Field_Save_Button_Handling import handle_custom_field_save_button


def login_and_save_my_info():
    try:
        write_in_file("Log/report.txt", "\n----Data starts here----\n")
        # checking if the title of the current url matches the homepage url
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert "https://opensource-demo.orangehrmlive.com" in driver.current_url, f"URL " \
                                                                                  f"mismatched!"

        write_in_file("Log/report.txt", "Homepage opened successfully!")
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
        write_in_file("Log/report.txt", "\n-----Data ends here-----\n")

    except Exception as e:
        write_in_file("Log/report.txt", "URL Exception:  " + type(e).__name__)


login_and_save_my_info()
