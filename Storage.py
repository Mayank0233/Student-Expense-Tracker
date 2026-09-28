import os



def save(item, cat, cost):
    f = open("expenses.txt", "a")
    f.write(item + "," + cat + "," + str(cost) + "\n")
    f.close()

def read():
    try:
        f = open("expenses.txt", "r")
        data = f.readlines()
        f.close()
        return data
    except:
     return []



