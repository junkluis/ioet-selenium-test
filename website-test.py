from selenium import webdriver
import toolbox
import espol.educationPage
import unittest
import time
import espol.educationPage as educationPage


class espolCareerInformation(unittest.TestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome('driver/chromedriver.exe')
        self.driver.get('http://www.espol.edu.ec/es/educacion')
    
    def test_search_in_python_org(self):

        page = educationPage.EdPage(self.driver)
        info = page.get_faculties_career()
        csv = toolbox.CSVtools()
        header = ['career_name_es', 'faculty_name', 'link_to_career_curriculum']
        csv.infoToCSV(info, header)

        self.assertEqual(1,1)
        #print(str(page.buscarPaneles))
        # main_page = educationPage.MainPage( self.driver )
        # assert search_results_page.is_results_found( )
    
    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()




"""

driver = webdriver.Chrome('driver/chromedriver.exe')
driver.get('http://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()

time.sleep(5)
driver.quit()

"""