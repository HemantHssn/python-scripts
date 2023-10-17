
# grading is done from 0 to 100
# if score is less than 40 is failing 
# grade = score
 # if score + x >> 40
# score + x  is divisible by 5
# if x << 3 ; grade = score + x
# if x => 3 ; grade = score

def main(markLst):
    finalMarks = []
    for i in ([eval(i) for i in (markLst)]):
            apparScore = i
            for j in range(0,6):
                # print(j)
                if ((apparScore + j) % 5 ) == 0:
                    x = j
            if apparScore >= 38 :
                grade = apparScore
                if x >= 3:
                    finalMarks.append(grade)
                else:
                    grade = apparScore + x
                    finalMarks.append(grade)
                    
            else:
                grade = apparScore
                finalMarks.append(grade)
    return finalMarks






if __name__ == "__main__":
    noStud = int(input())   # "enter the no of students :\n"
    # print(type(noStud))
    marksLst = []
    for i in range(noStud):
        score = input() # Enter the marks
        marksLst.append(score)
    grade = main(marksLst)
    # print(marksLst)
    # print("------------------") 
    print(*grade, sep = "\n")  # x\ny\nz
    # print(*grade) ----->>>> op ---->>> x y z 
    