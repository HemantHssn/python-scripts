"""
grading students.....

* less than 40 ----->>> failing grade
* if ( grade - next multiple of 5 ) < 3 ----->>>> round grade to next multiple of 5 
* if the above difference is >= 3 ------->>>> don't round of the grade  

"""
def final_grades(grade):

    # print(grade)
    for i in range(len(grade)):
        # print(f"this is the i value ----->>>> {i}")
        score = grade[i]
        if score < 38:
            print(score)
            # print(f"grade [i] value ----->>>> {grade[i]} which is equalent to score ------->>>> {score} where i is ------>>>>>{i}")
            
        elif score >= 38:
            for x in range(0,5):
                # print(f"this is the x value ------>>>>> {x}")
                sum_up_value = score + x
                # print(f"the sum_up_value ------->>>>> {sum_up_value}")
                remainder = sum_up_value % 5
                # print(f"this is the remainder value {remainder}")
                if remainder == 0:
                    # print(f"the value of differece ------->>>>> {x}")
                    if x < 3:
                        print(sum_up_value)
                    else:
                        print(score)
                        break

                    break
                
                    
                    



    return None




if __name__ == '__main__':
    n = int(input())
    # print(n)
    # print(type(n))
    grade = []
    for i in range (0,n):
        grade.append(int(input()))
 
     # print(grade)
        
    result = final_grades(grade)
          