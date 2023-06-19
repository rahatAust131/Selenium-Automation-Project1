from OrangeHRM.Necessary_Packages_Module.Necessary_Packages import *


def handle_page_scroll_down(scroll_height):
    try:
        driver.execute_script(f"window.scrollTo(0,document.body.scrollHeight/{scroll_height})")
        # time.sleep(3)
    except Exception as e:
        print("Context scroll Exception: ", type(e).__name__)
