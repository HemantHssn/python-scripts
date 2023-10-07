def main(hr,min,sec):
    am_pm = sec[2:4].lower()
    hr = int(hr)
    sec = sec[0:2]
    min = min[0:2]
    if am_pm == "am":
            if hr == 12:
                hr = "00"
            else:
                hr = "0" + str(hr)
                # hr = "0".join(str(hr))--------->>>> it adds "0"after each index
                
    else:
        if hr == 12:
           hr = 12
        else:
            hr = hr + 12
            
    return hr,min,sec


if __name__ == "__main__":
    # time_strinng = input("time in 12hr format hh:mm:ss:am\n")
    time_strinng = input()
    time_splited = time_strinng.split(":")
    # print(time_splited)
    hr = time_splited[0]
    min = time_splited[1]
    sec = time_splited[2]
    time_24_format = main(hr, min, sec)
    print(f"{time_24_format[0]}:{time_24_format[1]}:{time_24_format[2]}")
