def emailVerfication_using_string_functions():
    print("====>>Welcome to Email Verification<<====")

    k,j,d =0,0,0 
    email = input("====>>Enter your email : \n====>>")

    if len(email) >=6: # length on email should atleast 6
        if email[0].isalpha(): # starts with letter
            
            if ('@' in email) and (email.count('@') ==1): # @ symbol should need to be in email and which should be @ =1
                if  (email.count("_")<=1) and (email.count('.')==1): # checks _ and . should be ==1 

                    if (email[-4] =='.')  ^ (email[-3]=='.') :#f@g.com or .in
                        for i in email:
                            if i==i.isspace(): # if a space is there 
                                k =1
                            elif i.isalpha(): # if letter
                                if i ==i.isupper(): #if letter is upper 
                                    j = 1
                            elif i.isdigit(): # if there is digit in email
                                continue 
                            elif i =="_" or i =="." or i =="@": # allow _,.,@ symbols
                                if i.count(".") ==1 and i.count("_")==1:
                                    continue
                            else:
                                d =1 
                        if  k==1 or d ==1 or j ==1:
                            print("Email is Invalid!")
                        else: 
                            print("Your Email is Valid ")

                    else:
                        print("Email is Invalid! \nThere must be dot(.) after the domail name! ")
                else:
                    print("Email is Invalid !\nEmail must contain one dot(.) and one (_)")
            else:
                print("Email is Invalid! \nEmail must contain @ symbol and it's length must be 1") 
        else:
            print("Email is Invalid! \nEmail must starts with small letter ")
    else:
        print("Email is Invalid! \nLength of email should be atleast 6 ")

# emailVerfication_using_string_functions()

def regex_email_verification():
    import re 
    email_input = input("=====>>Enter Your Email :\n=====>>")

    email_condition = "[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2.3}"
    if re.search(email_condition,email_input):
        print("Email is Valid!")
    else:
        print("Email Is Invalid")


regex_email_verification()