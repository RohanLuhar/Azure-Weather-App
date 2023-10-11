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
1. Create a Resource Group.
   ![Screenshot 2023-10-11 150733](https://github.com/RohanLuhar/Azure-Weather-App/assets/99538858/04ee3cbf-d042-45a6-b5a7-0857b68c9a9f)
   
2. Create a Web App Service in your Azure.
   Enter a unique name for your app service and linux plan.
   Select Python 3.11.1 as runtime stack, Central India as region, and Free F1 as pricing plan.
   Hit Review + Create.
   It will take under less than 1 minute to deploy your website. Click on 'Go to resource'.
![Screenshot 2023-10-11 151325](https://github.com/RohanLuhar/Azure-Weather-App/assets/99538858/cd3e4b9e-3c71-4820-b62b-ecf17d6f28b9)
   ![Screenshot 2023-10-11 151421](https://github.com/RohanLuhar/Azure-Weather-App/assets/99538858/b32f69de-9aee-483d-93a0-5af6144b5063)
   
4. Now, go to Configuration > General Settings, and save it after writing the following 'Startup Command':
   gunicorn --bind=0.0.0.0 --timeout 600 startup:app
   ![Screenshot 2023-10-11 150137](https://github.com/RohanLuhar/Azure-Weather-App/assets/99538858/9c8494c0-9e83-4636-96aa-97b295ba9aeb)
   
5. Go to Deployment Center.
   Signin into your Github there, choose repository, choose branch and save it.
   
   
7. You can finally browse your webapp from the mentioned url in Overview section.
![Screenshot 2023-10-11 150103](https://github.com/RohanLuhar/Azure-Weather-App/assets/99538858/08b1d00c-71cc-4a85-8da7-ac18a93abaaf)


Requirements:
1. Flask 3.0.0
2. Python 3.11.1
3. Microsoft Azure Subscription
4. OpenWeatherMap API

References:
1. https://flask.palletsprojects.com/en/3.0.x/
2. https://learn.microsoft.com/en-us/azure/ai-services/translator/
3. https://openweathermap.org/
