Task:

      Task is to  scrape a simple and real HTML web page,  learn how to parse the response using LXML, how to clean the scraped data, how to write the data whether to JSON or CSV files and finally  how to turn this code to a command line app where the user can specify a book page and where to store the data.
      
      Target web page: http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
      
      Refer to project_1 folder for the solution


Make sure python (preferred python3.7) is added to path.

    python --version
        or		
    python3.7 --version
 
 
 Install virtualenv using pip.

         pip install virtualenv 
 
First create a virtual environment for the project.

    virtualenv -p python3.7 venv or virtualenv venv
         . venv/bin/activate (Linux)
         . venv/Scripts/activate (windows)
         
## Install dependencies

        pip install -r requirements.txt
    
This will install all the dependencies (pylint, pycodestyle, flask) mentioned in the requirements file.


##Run using below command 

    python project_1/app.py  --bookurl='your url' --filename='your filename with json/csv extension'
                or
    python project_1/app.py (it will take default url and filename)
        