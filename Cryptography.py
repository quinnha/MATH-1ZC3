#!/usr/bin/env python
# coding: utf-8

# In[148]:

#Make sure to have numpy/pandas installed in cmd, pip install numpy

#Encode
import numpy as np

cipher = {"A" : 1, "B" : 2, "C" : 3, "D": 4, "E": 5, "F": 6,
         "G" : 7, "H" : 8, "I" : 9, "J": 10, "K": 11, "L": 12,
         "M" : 13, "N" : 14, "O" : 15, "P": 16, "Q": 17, "R": 18,
         "S" : 19, "T" : 20, "U" : 21, "V": 22, "W": 23, "X": 24,
         "Y": 25, "Z" : 0}

inv_cipher = {v: k for k, v in cipher.items()}

inverses = {1 : 1, 3 : 9, 5 : 21, 7 : 15, 9 : 3, 11 : 19, 15 : 7, 17 : 23, 19 : 11, 21 : 5, 23 : 17, 25: 25}

def convertLetter(ciphertext):
    returnval = []
    for i in ciphertext:
        returnval.append(inv_cipher[i])
    return returnval

def convertMod(plaintext):
    returnval = []
    for i in plaintext:
        if i == 26:
            returnval.append(0)
        elif i > 26:
            returnval.append(i % 26)
        elif i < 0:
            returnval.append(26 - abs(i) % 26)
        else:
            returnval.append(i)
    return convertLetter(returnval)

def convertModBase (number, base):
    if number == base:
        return 0
    elif number > base:
        return number % base
    elif number < 0:
        return (base - abs(number) % base)
    else:
        return number

def encode(A, message):
    encoded_text = ''

    counter = 0
    for i in range(0, len(message)-1, 2):
        plaintext = np.matmul(A, [cipher[message[i]], cipher[message[i+1]]])
        encoded_matrix = convertMod(plaintext)
        encoded_text = encoded_text + "".join(str(x) for x in encoded_matrix)
        counter+=2

    if len(message) - counter == 1:
        plaintext = np.matmul(A, [cipher[message[-1]], cipher[message[-1]]])
        encoded_matrix = convertMod(plaintext)
        encoded_text = encoded_text + "".join(str(x) for x in encoded_matrix)

    return encoded_text

def decode(A, message):
    decoded_text = ''

    A_inverse = (inverses[A[0][0] * A[1][1] - A[0][1] * A[1][0]]) * np.array([[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]])


    for i in range(0, len(message)-1, 2):
        plaintext = np.matmul(A_inverse, [cipher[message[i]], cipher[message[i+1]]])
        decoded_matrix = convertMod(plaintext)
        decoded_text = decoded_text + "".join(str(x) for x in decoded_matrix)

    return decoded_text


# In[151]:


#Change these values
A = np.array([[4,3],[1,2]]) #Change this to enciphering matrix, first [] is first row, second [] is second row

message = "DARK NIGHT".replace(" ", "").upper() #Change string to message wanted to encode

number = 11 #Change for number for convertModBase and inverse

base = 4 #Change for base for convertModBase

#Examples of Using code

#Encode
encode(A,message)

#Decode
decode(A, message)

#Convert number to mod with base
convertModBase(number, base)

#Get inverses for mod 26
inverses[number]

