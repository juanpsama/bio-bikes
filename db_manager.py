import sqlite3
import enum
from sqlalchemy import create_engine, Column, Integer, String, Float, Enum 
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import relationship 
from sqlalchemy.orm import sessionmaker 
  
engine = create_engine('sqlite:///gfg.db', echo=True) 
Base = declarative_base() 
Session = sessionmaker(bind=engine) 
session = Session() 

Base.metadata.create_all(engine)
class GenderEnum(enum.Enum):
    FEMENINO = "Femenino"
    MASCULINO = "Masculino"
class Pacient(Base): 
    __tablename__ = 'pacients'
      
    id = Column(Integer, primary_key=True) 
    name = Column(String) 
    last_name = Column(String)
    bike_name = Column(String)
    age = Column(Integer) 
    weigth = Column(Float)
    height = Column(Float)
    gender = Column(Enum(GenderEnum))
    url_video = Column(String)  
    knee_min = Column(Float)
    knee_max = Column(Float)
    hip_min = Column(Float)
    hip_max=Column(Float)
    shoulder_avg=Column(Float)
    hip_translation_horizontal=Column(Float)
    hip_translation_vertical=Column(Float)
      
    # fees = relationship("Fee") 
connection = sqlite3.connect("database/BioBikes.db")
cursor = connection.cursor()
def get_last_id():
    return cursor.execute('''SELECT seq FROM sqlite_sequence WHERE name = "PACIENTES";''').fetchall()[0][0]
def save_database(pacient_data : dict ):
    global connection, cursor
    query = f"""INSERT INTO PACIENTES 
    (NAME , LAST_NAME,BIKE ,AGE , WEIGHT , HEIGHT, GENDER) 
    VALUES 
    ('{pacient_data["name"]}', '{pacient_data["last_name"]}', '{pacient_data["bike"]}', {pacient_data["age"]}, {pacient_data["weight"]}, {pacient_data["height"]}, '{pacient_data["gender"]}')"""
    cursor.execute(query)
    last_id = int(get_last_id())
    query = f"""INSERT INTO PARAMETROS 
        (ID_PACIENTE , URL_VIDEO , KNEE_MIN, KNEE_MAX, HIP_MIN, HIP_MAX, SHOULDER_AVG, HIP_TRASLATION_X, HIP_TRASLATION_Y) 
        VALUES 
        ({last_id}, '{pacient_data["url_video"]}', {pacient_data["knee_min"]}, {pacient_data["knee_max"]}, {pacient_data["hip_min"]}, {pacient_data["hip_max"]}, {pacient_data["shoulder_avg"]}, {pacient_data["hip_traslation_x"]}, {pacient_data["hip_traslation_y"]})"""
    cursor.execute(query)
    connection.commit()
    # connection.close()  
def consult_db(ID_paciente):  
    query_pacientes = f"""SELECT * FROM PACIENTES WHERE ID = {ID_paciente} ;"""
    query_parametros = f"""SELECT * FROM PARAMETROS WHERE ID_PACIENTE = {ID_paciente} ;"""
    data_paciente = cursor.execute(query_pacientes).fetchall()[0]
    data_parametros = cursor.execute(query_parametros).fetchall()[0]
    data = (data_paciente, data_parametros)
    # print(data)
    return data
    


# def saveParametrosData(url_video, knee_min, knee_max, hip_min, hip_max, shoulder_avg):
#     global connection, cursor
#     last_id = int(get_last_id())
#     query = f"""INSERT INTO PARAMETROS 
#         (ID_PACIENTE , URL_VIDEO , KNEE_MIN, KNEE_MAX, HIP_MIN, HIP_MAX, SHOULDER_AVG) 
#         VALUES 
#         ({last_id}, 'videos_out/{url_video}', {knee_min}, {knee_max}, {hip_min}, {hip_max}, {shoulder_avg})"""
#     cursor.execute(query)
#     connection.commit()
# def savePersonalData(name, last_name, bike, knee_ext, knee_flex, hip_ext, hip_flex, shoulder_mean, video_url):
#     global connection, cursor
#     query = f"""INSERT INTO PACIENTES 
#     (NAME, LAST_NAME, BIKE, AGE, WEIGHT,GENDER ,KNEE_EXT , KNEE_FLEX, HIP_EXT, HIP_FLEX, SHOULDER_MEAN, VIDEO_URL) 
#     VALUES 
#     ('{name}', '{last_name}', '{bike}', {knee_ext}, {knee_flex}, {hip_ext}, {hip_flex}, {shoulder_mean}, '{video_url}' )"""
#     cursor.execute(query)
#     connection.commit()
#     # connection.close()  
  
  
# Creating table
# table = """CREATE TABLE PACIENTES (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     NAME VARCHAR(255), 
#     LAST_NAME VARCHAR(255),
#     BIKE VARCHAR(255),
#     AGE INTEGER(3),
#     WEIGHT INTEGER(3),
#     HEIGHT INTEGER(3),
#     GENDER VARCHAR(20));"""
# cursor.execute(table)

# table = """CREATE TABLE PARAMETROS (
#     ID_PACIENTE INTEGER,
#     URL_VIDEO VARCHAR(255), 
#     KNEE_MIN FLOAT(3),
#     KNEE_MAX FLOAT(3),
#     HIP_MIN FLOAT(3),
#     HIP_MAX FLOAT(3), 
#     SHOULDER_AVG FLOAT(3),
#     HIP_TRASLATION_X FLOAT(3),
#     HIP_TRASLATION_Y FLOAT(3),
#     FOREIGN KEY(ID_PACIENTE) REFERENCES PACIENTES(ID) );"""
# cursor.execute(table)

# cursor.execute('UPDATE sqlite_sequence SET seq = 1;')
# cursor.execute('DELETE FROM PACIENTES;')
# cursor.execute('DELETE FROM PARAMETROS;')
# cursor.execute("""INSERT INTO PACIENTES 
#     (NAME , LAST_NAME,BIKE ,AGE , WEIGHT , HEIGHT, GENDER) 
#     VALUES 
#     ('Juan', 'Samayoa', 'Rockhopper', 21, 65, 170, 'masculino' )""")

# cursor.execute("""INSERT INTO PARAMETROS 
#     (ID_PACIENTE , URL_VIDEO , KNEE_MIN, KNEE_MAX, HIP_MIN, HIP_MAX, SHOULDER_AVG) 
#     VALUES 
#     (2, 'videos_img_out/video_prueba47', 27.5, 180.3, 22.2, 170.2, 33.2 )""")

# saveData('Juan Jose','Ancheyta', 'Ranger', 140.22, 23.1, 140.22, 23.1, 45.3, 'video/video_prueba13.avi')
# print("Data Inserted in the table: ")
# cursor.execute('''DROP TABLE PACIENTES;''')
# cursor.execute('''DROP TABLE PARAMETROS;''')
# data = cursor.execute('''SELECT seq FROM sqlite_sequence WHERE name = "PACIENTES";''')
# print(data.fetchall()[0][0])
# for row in data:
#     print(row)
connection.commit()

# connection.close()  
  

# Commit your changes in the database    


  