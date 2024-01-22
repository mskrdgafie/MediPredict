from django.shortcuts import render
from joblib import load

def index(request):
    loaded_model = load('disease_prediction_model.joblib')
    new_symptoms = request.get['symptoms']
    new_predictions = loaded_model.predict(new_symptoms)
    return render(request, 'index.html', {'new_predictions':new_predictions})