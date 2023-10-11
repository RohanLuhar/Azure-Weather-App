# Azure-Weather-App
This is a simple Weather Application made using Flask (Python).

Steps involved:
1. Create an empty folder for your application.
2. Create a virtual environment for your project by typing following command in the terminal.
   python -m venv venv
3. Now, activate the virtual environment, using:
   For windows: ./venv/Scripts/activate
   For Linux  : source venv/Scripts/activate
4. Download Flask and Requests using following commands:
   pip install Flask
   pip install requests
5. Create a subfolder named 'app' and create the project files including both frontend and backend.
   To use OpenWeatherMap API, sign up on https://openweathermap.org/ and get your API key and read its documentation to use      the API efficiently.
   To use Azure Translator API, create Translator service in your Azure account.
7. Define the start point by creating startup.py file.
8. Install requiremnts using:
   pip freeze > requiremnets.txt
9. To configure launch.json file, execute following commands in your terminal:
   $Env:FLASK_APP:"startup:app"
   $Env:FLASK_ENV:"development"
10. Now you can run your poject by executing:
    run flask
11. Sync all your file in a separate Github repository.

Steps to deploy on Azure:
1. Create an App Service in your Azure and choose free plan.
   This will get you a default microsoft website.
2. Now, go to Configuration > General Settings, and save it after writing the following 'Startup Command':
   gunicorn --bind=0.0.0.0 --timeout 600 startup:app

3. Go to Deployment Center.
   Signin into your Github there, choose repository and save it.
4. You can finally browse your webapp from the mentioned url in Overview section.


  ![Screenshot 2023-10-11 150137](https://github.com/RohanLuhar/Azure-Weather-App/assets/99538858/9c8494c0-9e83-4636-96aa-97b295ba9aeb)


Requirements:
1. Flask 3.0.0
2. Python 3.11.1
3. Microsoft Azure Subscription
4. OpenWeatherMap API

References:
1. https://flask.palletsprojects.com/en/3.0.x/
2. https://learn.microsoft.com/en-us/azure/ai-services/translator/
3. https://openweathermap.org/
