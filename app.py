from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('modelRf_2_.pkl')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        error_message = 'El modelo no está disponible.'
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
                               columns=['Hour', 'Temperature', 'Humidity', 'DewPointTemperature', 'Seasons', 'FunctioningDay'])
        
        # Realizar predicciones
        prediction = model.predict(data_df)
        
        # Convertir la predicción a un tipo nativo de Python
        prediction_int = int(prediction[0])
        
        # Devolver las predicciones como respuesta JSON
        return jsonify({'Rented Bike Count': prediction_int})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
