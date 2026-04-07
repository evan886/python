# def reve(s):
#     return  " ".join(s.split()[::-1])
#
# print(reve("hello world foo"))

# lst = [3,1,4,1,5,9,2,6,5]
#
# print(sorted(lst))
# print(sorted(lst,reverse=True))
# print(sum(lst)) 
#
# print(lst.count(5))
#
# print(list(set(lst)))

# lst = ["apple","banana","cherry"]
#
# for i , val  in enumerate(lst):
#     print(f"index {i}: {val}")

#
# for a,b in zip([1,2,3],["x","y","z"]):
#     print(a,b)

# sq = [x**2 for  x in range(10)]
# print(sq)
# d = {"name": "EVAN", "age": 40}
#
# print(d.get("name"))
# print(d.get("sala",0))
# evens = [x for x in range(20) if x % 2 == 0]
# print(evens)

# marrix = [[i*j for j in range(1,4)] for i in range(1,4)]
# print(marrix)

# # squqres = [x**2 for x in range(10)]
# squqres = [x**2 for x in  range(20) if x % 2 ==0]
# print(squqres)
# 第一步：手打操作
#
# d = {"name": "alice","age": 25}
# # print(d.get("name"))
# # print(d.get("sala",0))
#
# for k,v in d.items():
#     print(k,v)
#
# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a & b)
# print(a | b)
# print(a - b)

# students = [("alice",85),("bob",92),("charlie",78),("dave",85)]
# # print(sorted(students,key=lambda x: x[1]))
#
# # print(sorted(students,key=lambda x: x[1],reverse=True))
# print(sorted(students,key=lambda  x: (-x[1],x[0])))




# people = [{"name":"alice","age":30},{"name":"bob","age":25}]
# print(sorted(people,key=lambda x: x["age"]))

def two_sum(nums,target):
    seen = {}
    for i,n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen [complement],i]
        seen[n] = i
    return  []

print(two_sum([2,7,11,15],9))