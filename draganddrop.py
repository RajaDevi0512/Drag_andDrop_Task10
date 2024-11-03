from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, NoSuchDriverException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# Class to hold url
class Data:
    url = 'https://jqueryui.com/droppable/'

# Class to hold source and target element
class Locator:
    source_element = 'draggable'
    target_element = 'droppable'

class DragAndDrop(Data, Locator):
    def __init__(self):
        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.action = ActionChains(self.driver)
        except NoSuchDriverException as error:
            print("Error:", error)

    def drag_and_drop(self):
        try: 
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)

            # Switch to the iframe that contains the drag-and-drop elements
            iframe = self.driver.find_element(By.CSS_SELECTOR, ".demo-frame")
            self.driver.switch_to.frame(iframe)

            # Locate source and target elements within the iframe
            iframe_source_element = self.driver.find_element(By.ID, self.source_element)
            iframe_target_element = self.driver.find_element(By.ID, self.target_element)

            # Perform drag and drop
            self.action.drag_and_drop(iframe_source_element, iframe_target_element).perform()
            print("SUCCESS: Drag and Drop completed!")
            
            # Switch back to the main content if needed
            self.driver.switch_to.default_content()

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("Element is not visible!", error)
        finally:
            self.driver.quit()

# Execute the drag-and-drop action
my_actions = DragAndDrop()
my_actions.drag_and_drop()
