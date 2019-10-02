import math
import random
import time


def randNumbers(n):
    nums = []
    for i in range(0, n):
        nums.append(random.randint(0, 9))
    return nums, random.randint(0, 9999)

def addOperands(nums):
    expr = []
    for i in range(2, 2 * len(nums) + 1):
        if (i % 2 == 0):
            expr.append(nums[int(i / 2) - 1])
        else:
            r = random.choice("+-/*")
            expr.append(r)
    return expr

def listToString(expr):
    st = ""
    for a in expr:
        st = st + "" + str(a)
    return st

def evaluate(expr):
    value = 0
    leftHand = expr[0]
    for i in range(1, len(expr), 2):
        operator = expr[i]
        rightHand = expr[i + 1]
        if operator == "+":
            value = leftHand + rightHand
        elif operator == "-":
            value = leftHand - rightHand
        elif operator == "*":
            value = leftHand * rightHand
        elif operator == "/":
            if rightHand == 0:
                value = 0
            else:
                value = leftHand / rightHand
        # print("     ",leftHand," ",operator," ",rightHand, " = ",value)
        leftHand = value
    return value

def swap(expr, i, j):
    neighbor = expr.copy()
    temp = neighbor[j]
    neighbor[j] = neighbor[i]
    neighbor[i] = temp
    return neighbor

def changeSign(expr, i, sign):
    neighbor = expr.copy()
    neighbor[i] = str(sign)
    return neighbor

def hillclimb(expr, target, best):
    #print(submation(int((len(expr)+1)/2)) + 3*(int((len(expr)+1)/2)-1))
    for k in range(1, len(expr) - 1, 2):
        for c in "+-*/":
            if expr[k] != c:
                neighbor = changeSign(expr, k, c)
                #print(k, " ", c, " ", neighbor)
                val = abs(evaluate(neighbor) - target)
                if val < best:
                    print("     Best State:", listToString(neighbor))
                    print("     Distance From Target:", val)
                    print()
                    return hillclimb(neighbor.copy(), target, val)
    for i in range(0, len(expr), 2):
        for j in range(i, len(expr), 2):
            if i != j:
                neighbor = swap(expr, i, j)
                val = abs(evaluate(neighbor) - target)
                if val < best:
                    print("     Best State:", listToString(neighbor))
                    print("     Distance From Target:", val)
                    print()
                    return hillclimb(neighbor.copy(), target, val)
                #print(i, " ", j, " ", neighbor)
    return expr, best


def RRIteration(nums, sec, target):
    t_end = time.time() + sec
    print("Number set:", nums)
    print("Target: ", target)

    times = 1
    overall = math.inf
    bestexp=[]
    while time.time() < t_end and overall!=0.0:
    #while times < 2:
        random.shuffle(nums)
        expr = addOperands(nums)
        print("***************************************")

        print("RR Iteration:", times, "    Goal: ", target)
        if overall != math.inf:
            print()
            print("Overall Best:", abs(evaluate(bestexp) - target))
            print("Best Expression:",listToString(bestexp))
            print()
        times += 1
        print("     Start: ", listToString(expr))
        start = abs(evaluate(expr) - target)
        print("     Distance From Target:", start)
        print()
        expr, best = hillclimb(expr, target, start)
        if best < overall:
            overall = best
            bestexp=expr

    print("***************************************")
    print()
    print("Overall Best:", abs(evaluate(bestexp) - target))
    print("Best Expression:", listToString(bestexp))
    print()
def main():
    nums, target = randNumbers(100)
    RRIteration(nums, 60, target)


if __name__ == '__main__':
    main()
