#welcome message
print("welcome this a calculator that can enter your all operation in one line :-)")
#input for calculation 
def cal():
    calculation=input("Enter your calculation:" )
    l=len(calculation)
    #find operator
    f_oplus=calculation.find("+")
    f_ominus=calculation.find("-")
    f_odiv=calculation.find("/")
    f_omulti=calculation.find("*")
    f_opower=calculation.find("^")
    f_opower2=calculation.find("**")
    f_omodule=calculation.find("%")
    #calculation of addition
    if f_oplus>0:
        firstoperand=calculation[0:int(f_oplus)]
        secondoperand=calculation[int(f_oplus)+1:int(l)]
        print(float(firstoperand)+float(secondoperand))
    #calculation of substraction
    elif f_ominus>0:
        firstoperand=calculation[0:int(f_ominus)]
        secondoperand=calculation[int(f_ominus)+1:int(l)]
        print(float(firstoperand)-float(secondoperand))
    #calculation of divisiontion
    elif f_odiv>0:
        firstoperand=calculation[0:int(f_odiv)]
        secondoperand=calculation[int(f_odiv)+1:int(l)]
        print(float(firstoperand)/float(secondoperand))
        #calculation of power(if user use ^)
    elif f_opower>0:
        firstoperand=calculation[0:int(f_opower)]
        secondoperand=calculation[int(f_opower)+1:int(l)]
        print(float(firstoperand)**float(secondoperand))
        #calculation of multiple
    elif not(f_omulti and f_opower2)>0:
        firstoperand=calculation[0:int(f_omulti)]
        secondoperand=calculation[int(f_omulti)+1:int(l)]
        print(float(firstoperand)*float(secondoperand))
    #calculation of power(if user use **)
    elif f_opower2>0:
        firstoperand=calculation[0:int(f_opower2)]
        secondoperand=calculation[int(f_opower2)+2:int(l)]
        print(float(firstoperand)**float(secondoperand))
    #calculation of module
    elif f_omodule>0:
        firstoperand=calculation[0:int(f_omodule)]
        secondoperand=calculation[int(f_omodule)+1:int(l)]
        print(float(firstoperand)%float(secondoperand))
    continu=input("If you want to do another calculation type\"y\" it's not type \"n\" ")
    if continu == "y":
        cal()
cal()
