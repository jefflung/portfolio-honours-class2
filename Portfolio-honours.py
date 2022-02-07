#honours classification

firstName=str(input("Please enter your first name:"))
lastName=str(input("Please enter your last name:"))
wam=int(input("Please enter your Weighted Average Mark:"))

def get_class(wam):
    if(wam>=70):
        classification="First Class"
    elif(wam>=60):
        classification="Upper Second"
    elif(wam>=50):
        classification="Lower Second"
    elif(wam>=40):
        classification="Third Class"
    elif(wam>=35):
        classification="Pass Degree"
    else:
        classification="Fail"
    return classification

def get_message(wam):
    if(wam>=70):
        message="Excellent, well done!"
    elif(wam>=60):
        message="Very good, well done!"
    elif(wam>=50):
        message="Good, well done!"
    elif(wam>=40):
        message="Could have done better!"
    elif(wam>=35):
        message="Work harder next time!"
    else:
        message="Oh dear, try again!"
    return message

def get_result(classification, message):
    if(wam>=0 and wam<=100):
        print(firstName+" "+lastName)
        print("Your Honours Classification is",classification)
        print(message)
    else:
        print("The input is invalid.")

classification=get_class(wam)
message=get_message(wam)
get_result(classification, message)