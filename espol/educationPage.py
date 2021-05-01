from espol.PageLocators import FacultyLocator
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class EdPage(BasePage):

    facultiesInfo = []

    def get_faculties_info(self):
        return self.facultiesInfo

    def get_faculties_career(self):
        facultiesPanel = self.driver.find_elements(*FacultyLocator.FACULTY_PANELS)
        for panel in facultiesPanel:
            titulo = self.search_title(panel)
            careers = self.search_careers(panel)
            for career in careers:
                info = []
                info.append(career[0])
                info.append(titulo)
                info.append(career[1])
                self.facultiesInfo.append(info)
        return len(self.facultiesInfo)
    
    def search_acreditations(self):
        careers_with_acreditation = 0
        for index, item in enumerate(self.facultiesInfo, start=0):
            self.driver.get(item[2])
            acreditation = False
            try:
                acreditacion = self.driver.find_element(*FacultyLocator.ACREDITACION)
                if( acreditacion is not None ):
                    acreditation = True
                    careers_with_acreditation += 1
                else:
                    acreditation = False
            except NoSuchElementException:
                acreditacion = False
            self.facultiesInfo[index].append(acreditation)
        return careers_with_acreditation
    
    def search_title(self, panel):
        titulo = panel.find_element(*FacultyLocator.FACULTY_TITTLE)
        textTitulo = titulo.get_attribute('innerHTML').strip()
        return textTitulo
    
    def search_careers(self, panel):
        carreras = panel.find_elements(*FacultyLocator.FACULTY_CAREER)
        careerInfo = []
        for career in carreras:
            careerName = career.get_attribute('innerHTML')
            careerLink = career.get_attribute('href')
            careerInfo.append([careerName, careerLink])
        return careerInfo


class SearchResultsPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source