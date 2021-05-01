from selenium.webdriver.common.by import By


class FacultyLocator(object):
    #FACULTY_PANEL = (By.XPATH, "//div[@class='panel-default']/ancestor::div[@id='grado']")
    FACULTY_PANELS = (By.XPATH, "//div[@id='grado']//div[@class='panel panel-default']")
    FACULTY_TITTLE = (By.XPATH, ".//a[contains(text(), 'Facultad')]")
    FACULTY_CAREER = (By.XPATH, ".//li//a")
