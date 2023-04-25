from database import *
class Paciente():
    def __init__(self):
        pass
        # self.knee_ext = knee_ext #, knee_ext, knee_flex, hip_ext, hip_fle, shoulder_mean, video_url
        # self.knee_flex = knee_flex
        # self.hip_ext = hip_ext
        # self.hip_fle = hip_ext
        # self.shoulder_mean = shoulder_mean
        # self.video_url = video_url
    def set_personal_data(self,name, last_name, bike, age, weight, height, gender):
        self.name = name
        self.last_name = last_name
        self.bike = bike
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        savePersonalData(self.name, self.last_name, self.bike, self.age, self.weight, self.height, self.gender)
        print(self.name, self.last_name)