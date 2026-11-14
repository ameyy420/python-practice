num = int((input("Enter marks:")))

if num>40:
    print("Pass the exam")
elif num>40 and num<50:
    print("Got C Grade");
elif num>50 and num<60:
    print("Got B Grade")
    
elif num>60 and num<70:
    print("Got A- Grade")
    
elif num>70 and num<80:
    print("Got A Grade")
 elif num>80 or num<=100:
    print("Got A+ Grade")