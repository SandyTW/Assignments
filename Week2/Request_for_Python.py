#!/usr/bin/python
#coding:utf-8

#要求一
def calculate(min, max):
    sum=0
    for n in range(min,max+1):
        sum=sum+n
    print(sum)
    
calculate(1,3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4,8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

#要求二
def avg(data):
    sum=0
    for i in range(0, data["count"]):
        sum=sum+data["employees"][i]["salary"]
    print(sum/data["count"])


avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})

#要求三
def maxProduct(nums):
    product=0
    maxProduct=0
    if len(nums)<3:
        print(nums[0]*nums[1])
    else:
        for i in range(0,len(nums)-1):
            for k in range(i+1, len(nums)):
                product=nums[i]*nums[k]
                if product>maxProduct:
                    maxProduct=product
        print(maxProduct)
maxProduct([5,20,2,6]) #得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10,-20,0,3]) # 得到 30 因為 10 和 3 相乘得到最大值

#要求四
def twoSum(nums,target):
    for i in range(0,len(nums)-1):
        for k in range(i+1, len(nums)):
            if(nums[i]+nums[k]==target):
                return [i,k]
result=twoSum([2,11,7,15],9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#要求五
def maxZeros(nums):
    maxCount=0
    count=0
    for i in range(0,len(nums)):
        if nums[i]==0:
            count+=1 
            maxCount=max(count,maxCount)          
        else:  
            count=0
    print(maxCount)
                
maxZeros([0,1,0,0])  # 得到 2
maxZeros([1,0,0,0,0,1,0,1,0,0])  # 得到 4
maxZeros([1,1,1,1,1])   # 得到 0

