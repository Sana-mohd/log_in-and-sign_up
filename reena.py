import json
data={}
dictionary={}
new_dictionary={}
def strong_password(user_password):
    number="0123456789"
    capital_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_alphabet="abcdefghijklmnopqrstuvwxyz"
    special_chrs="@#&"
    sum=0
    a=0;x=0;y=0;z=0
    if len(user_password)<5 or len(user_password)>17:
        print("password length between 6 to 16")
        user_password=input("\nplease enter password")
    for i in range(len(user_password)):
        if user_password[i] in number:
            x=1
        elif user_password[i] in capital_alphabet:
            y=1
        elif user_password[i] in small_alphabet:
            a=1  
        elif user_password[i] in special_chrs:
            z=1
    sum=a+x+y+z
    if sum!=4:
        print("password must contain number,capital_alphabet,small_alphabet,special_character,")

        user_password=input("enter the correct password:\n")
    else:
        print("\ncorrect password!!")
#user_password=input("enter the password")#strong_password(user_password)
def user():
    global user_name
    global data
    user_name=input("enter the user_name\n")


def signup():

        user()#user_name=input("enter the user_name:\n")
        with open("userdeatils.json","r") as f:
            data=json.load(f)
            for i in data["user"]:
                if user_name in i["name"]:
                    print("user already exists")
                    user()
                    break
                else:
                    pass#user_name=input("enter the user_name:\n")
        
        password1=input("enter the password:-")
        strong_password(password1)
        password2=input("enter your confirm password:-")
        if password1==password2:
            print("your password is confirm")
            print("signed up successfully!")
           
            description=input("enter the description=")
            dob=input("enter the dob=")
            hobbies=input("enter the hobbies=")
            gender=input("enter the gender=")
            dictionary["name"]=user_name
            dictionary["password"]=password1
            new_dictionary["description"]=description
            new_dictionary["dob"]=dob
            new_dictionary["hobbies"]=hobbies
            new_dictionary["gender"]=gender
            dictionary["profile"]=new_dictionary
            data["user"].append(dictionary)

            f=open("userdeatils.json","w")
            json.dump(data,f,indent=3)
            f.close()
        else:
            print("both password is not same")

def log_in():#user()# password=input("enter the correct password:_")
    with open("userdeatils.json") as f:
        data=json.load(f)
        user()
        password1=input("enter the password:---")
        strong_password(password1)
        with open("userdeatils.json","r") as fi:
            data2=json.load(fi)
            fi.close()
            i=0
            while i<len(data["user"]):
                user_data=(data2["user"][i])
                if user_data["name"] ==user_name and user_data["password"]==password1:
                    print("USER_PROFILE")
                    print("Username:--",user_name)
                    print("Gender:--",user_data["profile"]["gender"])
                    print("Bio:--",user_data["profile"]["description"])
                    print("Hobby:--",user_data["profile"]["hobbies"])
                    print("DoB:--",user_data["profile"]["dob"])
                    break
                i=i+1
            else:
                print("username and Invalid password")
                log_in()
                    # break
                

    
            
def log_in_sign_up():
    print("create your account")
    option=input("enter the option\n log_in or sign_up\n")
    if option=="sign_up":
        signup()
        print("congrates",user_name,"you are signed successfully!!!")
    elif option=="log_in":
        log_in()
        if True:
            print(user_name,"you are logged in successfully!!!!")
log_in_sign_up()