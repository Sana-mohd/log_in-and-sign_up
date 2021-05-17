user_ans=input("enter either log in or sign up: ")
if user_ans=="sign up":
    user_name=input("enter your user name: ")
    i=1
    list=["0","1","2","3","4","5","6","7","8","9"]
    while i<2:
        password=input("enter your password: ")
        a=0
        b=0
        c=0
        for x in password:
            if x>"A" and x<"Z" or x>"a" and x<"z" or x=="@" or x=="#" or x in list:
                if x>"A" and x<"Z" or x>"a" and x<"z":
                    c=c+1
                elif x in list:
                    a=a+1
                elif  x=="@" or x=="#":
                    b=b+1
        if a==0:
            print("req atleast one number")
        if b==0:
            print("req atleast one special character\nplease sign up again")
        if c==0:
            print("req alphabets ")
        i=i+1
        if a>=1 and b>=1 and c>=1:
            print("alright it is acceptable")
            confirm_password=input("enter your password for confirmation: ")
            if password==confirm_password:
                print("congratulations\nyou are signed up successfully")
                import json
                dict={}
                json_file={}
                dict[user_name]=password
                list=[dict]
                json_file["user"]=list
                f=open("signup.json","w")
                json.dump(json_file,f,indent=1)
                f.close()
            else:
                print("both passwords are not same\ncheck weather you have entered both passwords correclt or not")
        else:
            print("not acceptable")
    


            
            