# import time
# time.sleep(2)
# print("After 2 secs")

# class Test():
#     __trr = 10
#     ret = 23

# print(dir(Test))

# import prog2

# print(prog2.add(12,32))

# import calendar as cl

# year =2022
# month =11

# mycal = cl.month(year,month)

# mycal2 = cl.monthcalendar(year,month)

# # for i in cl.day_name:
# #     print(i,end=" ")

# print(cl.firstweekday())

# print(cl.weekday(2022,11,9))

with open('tsest.txt','r') as f:
    # f_content = f.readline()
    # print(f_content)

    # for line in f:
    #     print(line,end="")

    size_to_read = 10
    f_content = f.read(size_to_read)

    while len(f_content)>0:
        print(f_content,end="//")
        f_content=f.read(size_to_read)
