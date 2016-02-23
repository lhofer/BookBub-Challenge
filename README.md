#BookBub Challenge
##Leila Hofer
##2/22/2016

##Requirments:
######Note: Requirements can be installed without virtual environment but since I use it on my computer, the start up instructions include it
1. Virtual environment
  * (mac) $ sudo easy_install virtualenv  
  * (windows) $ sudo apt-get install python-virtualenv
  * to start cd into project folder and first type:
   ** (mac/windows) $ virtualenv venv   
   #####then one of the following   
   ** (mac) $ . venv/bin/activate   
   ** (windows) $ venv\scripts\activate   
2. NLTK:
  * (mac) $ pip install nltk
  *	(Windows) see http://www.nltk.org/install.html

##Usage:
$ python genres.py csv_file.csv book_description_file.json
