from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
app = Flask(__name__)

with open('regression_model.pkl','rb') as file:
    model = pickle.load(file)

with open('Scaler (1).pkl','rb') as file:
    scaler = pickle.load(file)

num_cols_std=['winery', 'wine', 'year', 'rating', 'num_reviews', 'region', 'type',
    'body', 'acidity']

features_to_log1p=['winery', 'wine', 'year', 'rating', 'num_reviews', 'region', 'type',
    'body', 'acidity']

@app.route('/')
def home():
    return render_template('form.html',prediction ="")

@app.route('/Predict', methods = ['POST'])
def index():

    input_data = {
    'winery':request.form['winery'],
    'wine':request.form['wine'],
    'year':int(request.form['year']),
    'rating':float(request.form['rating']),
    'num_reviews':int(request.form['num_reviews']),
    'region':request.form['region'],
    'type':request.form['type'],
    'body':float(request.form['body']),
    'acidity':float(request.form['acidity'])
}
    input_df = pd.DataFrame([input_data])

    input_df['winery'] = LabelEncoder().fit_transform(input_df['winery'])
    input_df['wine'] = LabelEncoder().fit_transform(input_df['wine'])
    input_df['region'] = LabelEncoder().fit_transform(input_df['region'])
    input_df['type'] = LabelEncoder().fit_transform(input_df['type'])
    input_df[num_cols_std] = scaler.transform(input_df[num_cols_std])
    input_df[features_to_log1p] = input_df[features_to_log1p].apply(np.log1p)
    
    # Predict
    prediction = model.predict(input_df)[0]

    # If model predicted log(price), convert back
    predicted_price = np.expm1(prediction)

    return render_template('form.html', prediction=f"Predicted Wine Price: ${predicted_price:.2f}")


if __name__ == '__main__':
    app.run(debug=True) 