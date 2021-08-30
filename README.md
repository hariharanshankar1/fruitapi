# fruitapi
This is the coding challenge conducted by a company called OneValley. The main requirment is to collected data from [FruityVice](https://www.fruityvice.com/). 
And to display the images of fruits alone with a link to their information. 

My deployed Project is available here. 
[Project](https://hshankarfruitapi.herokuapp.com/)

## To run the project on your local machine follow these steps.
### Clone this repo into your directory.
``` mkdir imageview_project ``` 
``` cd imageview_project ```
``` git clone https://github.com/hariharanshankar1/fruitapi.git ```
### Create a virtual environment
``` python -m venv <environment name> ```
### Install all dependencies 
``` pip install -r requirements.txt ```
### Pull Data from the REST api
``` python data_load.py > ./fruit_grid_app/fixtures/data.json ```
### Updates the database with latest data
``` python manage.py loaddata ./fruit_grid_app/fixtures/data.json  ```
### Now migrate the data to the database
``` python manage.py migrate ```
### Finally Run the Application
``` python manage.py runserver ```
### View the project here.
``` http://127.0.0.1:8000/ ```
