# position of s & t
# position of apple and orange a & b
# total no of apple and orange are fall m & n
# positions of fallen apple from apple tree -->> a
# position of fallen orange from orange tree -->> b

def main(s,t,a,b,m,n,appleDistance,orangeDisatance):
    apple = []
    orange = []
    for i in appleDistance:
        if a + i >= s and a +i <= t:
            # print(a+i)
            # print(apple)
            apple.append(1)
            # print(apple)
    
    for i in orangeDisatance:
        if b + i >= s and b + i <= t:
            # print(b+i)
            # print(orange)
            orange.append(1)
            # print(orange)
        
    totalFruits = []
    x = sum(apple)
    y = sum(orange) 
    totalFruits.append(x)
    totalFruits.append(y)
    # print(totalFruits)
    
    return totalFruits



if __name__ == "__main__":
    housePosition = input()
    str_end_pos = housePosition.split(" ")
    s_t = [eval(i) for i in str_end_pos]
    s = s_t[0]
    t = s_t[1]

    treesPosition = input()
    apple_orange = treesPosition.split(" ")
    a_b = [eval(i) for i in apple_orange]
    a = a_b[0]
    b = a_b[1]

    fruitsFallen = input()
    fruits = fruitsFallen.split(" ")
    m_n = [eval(i) for i in fruits]
    m = m_n[0]
    n = m_n[1]

    applePosition = input()
    apple_pos = applePosition.split(" ")
    appleDistance = [eval(i) for i in apple_pos]

    orangePosition = input()
    orange_pos = orangePosition.split(" ")
    orangeDistance = [eval(i) for i in orange_pos]

    # print("=============================")

    nearHouse = main(s,t,a,b,m,n,appleDistance,orangeDistance)
    print(*nearHouse, sep = "\n")

