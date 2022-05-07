import math
import os
import random
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
msg='Your OTP Verification for app is '+OTP+' Note..  Please enter otp within 2 minutes and 3 attempts, otherwise it becomes invalid'
file2=open("otp.txt","w")
file2.write(OTP)
file2.close()
os.system('python second.py')
