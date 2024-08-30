from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize the Flask application
application = Flask(__name__)
app = application

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling prediction requests
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Collect data from the form
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        # Convert data to a DataFrame
        pred_df = data.get_data_as_data_frame()
        print("Input DataFrame:")
        print(pred_df)
        print("Before Prediction")

        # Initialize the prediction pipeline
        predict_pipeline = PredictPipeline()
        print("Mid Prediction")

        # Make predictions
        try:
            results = predict_pipeline.predict(pred_df)
            print("After Prediction")
            print(f"Prediction Result: {results[0]}")
        except Exception as e:
            print(f"An error occurred during prediction: {e}")
            return render_template('home.html', error=str(e))

        # Return the result to the user
        return render_template('home.html', results=results[0])

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

