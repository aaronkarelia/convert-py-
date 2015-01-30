# convert.py
# A program to convert Celsius temps to Fahrenheit

def main():
    print("The program will convert celsius to fahrenheit.")    
    celsius = eval(input("What is the Celsius temperature? "))
    for celsius in [0, 10, 20, 30, 40, 50, 60, 70 ,80, 90, 100]:
        fahrenheit = 9/5 * celsius + 32
        print('The temperature is', celsius, 'celsius and', fahrenheit, 'degrees Fahrenheit.')

main()

