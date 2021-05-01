from espol.PageLocators import FacultyLocator
from espol.PageElements import PageElement




class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class EdPage(BasePage):

    #buscarPaneles = searchPanels()

    def get_faculties_career(self):
        facultiesPanel = self.driver.find_elements(*FacultyLocator.FACULTY_PANELS)
        facultiesInfo = []
        for panel in facultiesPanel:
            titulo = self.search_title(panel)
            careers = self.search_careers(panel)
            for career in careers:
                info = []
                info.append(career[0])
                info.append(titulo)
                info.append(career[1])
                facultiesInfo.append(info)
        return facultiesInfo
        
    
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