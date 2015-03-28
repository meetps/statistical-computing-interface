# statistical-computing-interface
R based Statistical Computing Interface for easy statistical analysis and data visualization. 
A prototype application written in Django including basic features of displaying graphs from uploaded file data , OpenCPU R Computations etc.
## Features :
  * User Registration system 
  * Secure User Login System to prevent csrf attacks. 
  * Bar Graph output of uploaded data file  (csv for now other formats support soon). 
  * Line Graph output of uploaded data file (csv for now other formats support soon).
  * Mean of columns in the uploaded file displayed using R requests to OpenCPU Servers. (Linear Regression coming soon.)

##Installation 
  * Clone this repository using `git clone <Repo link here>`
  * Set up a virual environment in the same directory using `virtualenv <environment name>`
  * Activate your virtualenv using `source /<environment_name>/bin/activate`
  * Change your directory to statistical-computing-interface 
  * Install all dependencies using `pip install -r dependencies.txt`
  * Collect the static files using `python manage.py collectstatic`
  * Start the Django server `python manage.py runserver` 
  * Open up your browser and open up `127.0.0.1:8080/sciApp/register/` to see the application live.

##Why Django ?
  * Thousands of useful scientific and statistical python libraries can be harnessed which is not possible easily in PHP, Node.js. 
  * Django is utilized by a lot of modern organizations as it provides a lot of scalibity features such as models,  templateFillers etc which makes the interface future proof. 
  * No vulnerability to CSRF attacks.
  * Code is in Python hence lesser lines of code.
  * Statistical analysis is in pure python , hence future contribution from python community can be easy to get.
