## mtaa_yangu

## Author
Ndundiro Kamau 

## Description
Mtaa_yangu is a web application that allows users to be in the loop about everything happening in their neighborhood. From contact information of different businesses to meeting announcements or even alerts.

## Live Link 
[click here](https://mtaa_yangu.herokuapp.com/) view the live site.

## SetUp/Installations
1. Download the zip file of the project or Clone the repository using the following command:
git clone ```https://github.com/Ndundiro/mtaa_yangu```

Navigate to the project directory
```cd NEIGHBOURHOOD-IP```

2. Virtual Environment
Install virtualenv  using pip:  
```python3.6 -m venv virtual```  
Proceed to activate the virtual environment   
```source virtual/bin/activate```

3. Install packages/dependancies  
Install the packages in the requirements.txt file:  
```pip install -r requirements.txt```

4. Create a database
Create a new postgress database,Type the following command  
psql  
Run the following command,it creates a new database named gallery1  
```#create database mtaa```

5. Create Database migrations
run the following command:    
 ```python3 manage.py makemigrations Mtaa_yangu```
followed by:    
 ```python3 manage.py migrate```

6. Run the app
To run the application:  
```python3 manage.py runserver``` 

Open  the link http://127.0.0.1:8000/  in a browser.

7. To run tests:  
```python3 manage.py test```

For more Information,Read the following documents:

* [DjangoDocumentation](https://docs.djangoproject.com/en/1.11/)
* [PythonDocumentation](https://docs.python.org/3.6/)

User Story

A user should be able to:
1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the health department and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.

## Bugs
There are no known bugs yet

## Technologies Used
* Python3.6
* Django 2.20
* PostgreSQL
* HTML5
* CSS3
* Heroku

### Dependencies
* Postgresql

## Support and Contact Details
For any comments,suggestions,feedback or inquiries, contact me via email: ndundirokamau@gmail.com

## License
[MIT License](https://github.com/Ndundiro/Project-Rank/blob/master/LICENSE)

Copyright © 2019 Ndundiro Kamau