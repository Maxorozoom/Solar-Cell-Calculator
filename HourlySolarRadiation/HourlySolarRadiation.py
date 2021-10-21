import math #imports math functions such as pi cos or sin
import tkinter #imports functions for the GUI that will hopefully be used in th next prototype
import matplotlib.pyplot as plt #to create plots for graphs and shorted to be used in plt rather than matplot the entire program


ianswer= int(input("Please put what day that you would like to analyze\n1. January 1\n2. June 21\n3. December 21\n4. December 31 \n")) #output what the user views
pi = float(math.pi) #pi function but used to not have to use the math.pi everytime pi is used


def day_angle_function(ianswer): #function to find the day angle 

    days_list = [0, 1 , 171 , 335, 365] # the days that are available to be found those days are important as in 1st day of the year start of the summer solstice stard of winter solstice and the lat day of the year
    global day_number #makes the variable global througout the program 
    global day_angle #makes the variable global througout the program 
    day_number = int(days_list[ianswer]) #ensures that the number inputted is an integer

    
    day_angle = 2*pi*(day_number-1)/365 #day angle equation
    
    math.radians(day_angle) #converts the answer to degrees

    print(day_angle, " day angle ") #prints the day angle 

def declination_angle_function (day_angle):# function for the delination angle uses the day angle
    global declination_angle #makes the variable global througout the program 
    declination_angle = .006918-.399912*math.cos(day_angle)+.070257*math.sin(day_angle)-.006758*2*math.cos(day_angle)+.000907*2*math.sin(day_angle)-.002697*3*math.cos(day_angle)+.00148 *3*math.sin(day_angle)*(180/pi)
    #equation above used to find the declination angle depending on the day angle.
    
    print(declination_angle, " Declination Angle")

def B_function (day_number):#function to solve for B function

    global B #makes the variable global througout the program 

    B = 360*(day_number-81)/365 # equation to fin the B for the equation of time depends on the day number

    B= round(B) #rounds the number

    print (B," B number")

def Equation_time_function(B): #function to find the equation of time

    global ET #makes the variable global througout the program 

    B=math.radians(B) #converts the B angle to degrees
   

    ET = 9.87*math.sin(2*B)-7.57*math.cos(B)-1.5*math.cos(B)# equation for time

   

    print(ET," Equation of Time")

def Local_solar_time_function (ET):#function tosolve for local solar time

    global hour_list #makes the variable global througout the program 
    hour_list = [9,12,15,18,21] #list of the hours that will be used for the imulation in millitary time
    longitude = -99.50 #longitude of Laredo
    Ls = -90 #local standay meridian of Laredo
    global ST #makes the variable global througout the program 
    ST = [] #List of the Local solar time
    for hour in hour_list: #for loop to iterate multiple times for each hour in the hour list
        ST_values = hour +(ET/60)+ 4/60*(Ls - longitude) #equation for the local solar time
        ST_values = round(ST_values)# rounds the values
        ST.append(ST_values)#updates the empty ST list

    print(ST," ST Values")

def hour_angle_function (ST):#function for hour angle 

    global w #makes the variable global througout the program 
    w=[] #List for the hour angles
    for i in ST: #for loop to iterate over the amount of values in the ST list

        if i == 13:#if a value of ST will = 13 it will cahnge the value to 0 instead reason is since it rounds upwards the value of 12 will be 13 and at noon should be 0

            i = 0
    
       
        hour_angle = (12-i)*15#eqauation for the hour angle


        w.append(hour_angle)#updates the hour angle lists
    print (w," Hour Angles")

def eccentricity (day_angle):#fucntion for eccentricity

    math.radians(day_angle)#converts the day angle to degrees
    global E#makes the variable global througout the program 
    E = 1 + .0033*math.cos(2*pi*day_angle/365) #equation for the eccentricity

    E=round(E)#rounds the eccentricity values

    print (E," Eccentricity Values")

def hourly_radiation(E,declination_angle,w,):#function for hourly radiation
    latitude = 27.51# latitude of Laredo
    Isc = 1367#solar constant
    global H0#makes the hourly radiation global
    H0=[]#empty list for the global radiation at different times
    for hour in w: #for loop to iterate over the # of hours in the hourangle list
        H0_values = (12*3.6*Isc*E)/pi#first part of the equation for the radiation

        H0_values = abs(H0_values *(math.sin(latitude)*math.cos(declination_angle)*(math.sin(hour+3)-math.sin(hour))+((pi*(hour+3-hour))/180)*(math.sin(latitude)*math.sin(declination_angle))))
        #second part of the equation
        H0_values=round(H0_values)#rounds values

        H0.append(H0_values)#updates values
    print (H0," Radiation Values")

def final_H_values (H0):#function for final H values

    global final_H0_values#makes the final radiation values global
    final_H0_values = []#empty list for the final radiation values to go in
    for i in H0:#another for loop to divide the values by 1000 to ensure thay are in KwH
   

        FH = i /1000

        final_H0_values.append(FH)

    print(final_H0_values,"Final Radiation values in W/h")

def Final_output(final_H0_values):#fucntion for the final output
    Sarea = 1.63 #Surface Area in m^2
    Syield = .245 #solar panel yield %
    Pratio = .75  #Performance ratio
    global final_output_list #final output list global
    final_output_list = []
    for i in final_H0_values:#final output of the solar panel using the equation E = A x r x H x PR to estimate the electricity generated in Kwh 

        final_output = i*Sarea*Syield*Pratio#Equarion for the output

        final_output=round(final_output)#rounds values

        final_output_list.append(final_output)#updates list

      

    print (final_output_list," Final output in KWH")

def graph (final_output_list,hour_list):#function especially for the graph

    plt.plot(hour_list,final_output_list)# puts their axis in x,y for the lists

    plt.xlabel("Hour")#title for x axis
    plt.ylabel ("Output in Kw/h")#title for yaxis
     
    plt.title("Solar Output Per Hour")#title for graph

    plt.show()#shows the graph



day_angle_function(ianswer)#function call

declination_angle_function (day_angle)#function call

B_function (day_number)#function call

Equation_time_function(B)#function call

Local_solar_time_function (ET)#function call

hour_angle_function (ST) 

eccentricity (day_angle)#function call

hourly_radiation(E,declination_angle,w,)#function call

final_H_values (H0)#function call

Final_output(final_H0_values)#function call

graph (final_output_list,hour_list)#function call

