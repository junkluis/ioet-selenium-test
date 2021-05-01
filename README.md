## The Aproach

First, we create a skeleton of the project with the basic elements of the web page. We define a test case. For this example, we try to locate careers on the ESPOL website and save them in a CSV file.
The functions created for the test are on the education page, so it can be reused in different test cases.
All the locators are found on pageLocators as constants. I use basically two different types: absolutes (root) and relative. My approach tries to isolate the main component (Faculty block) and then find what I need within the webElement (Faculty name and careers)

Main Sources
* [Page Objects design pattern](https://selenium-python.readthedocs.io/page-objects.html)
* [XPATH Strategies](http://pragmatictestlabs.com/2020/01/28/mastering-xpath-for-selenium-test-automation-engineers/)


## Getting Started

### Prerequisites
Python Lib
```
    selenium
    unittest
    csv
```

Chrome Driver
```
    /driver/chromedriver.exe    --version: 90.0.4430.24
```

## Usage

python website-test.py


<!-- CONTACT -->
## Contact

Luis Zuñiga Rosado - [@junkluis](https://twitter.com/junkluis) - lufezuro@gmail.com

Project Link: [https://github.com/junkluis/ioet-selenium-test](https://github.com/junkluis/ioet-selenium-test)
