from db_manager import *

pacient_data = {}
def set_personal_data(name, last_name, bike, age, weight, height, gender):
    global pacient_data
    pacient_data['name'] = name
    pacient_data['last_name'] = last_name
    pacient_data['bike'] = bike
    pacient_data['age'] = age
    pacient_data['weight'] = weight
    pacient_data['height'] = height
    pacient_data['gender'] = gender
    # savePersonalData(self.name, self.last_name, self.bike, self.age, self.weight, self.height, self.gender)
    # print(self.name, self.last_name)
def set_goniometric_data(url_video, knee_min, knee_max, hip_min, hip_max, shoulder_avg):
    global pacient_data
    pacient_data['url_video'] = url_video
    pacient_data['knee_min'] = knee_min
    pacient_data['knee_max'] = knee_max
    pacient_data['hip_min'] = hip_min
    pacient_data['hip_max'] =  hip_max
    pacient_data['shoulder_avg'] = shoulder_avg
def save_data():
    global pacient_data
    save_database(pacient_data)
    pacient_data = {}