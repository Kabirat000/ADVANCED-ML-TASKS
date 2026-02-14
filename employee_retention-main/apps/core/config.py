from datetime import datetime
import random

#Class for configuration instance attributes
class Config:
    def __init__(self):
        self.training_data_path = 'data/training_data'
        self.traing_database = 'training'
        self.prediction_data_path = 'data/prediction_data'
        self.prediction_database= 'prediction'

    #method to generate run id
    def get_run_id(self):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H%M%S")
        return str(self.date)+"_"+str(self.current_time)+"_"+str(random.randint(100000000, 999999999))
