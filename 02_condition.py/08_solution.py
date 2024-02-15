password = "Secure3P@ass"

if len(password) < 6:
    streangth = "Weak"
elif len(password)<= 10:
    streangth = "Medium"
else:
    streangth = "Strong"
print("Password Streanght is :", streangth)