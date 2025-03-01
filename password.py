import time
user_info={"Arjun":3.25,"Seyyan":3.56,"Rayan":4.08,"Athul":4.98}
print("User Authentification:")
user_name=input("Enter the User Name:")

if user_name in  user_info:
    count=0
    start_time = time.time()
    password = input("Enter the password:")
    end_time = time.time()
    time_taken = end_time - start_time
    while count<=3:
           if time_taken < user_info[user_name] or time_taken > user_info[user_name]:
               count+=1
               print("Authentification failed due to mismatched response time")
               if count==3:
                   print("Too many failed attempts Try after some time")
                   break

               choice=input("Do you want to try again yes/no")
               if choice=="yes":
                   user_name = input("Enter the name:")
                   if user_name in user_info:
                           start_time = time.time()
                           password = input("Enter the password:")
                           end_time = time.time()
                           time_taken = end_time - start_time
                   else:
                       print("You dont have an account SignUp!")
                       break
               if choice!="yes":
                   print("If you are a valid user and cannot login please check your registerd email for instructions")
                   break

           else:
              print("Logged in Successfully")



else:
     print("You dont have an account Sign Up!")


