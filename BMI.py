
def BMI_calculate(height, weight):
    height = height/100
    BMI = weight/ (height*height)
    return BMI

def main():

    Height = float(input(" Enter your Height in centimeters: "))
    Weight = float(input(" Enter your body Weight in kg: "))
    BMI = BMI_calculate(Height, Weight)
    print (" your Body Mass Index (BMI) is : ", BMI)
    
    if (BMI > 0):
        if (BMI <= 16):
            print(" you are severely underweight.")
        elif (BMI <= 18.5):
            print(" you are underweight.")
        elif (BMI <= 25 ):
            print(" you are healthy.")
        elif (BMI <= 30):
            print(" you are overweight.")
        else: 
            print(" you are severly overweight.")
    else:
        print (" Enter valid details.")
    
if __name__ == '__main__':
    main()

