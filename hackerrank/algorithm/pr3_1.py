

def main(a,b):
    p1 = 0
    p2 = 0
    for i in range(0,3):
        if int(a[i]) > int(b[i]):
            p1 += 1
            pass
        elif int(a[i]) < int(b[i]):
            p2 += 1
        else:
            pass 
    print(f"{p1} {p2}") 
    return None

if __name__ == "__main__":
    person1 = input()
    data1 = person1.split(" ")
    # print(data1)
    person2 = input()
    data2 = person2.split(" ")
    # print(data2)
    main(data1,data2)
  
    
   