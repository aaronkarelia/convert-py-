# convert.py
# A program to convert Celsius temps to Fahrenheit

def main():
    print("The program will convert celsius to fahrenheit.")    
    celsius = eval(input("What is the Celsius temperature? "))
    for celsius in range(5):
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
