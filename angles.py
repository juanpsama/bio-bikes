import matplotlib.pyplot as plt
import numpy as np
import math


def getAnglesBetweenPoints(central_point , first_point, second_point):
    # pendiente = (Y2-Y1)/(X2-X1) 
    # alpha = atan(m1-m2)/(1+m1*m2)
    central_point = (round(central_point[0], 3), round(central_point[1], 3))
    first_point = (round(first_point[0], 3), round(first_point[1], 3))
    second_point = (round(second_point[0], 3), round(second_point[1], 3))
    #si el punto 1 y el central estan alineados en el eje y ocurre un error de division entre 0
    if (first_point[0] == second_point[0]) and (first_point[0] == central_point[0]):
        angle = 180
    elif (first_point[1] == second_point[1]) and (first_point[1] == central_point[1]):
        angle = 0
    elif (second_point[0] - central_point[0]) == 0:
        tan_alpha = (central_point[1] - first_point[1])/(central_point[0] - first_point[0])   
        angle = 90 - math.degrees(math.atan(tan_alpha))
    elif(first_point[0] - central_point[0]) == 0:
        tan_alpha = (central_point[1] - second_point[1]) / (central_point[0] - second_point[0])   
        angle = 90 + math.degrees(math.atan(tan_alpha))
    else:
        pendiente_1 = (first_point[1] - central_point[1])/(first_point[0] - central_point[0])
        pendiente_2 = (second_point[1] - central_point[1])/(second_point[0] - central_point[0])  
        if (pendiente_1 * pendiente_2) != -1:
            # print(pendiente_1, pendiente_2)
            tan_alpha = (pendiente_1 - pendiente_2) / (1 + pendiente_1 * pendiente_2)
            angle = math.degrees(math.atan(tan_alpha))
            if angle < 0:
                angle = abs(angle)
            else:
                angle = 180 - angle
        else:
            angle = 90
    # fig, ax = plt.subplots()  # Create a figure containing a single axes.
    # ax.plot([first_point[0], central_point[0], second_point[0]], [-first_point[1] + 500, -central_point[1] + 500, -second_point[1] + 500]);  # Plot some data on the axes.
    # ax.axis('equal')
    # plt.show()
    # if central_point[0] > first_point[0] and angle < 45:
    #      angle -= 180
    # return abs(angle)
    return angle
    

x = [319, 366, 347]
y = [-246, -341, -456]

# ax.plot(x, y);  # Plot some data on the axes.
# ax.axis('equal')

# sagital_14:
# Rodilla: [424.14544546604156, 312.80561780929565]
# Tobillo: [372.6763038635254, 407.8215112686157]
# Cadera: [270.82268607616425, 270.82268607616425]
# Angulo: -38.05713711134102
# sagital_12: el angulo se toma al revez checar eso 
# Rodilla: [366.4123131632805, 341.4016273021698]
# Tobillo: [347.3477544784546, 456.6890435218811]
# Cadera: [319.75472831726074, 246.37444746494293]
# Angulo: 35.540438105555296
     
#angulo = getAnglesBetweenPoints((x[1],y[1]), (x[0],y[0]), (x[2],y[2]) )
#print(f'Angulo: {angulo}')
# print(f'pendiente 1:{pendientes[0]}') 
# print(f'pendiente 2:{pendientes[1]}') 

# plt.show()


