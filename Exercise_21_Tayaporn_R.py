from tkinter import *
import math

def calculate_bmi(): # Create a function to calculate BMI
    try:
        weight = float(textBoxWeight.get()) # Get weight value from the entry box and convert to float
        height = float(textBoxHeight.get()) / 100 # Get height value from the entry box, convert to float, and convert to meters
        bmi = weight / (height ** 2) # Calculate BMI
        labelResult.configure(text=f"BMI: {bmi:.2f}") # Display the calculated BMI with 2 decimal places
        show_bmi_category(bmi) # Call the function to show BMI category
    except ValueError:
        labelResult.configure(text="Invalid input") # Show this message if the input is invalid

def show_bmi_category(bmi): # Create a function to display BMI category in a new window
    category_window = Toplevel(MainWindow) # Create a new window (Toplevel) within the main window
    category_window.title("BMI Category")

    labelCategory = Label(category_window, text="")
    labelCategory.pack()

    if bmi < 18.5:
        labelCategory.configure(text="คุณผอมเกินไป ไปหาหมอบ้างนะ")
    elif 18.5 <= bmi <= 22.9:
        labelCategory.configure(text="น้ำหนักปกติ ยินดีด้วย")
    elif 23 <= bmi <= 24.9:
        labelCategory.configure(text="น้ำหนักเกิน กินเพลินไปหน่อยนะ")
    elif 25 <= bmi <= 29.9:
        labelCategory.configure(text="อ้วนแบบนี้ ไม่มีผัวแน่")
    else:
        labelCategory.configure(text="อ้วนมาก เตรียมตัวโดนตัดขาได้เลย")

MainWindow = Tk()
MainWindow.title("BMI Calculator")

labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)

labelWeight = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)

calculateButton = Button(MainWindow, text="คำนวน", command=calculate_bmi)
calculateButton.grid(row=2, column=0, columnspan=2)

labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=3, column=0, columnspan=2)

MainWindow.mainloop()

