# Program to print this pattern
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def main():
    k=0
    for i in range(0,5):
        for j in range(0,5):
            if i==j:
                print("*"*i)
                k+=1
            elif i != j:
                print(end="")
        if k == 5:
            break
    for x in range(5,0,-1):
        print("*"*x)
        

if __name__ == "__main__":
    main()