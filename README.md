# Job Application Script for Career Fair
  
A one-time simple automated job application script.

## Instructions  
  
**Note:** Does not include writing elevator pitch when submitting your job application.  
  
**1. In order to initialise virtual environment in preferred Python version, perform the following command in your command terminal at your preferred directory.**  
  
```sh  
py -(version) -m venv env  
```  
  

**2. Activate virtual environment.**  

*On macOS and Linux:*  
```sh
source env/bin/activate
```  

*On Windows:*  
```sh
.\env\Scripts\activate
```  
  
  
**3. Install Selenium.**  
  
```sh
pip install Selenium
```  
   
https://pypi.org/project/selenium/  
  
Requires: Python 2.7, 3.4+
  
  
**3. Install preferred web driver in a chosen directory.**  
   
*Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads*  
*Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/*  
*Firefox: https://github.com/mozilla/geckodriver/releases*  
*Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/*  
  
  
**4. Install dotenv.**  
  
```sh
pip install python-dotenv
```  
   
https://pypi.org/project/python-dotenv/
  
  
**5. Open a new command terminal at the same directory. Perform a git clone.**
```sh
git clone https://github.com/snwl123/Automated-Job-Application-Script.git
```
Close command terminal if necessary.  
  

**6. In the script 'job_application.py', add urls of the job descriptions to the list of websites.**  
  
```
websites = [
    https://www.jobstreet.com.sg/en/job/8348181?icmpid=vcfsg%3A20210301,  
    https://www.jobstreet.com.sg/en/job/8368337?icmpid=vcfsg%3A20210301  
]
```  
  
  
**7. Run command to automate submission of job applications.**  
```sh
py job_application.py
```  
  
  
  
**8. Deactivate virtual environment.**  
```sh
deactivate
```
  
  
## Additional Information
  
Not yet implemented checking for webpage title.
  
-  For more information on virtual environments:   
   https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/  



