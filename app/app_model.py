
from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('app/model/model.pkl')
app.logger.debug('Modelo cargado correctamente.')

@app.route('/')
def home():
    return render_template('model.html')

@app.route('/predict_model', methods=['POST'])
def predict():
    try:
        # Obtener los datos enviados en el request
        date = float(request.form['Date'])
        d4046 = float(request.form['4046'])
        d4225 = float(request.form['4225'])
        region = float(request.form['region'])
        type = float(request.form['type'])
        Large_Bags = float(request.form['Large_Bags'])
        
        # Crear un DataFrame con los datos
        data_df = pd.DataFrame([[date,d4046,d4225,region,type,Large_Bags]], columns=['date','d4046','d4225','region','type','Large Bags'])
        app.logger.debug(f'DataFrame creado: {data_df}')
        
        # Realizar predicciones
        prediction = model.predict(data_df)
        app.logger.debug(f'Predicción: {prediction[0]}')
        
        # Devolver las predicciones como respuesta JSON
        return jsonify({'price': prediction[0]})
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

