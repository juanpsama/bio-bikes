import sqlite3

connection = sqlite3.connect("database/BioBikes.db")
cursor = connection.cursor()

def savePersonalData(name, last_name, bike, age, weight, height, gender):
    global connection, cursor
    query = f"""INSERT INTO PACIENTES 
    (NAME , LAST_NAME,BIKE ,AGE , WEIGHT , HEIGHT, GENDER) 
    VALUES 
    ('{name}', '{last_name}', '{bike}', {age}, {weight}, {height}, '{gender}' )"""
    cursor.execute(query)
    connection.commit()
    # connection.close()  
  
# def savePersonalData(name, last_name, bike, knee_ext, knee_flex, hip_ext, hip_flex, shoulder_mean, video_url):
#     global connection, cursor
#     query = f"""INSERT INTO PACIENTES 
#     (NAME, LAST_NAME, BIKE, AGE, WEIGHT,GENDER ,KNEE_EXT , KNEE_FLEX, HIP_EXT, HIP_FLEX, SHOULDER_MEAN, VIDEO_URL) 
#     VALUES 
#     ('{name}', '{last_name}', '{bike}', {knee_ext}, {knee_flex}, {hip_ext}, {hip_flex}, {shoulder_mean}, '{video_url}' )"""
#     cursor.execute(query)
#     connection.commit()
#     # connection.close()  
  

# table = """CREATE TABLE PARAMETROS (ID_PACIENTE VARCHAR(255), URL_VIDEO VARCHAR(255),
# KNEE_MIN FLOAT(3), KNEE_MAX FLOAT(3), HIP_MIN FLOAT(3), HIP_MAX FLOAT(3), SHOULDER_AVG FLOAT(3));"""
# cursor.execute(table)


# Creating table
# table = """CREATE TABLE PACIENTES (ID INTEGER PRIMARY KEY AUTOINCREMENT ,NAME VARCHAR(255), LAST_NAME VARCHAR(255),
# BIKE VARCHAR(255),AGE INTEGER(3), WEIGHT INTEGER(3), HEIGHT INTEGER(3), GENDER VARCHAR(20) ,KNEE_EXT FLOAT(6), KNEE_FLEX FLOAT(6), HIP_EXT FLOAT(6), HIP_FLEX FLOAT(6), SHOULDER_MEAN FLOAT(6), VIDEO_URL VARCHAR(255) );"""
# cursor.execute(table)


# cursor.execute('''INSERT INTO PACIENTES VALUES (1 , 'Juan Pablo', 'Garcia Samayoa', 'Rockhopper', 150.2, 20.5, 150.2, 20.5, 45, 'videos/video_prueba17.avi' )''')

# saveData('Juan Jose','Ancheyta', 'Ranger', 140.22, 23.1, 140.22, 23.1, 45.3, 'video/video_prueba13.avi')
# print("Data Inserted in the table: ")
data = cursor.execute('''SELECT * FROM PACIENTES''')
for row in data:
    print(row)
connection.commit()

# connection.close()  
  

# Commit your changes in the database    


  