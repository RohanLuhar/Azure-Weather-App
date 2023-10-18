import requests, os, uuid, json
from flask import Flask, render_template, request
import requests

key = "a35a7b73b2374ad2896b197d61f332b8"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "centralindia"
path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['hi','gu']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    try:
        if request.method == 'POST':
            city_name = request.form['name']
            print(type(city_name))
            if (len(city_name) == 0):
                return render_template('invalid.html')
            else:
                url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=3c6d6137fff8654d1f2f4cdff76b0698'
                response = requests.get(url.format(city_name)).json()
                
                temp = response['main']['temp']
                weather = response['weather'][0]['description']
                min_temp = response['main']['temp_min']
                max_temp = response['main']['temp_max']
                icon = response['weather'][0]['icon']
                print(city_name,temp,weather,min_temp,max_temp,icon)
                
                body = [
                    {'text': temp},
                    {'text': weather},
                    {'text': min_temp},
                    {'text': max_temp},
                    {'text': city_name},
                ]

                requestt = requests.post(constructed_url, params=params, headers=headers, json=body)
                response = requestt.json()
                temp_hindi = response[0]['translations'][0]['text']
                weather_hindi = response[1]['translations'][0]['text']
                min_temp_hindi = response[2]['translations'][0]['text']
                max_temp_hindi = response[3]['translations'][0]['text']    
                city_name_hindi = response[4]['translations'][0]['text']

                return render_template('index.html',
                                    temp = temp,
                                    temp_hindi=temp_hindi,
                                    weather=weather.title(),
                                    weather_hindi=weather_hindi,
                                    min_temp=min_temp,
                                    min_temp_hindi=min_temp_hindi,
                                    max_temp=max_temp,
                                    max_temp_hindi=max_temp_hindi,
                                    icon=icon,
                                    city_name=city_name.upper(),
                                    city_name_hindi=city_name_hindi) 
        
        else:
            return render_template('index.html')
    
    except:
        return render_template('invalid.html')
    
    

def null_search():
    msg = "Please enter valid location"
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')


        



# # Add your key and endpoint
# key = "a35a7b73b2374ad2896b197d61f332b8"
# endpoint = "https://api.cognitive.microsofttranslator.com"

# # location, also known as region.
# # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
# location = "centralindia"

# path = '/translate'
# constructed_url = endpoint + path

# params = {
#     'api-version': '3.0',
#     'from': 'en',
#     'to': ['hi']
# }

# headers = {
#     'Ocp-Apim-Subscription-Key': key,
#     # location required if you're using a multi-service or regional (not global) resource.
#     'Ocp-Apim-Subscription-Region': location,
#     'Content-type': 'application/json',
#     'X-ClientTraceId': str(uuid.uuid4())
# }

# # You can pass more than one object in body.
# body = [{
#     'text': 'I would really like to drive your car around the block a few times!'
# }]

# request = requests.post(constructed_url, params=params, headers=headers, json=body)
# response = request.json()

# print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
