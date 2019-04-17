edyst-s19-diy-pokedex
================
This is a api which will get the details of pokemon through thier ID.

`Python` and `Flask` framework should be pre intalled.

Virtual environment should be created to execute the program.

'python app.py' command at current working directory will execute the program.

Then you will be provided with a link on which you can test the API or Postman also can be used for this.

Route-'http://localhost:8006/api/pokemon/:id' id can vary from '1' to '807'

`app.py` is the API programm.

`pokedata.py` is the program used for extracting data into a json file to tackle the situation when the external API is down

The script pokedata.py can be run every once in 24 hours by using Task schedular.

------------------

Steps :

->create a new task

->In general name your task.

->In action add new and set the action for python in scripts and in arguments name the python file and then add the location of python file.

->In triggers set the time for 1 day ie 24 hours.

->Then click ok and run