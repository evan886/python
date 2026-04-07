# s = "Hello World "
# print(s[::-1])
# print(s.upper())
# print(s.lower())
# print(s.strip())
# print(s.split(" "))
# print('********')
# print("-".join(["a","b","c"]))
# print(s.replace("l","x"))
# print(s.count("l"))
# print(s.find("World"))
# print(s.startswith("He"))
# print(s.isdigit())
# print(s.isalpha())
# #Mar 24

def two_sum(nums,target):
    seen = {}
    for i,n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen [complement],i]
        seen[n] = i
    return  []

print(two_sum([2,7,11,15],9))