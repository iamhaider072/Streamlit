import streamlit as st



st.title("Welcome to BMI Calculator")


#Weight
weight=st.number_input("Enter your weight (in KG's)?")

#Hight fromat
#Hight
height=st.number_input('Enter your height?')
status=st.radio('Select your heigth format:',('m','cm','feet'))
bmi=0

Button=st.button("Caculate BMI")



if Button and height!=0:

       if(status=='m'):
   
         bmi=weight/height*2
         st.write(f"BMI is {bmi}")


       elif(status=='cm'):
        newheigth=height/100
        bmi=weight/height
        st.write(f"BMI is {bmi}")

       elif(status=='feet'):
        newheight=height*100
        bmi=weight/height
        st.write(f"BMI is {bmi}")

elif(Button==False):
         print("Button is not pressed")
elif(height==0):
   print("Error:Division by Zero")








#Interpreting Values
    

if (bmi):   
 if(bmi<18.5):
   st.write("Underweight")

 elif(bmi>18.5 and bmi<24.9):
   st.write("Normal Weight")
 elif(bmi>25 and bmi>29.9):
   st.write("Overweight")
 elif(bmi>30):
   st.warning("Obesity")










