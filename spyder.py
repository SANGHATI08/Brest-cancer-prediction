from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()
class model_input(BaseModel):
    radius_mean : float
    texture_mean  : float
    perimeter_mean : float
    area_means : float
    smoothness_mean : float
    compactness_mean : float
    concavity_mean : float
    concave_points_mean : float
    symmetry_mean : float
    fractal_dimension_mean : float
    radius_se : float
    texture_se : float
    perimeter_se : float
    area_se : float
    smoothness_se : float
    compactness_se : float
    concavity_se : float
    concave_points_se : float
    symmetry_se : float
    fractal_dimension_se : float
    radius_worst : float
    texture_worst : float
    perimeter_worst : float
    area_worst : float
    smoothness_worst : float
    compactness_worst : float
    concavity_worst : float
    concave_points_worst : float
    symmetry_worst : float
    fractal_dimension_worst : float
    

#loading the saved model
model = pickle.load(open("D:/san/breast cancer classificatin/trained_model (1).sav",'rb'))

@app.post('/cancer_prediction')
def pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)  ##converting json to dict
    
    radius_mean = input_dictionary('radius_mean')
    texture_mean = input_dictionary('texture_mea')
    perimeter_mean = input_dictionary('perimeter_mean')
    area_means = input_dictionary('area_means')
    smoothness_mean = input_dictionary('smoothness_mean')
    compactness_mean = input_dictionary('compactness_mean')
    concavity_mean = input_dictionary('concavity_mean')
    concave_points_mean = input_dictionary('concave_points_mean')
    symmetry_mean = input_dictionary('symmetry_mean')
    fractal_dimension_mean = input_dictionary('fractal_dimension_mean')
    radius_se = input_dictionary('radius_se')
    texture_se = input_dictionary('texture_se')
    perimeter_se = input_dictionary('perimeter_se')
    area_se = input_dictionary('area_se')
    smoothness_se = input_dictionary('smoothness_se')
    compactness_se = input_dictionary('compactness_se')
    concavity_se = input_dictionary('concavity_se')
    concave_points_se = input_dictionary('concave_points_se')
    symmetry_se = input_dictionary('symmetry_se')
    fractal_dimension_se = input_dictionary('fractal_dimension_se')
    radius_worst = input_dictionary('radius_worst')
    texture_worst = input_dictionary('texture_worst')
    perimeter_worst = input_dictionary('perimeter_worst')
    area_worst = input_dictionary('area_worst')
    smoothness_worst = input_dictionary('smoothness_worst')
    compactness_worst = input_dictionary('compactness_worst')
    concavity_worst = input_dictionary('concavity_worst')
    concave_points_worst = input_dictionary('concave_points_worst')
    symmetry_worst = input_dictionary('symmetry_worst')
    fractal_dimension_worst = input_dictionary('fractal_dimension_worst')
    
    
    input_list = [radius_mean, texture_mean, perimeter_mean, area_means, smoothness_mean, compactness_mean , concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]
    
    prediction = model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The  type is Malignant'
    
    else:
        return 'It is Benign'
    
    

















