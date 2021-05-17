import json
def json_file():
    profile_list=["description","dob","hobbies","gender"]
    des_user=input("enter your description:  ")
    dob_user=input("enter your date of birth: ")
    hobby_user=input("enter your hobbies: ")
    gender_user=input("enter your gender: ")
    values_profile=[des_user,dob_user,hobby_user,gender_user]
    ind=0
    profile_dict={}
    while ind<len(profile_list):
        profile_dict[profile_list[ind]]=values_profile[ind]
        ind=ind+1
    print(profile_dict)
    dict={}
    json_file={}
    dict[user_name]=password
    dict["profile"]=profile_dict
    list=[dict]
    json_file["user"]=list
    f=open("signup.json","w")
    json.dump(json_file,f,indent=1)
    f.close()
def password_fun():
    confirm_password=input("enter your password for confirmation: ")
    if password==confirm_password:
        print("congratulations\nyou are signed up successfully")
        json_file()
    else:
        print("both passwords are not same\ncheck weather you have entered both passwords correclt or not")
        password_fun()
def sign_up_fun():
    i=1
    list=["0","1","2","3","4","5","6","7","8","9"]
    global password
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
    if a==0 or b==0 or c==0:
        print("once again enter your password\nnot in the correct form")
        sign_up_fun()
    if a>=1 and b>=1 and c>=1:
        print("alright it is acceptable")
        password_fun()
        
def user_name_fun():
    global user_name
    user_name=input("enter your user name: ")
    open_user=open("signup.json","r")
    load_user=json.load(open_user)
    c1=0
    for us in load_user["user"]:
        for er in us.keys():
            if user_name==er:
                print("you can't choose this username")
                open_user.close()
                user_name_fun()
                break
            else:
                print("you can choose this user name")
                open_user.close()
                c1=c1+1
                sign_up_fun()
                break
        if c1==1:
            break
def password_log_in():
    user_password=input("enter your password: ")
    file=open("signup.json","r")
    log_in=json.load(file)
    c3=0
    for pas in log_in["user"]:
        for word in pas.values():
            if user_password==word:
                c3=c3+1
                print("password is correct\nlogged in successfully")
                file.close()
                break
            else:
                print("invalid password")
                file.close()
                password_log_in()
                break
        if c3==1:
            break

def log_in_fun():
    log_in_name=input("enter your user name: ")
    log_open_file=open("signup.json","r")
    load_json=json.load(log_open_file)
    c2=0
    for log in load_json["user"]:
        for g in log.keys():
            if log_in_name==g:
                c2=c2+1
                print("your user name is correct")
                log_open_file.close()
                password_log_in()
                break

            else:
                print("invalid user name")
                log_open_file.close()
                log_in_fun()
                break
        if c2==1:
            break

def main_fun():
    user_ans=input("enter either log in or sign up: ")
    if user_ans=="sign up":
        user_name_fun()
    elif user_ans=="log in":
        log_in_fun()
main_fun()