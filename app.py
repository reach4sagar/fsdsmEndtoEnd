from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import sys

from flask import Flask,request,render_template,jsonify

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    
    if request.method == "GET":
        return render_template("form.html")
    
    else:
        data=CustomData(
            
            carat=float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        # this is my final data
        final_data=data.get_data_as_dataframe()
        
        logging.info("starting prediction")
        
        try:
            predict_pipeline=PredictPipeline()

        except Exception as e:
            raise customexception(e,sys) 
        
        logging.info("started with prediction")
        pred=predict_pipeline.predict(final_data)
        
        result=round(pred[0],2)
        
        return render_template("result.html",final_result=result)

#execution befin
if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080)