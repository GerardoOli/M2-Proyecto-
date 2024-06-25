from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('modelRf_2_.pkl')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        error_message = 'El modelo no está disponible.'
        app.logger.error(error_message)
        return jsonify({'error': error_message}), 500
    
    try:
        # Obtener los datos enviados en el request
        hour = float(request.form['Hour'])
        temperature = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        dew_point_temperature = float(request.form['DewPointTemperature'])
        seasons = float(request.form['Seasons'])
        functioning_day = float(request.form['FunctioningDay'])
        
        # Crear un DataFrame con los datos
        data_df = pd.DataFrame([[hour, temperature, humidity, dew_point_temperature, seasons, functioning_day]], 
                               columns=['Hour', 'Temperature(°C)', 'Humidity(%)', 'Dew point temperature(°C)', 'Seasons', 'Functioning Day'])
        app.logger.debug(f'DataFrame creado: {data_df}')
        
        # Realizar predicciones
        prediction = model.predict(data_df)
        app.logger.debug(f'Predicción: {prediction[0]}')
        
        # Convertir la predicción a un tipo nativo de Python
        prediction_int = int(prediction[0])
        
        # Devolver las predicciones como respuesta JSON
        return jsonify({'Rented Bike Count': prediction_int})
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
