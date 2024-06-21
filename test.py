from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

cust=CustomData(1.52,62.2,58.0,7.27,7.33,4.455,"Premium","F","VS2")
data=cust.get_data_as_dataframe()

print(data)