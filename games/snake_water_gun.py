import random

def calculation(a,b):

    final_user = sum(a)
    final_machine = sum(b)
    print(f"\nYour Total Score : {final_user}\n"f"Machine Total Score : {final_machine}\n")
    if final_user > final_machine:
        print(f"OH MY GOODNESS YOU WON AGAINST ME...!!!!\n""         PLAY AGAIN......")
    elif final_user == final_machine:
        print("!!!!!!!!!!!!!!!! DRAW MATCH !!!!!!!!!!!!!!! TRY AGAIN !!!!!!!!!!!!!!")
    else:
        print("I Told You In The Begining, You Can't Win Against Me \n""You Can Try Once More Also..........")
    return None

def score(a,b):
    user_points = []
    machine_points = []
    points1 = 0  # user initial points
    points2 = 0  # machine initial points

    for i in range(len(a)):

        if a[i] == b[i]:

            points1 = 0  
            points2 = 0
            user_points.append(points1)
            machine_points.append(points2)

            pass
        elif a[i] == 1 and b[i] == 2: # snake wins against water --->>> points for user 
            points1 = 1
            points2 = 0
            user_points.append(points1)
            machine_points.append(points2)
            pass
        elif a[i] == 1 and b[i] == 3: # snake looses against gun --->>> points for machine
            points1 = 0 
            points2 = 1
            user_points.append(points1)
            machine_points.append(points2)
            pass
        elif a[i] == 2 and b[i] == 1: # water looses against snake --->>> points for the machine 
            points1 = 0
            points2 = 1
            user_points.append(points1)
            machine_points.append(points2)
            pass
        elif a[i] == 2 and b[i] == 3: # water wins against the gun --->>> points for the user 
            points1 = 1
            points2 = 0
            user_points.append(points1)
            machine_points.append(points2)
            pass
        elif a[i] == 3 and b[i] == 1: # gun wins against the sanake --->>> points for the user
            points1 = 1
            points2 = 0
            user_points.append(points1)
            machine_points.append(points2)
            pass
        elif a[i] == 3 and b[i] == 2: # gun looses against the water --->>> points for the machine 
            points1 = 0
            points2 = 1
            user_points.append(points1)
            machine_points.append(points2)
            pass

    print("###################################################################")
    print(f"User Points : {user_points}\n"f"Machine Points : {machine_points}")
    print("###################################################################")

    calculation(user_points,machine_points) 
    return None 


def develop(series):
    print("==========================================================")
    user = []
    machine =[]
    if series != 3 and series != 5:
        print("ERROR....!!!!\n""You Can Choose Either 3 or 5 Only.....\n""Thankyou")
    elif series == 3 or 5:
        for i in range(series):
            my_dict = {"1" : "snake", "2" : "water", "3" : "gun"}
            user_action = int(input("\nEnter The Corresponding Action To Value :\n"" 1 = SNAKE \n"" 2 = WATER \n"" 3 = GUN\n"))
            if user_action not in [1,2,3]:
                print(f"\nYou Can Select Either 1,2 or 3 Only.....\nWhere,\n1 = SNAKE \n2 = WATER \n3 = GUN\n\nThankyou")
            else:
                user.append(user_action)
                machine_action = random.randint(1,3)
                print(f"This Is Machine Action {machine_action} Which Reflects {my_dict[str(machine_action)]}")
                print(f"This Is User Action {user_action} Which Reflects {my_dict[str(user_action)]}")
                machine.append(machine_action)
                print(f"User Input By Till This Time    --->>> {user}\n"f"Machine Input By Till This Time --->>> {machine}")
    
        score(user,machine)

    return None





if __name__ == "__main__":
    print("<<<< WELCOME TO GAME>>>>\n""             BE READY TO ***LOOSE***")

    series = int(input("\nEneter The Series You Wish To Play Either 3 or 5 \n"))
    start = develop(series)







