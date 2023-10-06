# ----------------------------------------------
def string(rislable,revision):
    print(f"{type(revision)}--->>> revision = {revision}")
    print(f"{type(rislable)}--->>> rislable = {rislable}")            
    return rislable, revision
    
def list(rislable,revision):
    build_list = [rislable]
    build_list.append(revision)
    print(type(build_list),build_list) 
    return build_list[0], build_list[1]  

def dictionary(rislable,revision):
    build_dict = {}
    build_dict.update({"rislable":rislable})
    build_dict.update({"revision":revision})
    print(type(build_dict),build_dict)
    return build_dict['rislable'], build_dict['revision']


def main():
    build_name = "FHGW23R2_010.1.9_2303022258_1430293_base"
    build_name_breaking = build_name.split("_")
    print(build_name_breaking)
    rislable = "_".join(build_name_breaking[0:2])
    rivision = build_name_breaking[3]

    x = input(f"in which format do you want to get string/list/dictionary ")
    if x== "s":
        ris, rev = string(rislable,rivision)      
    elif x == "l":
        ris, rev = list(rislable,rivision)
    else:
        ris, rev = dictionary(rislable,rivision)
    
    print(f" rislabel --> {ris}\n revision --> {rev}")


if __name__ == "__main__":
    main()

'''
use meaning parameter names rislabel and revison instead of a,b,c or x,y,z
use join function to add two splited string, and make it single variable as rislabel
'''