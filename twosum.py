def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum=array[i]
        for j in range (i+1, len(array)):
            secondNum=array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]

    return []           


def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialtarget=targetSum + num
        if potentialtarget in nums:
            return [potentialtarget, num]
        else:
            nums[num]= True

def twoNumberSum(array, targetSum):
    array.sort
    l = 0
    r= len(array)-1

    while l<r:
        currentSum=array[l] + array[r]
        if currentSum == targetSum:
            return [array[l],array[r]]
        elif currentSum > targetSum:
            r -= 1
        elif currentSum < targetSum:
            l += 1
    return []