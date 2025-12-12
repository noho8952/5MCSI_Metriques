from flask import Flask, jsonify
from urllib.request import urlopen
import json

app = Flask(name)

@app.route('/tawarano/')
def meteo():
    response = urlopen(
        'https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx'
    )
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))

    results = []
    for element in json_content.get('list', []):
        dt_value = element.get('dt')
        temp_celsius = element.get('main', {}).get('temp') - 273.15
        results.append({
            'Jour': dt_value,
            'temp': temp_celsius
        })

    return jsonify(results=results)

if name == "main":
    app.run(debug=True)
