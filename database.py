import sqlite3

connection = sqlite3.connect("database/BioBikes.db")
cursor = connection.cursor()
def get_last_id():
    return cursor.execute('''SELECT seq FROM sqlite_sequence WHERE name = "PACIENTES";''').fetchall()[0][0]
def savePersonalData(name, last_name, bike, age, weight, height, gender):
    global connection, cursor
    query = f"""INSERT INTO PACIENTES 
    (NAME , LAST_NAME,BIKE ,AGE , WEIGHT , HEIGHT, GENDER) 
    VALUES 
    ('{name}', '{last_name}', '{bike}', {age}, {weight}, {height}, '{gender}' )"""
    cursor.execute(query)
    connection.commit()
    # connection.close()  
def saveParametrosData(url_video, knee_min, knee_max, hip_min, hip_max, shoulder_avg):
    global connection, cursor
    last_id = int(get_last_id())
    query = f"""INSERT INTO PARAMETROS 
        (ID_PACIENTE , URL_VIDEO , KNEE_MIN, KNEE_MAX, HIP_MIN, HIP_MAX, SHOULDER_AVG) 
        VALUES 
        ({last_id}, 'videos_out/{url_video}', {knee_min}, {knee_max}, {hip_min}, {hip_max}, {shoulder_avg})"""
    cursor.execute(query)
    connection.commit()
  
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
#     FOREIGN KEY(ID_PACIENTE) REFERENCES PACIENTES(ID) );"""
# cursor.execute(table)


# cursor.execute("""INSERT INTO PACIENTES 
#     (NAME , LAST_NAME,BIKE ,AGE , WEIGHT , HEIGHT, GENDER) 
#     VALUES 
#     ('Juan', 'Samayoa', 'Rockhopper', 21, 65, 170, 'masculino' )""")

# cursor.execute("""INSERT INTO PARAMETROS 
#     (ID_PACIENTE , URL_VIDEO , KNEE_MIN, KNEE_MAX, HIP_MIN, HIP_MAX, SHOULDER_AVG) 
#     VALUES 
#     (2, 'videos_out/video_prueba47', 27.5, 180.3, 22.2, 170.2, 33.2 )""")

# saveData('Juan Jose','Ancheyta', 'Ranger', 140.22, 23.1, 140.22, 23.1, 45.3, 'video/video_prueba13.avi')
# print("Data Inserted in the table: ")
# data = cursor.execute('''DROP TABLE parametros;''')
# data = cursor.execute('''SELECT seq FROM sqlite_sequence WHERE name = "PACIENTES";''')
# print(data.fetchall()[0][0])
# for row in data:
#     print(row)
connection.commit()

# connection.close()  
  

# Commit your changes in the database    


  