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
def get_pacient_data(ID):
    global pacient_data
    data = consult_db(ID)
    #personal data
    pacient_data['name'] = data[0][1]
    pacient_data['last_name'] = data[0][2]
    pacient_data['bike'] = data[0][3]
    pacient_data['age'] = data[0][4]
    pacient_data['weight'] = data[0][5]
    pacient_data['height'] = data[0][6]
    pacient_data['gender'] = data[0][7]
    #cinematic data
    pacient_data['url_video'] = data[1][1]
    pacient_data['knee_min'] = data[1][2]
    pacient_data['knee_max'] = data[1][3]
    pacient_data['hip_min'] = data[1][4]
    pacient_data['hip_max'] =  data[1][5]
    pacient_data['shoulder_avg'] = data[1][6]
    img_id = data[1][1].split('/')[-1].split('_')[-1].replace('.avi', '').replace('prueba', '')
    # img_id = data[1][1].split('/')[-1].split('_')[-1].replace('.avi', '') para la nueva nomenclatura de nombrado
    pacient_data['img_id'] = img_id

    return pacient_data

