
def birday(candles_size,candles_height_list):
    # print(candles_height_list)
    candles_height_list.sort(reverse = True)
    # print(candles_height_list)
    # print(candles_height_list[0])
    count = 0
    for i in range(len(candles_height_list)):
        if candles_height_list[i] == candles_height_list[0]:
            count= count+1
            
    return count



if __name__ == '__main__':
    #candles_size = int(input("enter the size of the candles: "))
    candles_size = int(input())
    #candles_height = input("enter the candles_height: ").split( )
    candles_height = input().split()
    candles_height_list = [int(i) for i in candles_height]
    answer = birday(candles_size,candles_height_list)
print(answer)