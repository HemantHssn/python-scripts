
def calculating(a,b):
    # print(f"this p1 {a}\nthis is p2 {b}")
    p1 = 0
    p2 = 0
    if int(a[0]) > int(b[0]):
        p1 = +1
        # print(f"p1 got 1point")
    elif int(a[0]) == int(b[0]):
        # print(f"no points are earned")
        pass
    else:
       p2 = p2 + 1
    #    print(f"p2 got 1point")
    if int(a[1]) > int(b[1]):
       p1 = p1 + 1
    #    print(f"p1 got 1point")
    elif int(a[1]) == int(b[1]):
        # print(f"no points are earned")
        pass
    else:
       p2 = p2 + 1
    #    print(f"p2 got 1point")   
    if int(a[2]) >int(b[2]):
    #    print(type(a[2]),type(b[2]))
       p1 = p1 + 1
    #    print(f"p1 got 1point")
    elif int(a[2]) == int(b[2]):
        # print(f"no points are earned")
        pass 
    else:
       p2 = p2 + 1
    #    print(f"p2 got 1point")
    

    print(f"{p1} {p2}")
    return None



if __name__ == "__main__":
    person1 = input()
    data1 = person1.split(" ")
    # print(data1)
    person2 = input()
    data2 = person2.split(" ")
    # print(data2)
    calculating(data1,data2)
   