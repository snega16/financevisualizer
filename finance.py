'''
Budget App
Visualize your money
'''

import pandas as pd
import matplotlib.pyplot as plt

print("---------------------")
print("Welcome to Budget App")
print("---------------------")

file = input("Paste the file location: ")
s = pd.read_csv(file)
transaction = pd.DataFrame(s)
print(transaction)
print("File successfully added")
income = ['Income']
expenditure = ['Expenditure']
investment = ['Investment']
loss = ['Loss']
date = ['Date']



print("Following Analysis & Sorting you can do")
print("---------------------------------------")
print("1. Sort Income by date")
print("2. Sort Expenditure by date")
print("3. Sort Investment by date")
print("4. Sort Loss by date")
print("---------------------------------------")

c = input("Enter your choice: ")

if c == '1':
    df = pd.DataFrame(s, columns=['Income','Date'])
    print(df)
    s = input("Do you want to visualize it? ")
    if s =='y':
        x = df["Date"]
        y = df["Income"]
        plt.bar(x,y)
        plt.show()
elif c == '2':
    df = pd.DataFrame(s, columns=['Expenditure','Date'])
    print(df)
    s = input("Do you want to visualize it? ")
    if s == 'y':
        x = df["Date"]
        y = df["Expenditure"]
        plt.bar(x, y)
        plt.show()
elif c == '3':
    df = pd.DataFrame(s, columns=['Investment','Date'])
    print(df)
    s = input("Do you want to visualize it? ")
    if s == 'y':
        x = df["Date"]
        y = df["Investment"]
        plt.bar(x, y)
        plt.show()
elif c == '4':
    df = pd.DataFrame(s, columns=['Loss','Date'])
    print(df)
    s = input("Do you want to visualize it? ")
    if s == 'y':
        x = df["Date"]
        y = df["Loss"]
        plt.bar(x, y)
        plt.show()
else:
    print("Please enter a valid choice")

