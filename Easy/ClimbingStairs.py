# 70. Climbing Stairs
# recursive - not efficient solution
def climbStairs(n: int) -> int:
    return calcMaxWayToCLimb(n, 0)


def calcMaxWayToCLimb(remain_to_climb, counter):
    if remain_to_climb == 0:
        return 1
    if remain_to_climb < 0:
        return 0
    return calcMaxWayToCLimb(remain_to_climb - 1, counter) + calcMaxWayToCLimb(remain_to_climb - 2, counter)


# efficient - fibio sequence


def climbStairs(n: int) -> int:
    step_1, step_2 = 1, 1

    for i in range(n - 1):
        temp_step = step_1
        step_1 = step_2 + step_1
        step_2 = temp_step
    return step_1


print(climbStairs(35))

# Matrix that init with 0,1s need to write function that checks id its possible to arrrive from poiint in matix to other point in matrix shen you can go only trhow 1ns