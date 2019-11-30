# s = ""
# dp1 = [0] * 27
# dp2 = [0] * 27
# s = input()
# n = len(s)

# for i in range(n):
#     dp2[ord(s[i]) - ord('a')] += 1

# ans = 0

# for i in range(n):
#     c= s[i]
#     dp1[ord(c) - ord('a')] += 1
#     dp2[ord(c) - ord('a')] -= 1
#     temp = 0
#     for j in range(26):
#         temp += min(dp1[j], dp2[j])

#     ans = max(ans, temp)


# print(ans)

def strangeSort(mapping, nums):
    # STRING_ARRAY=[]
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            num1=nums[j]
            num2=nums[j+1]
            mapped1=''
            mapped2=''
            for k in num1:
                c= k
                digit=ord(c)-ord('0')
                # print(digit)
                for x in mapping:
                    if x==digit:
                        mapped1+=str(x)
                        break
            for k in num2:
                c=k
                digit=ord(c)-ord('0')
                # print(digit)
                for x in mapping:
                    if mapping[x]==digit:
                        mapped2+=str(x)
                        break
            # print(mapped1,mapped2)
            if int(mapped1)>int(mapped2):
                nums[j]=num2
                nums[j+1]=num1
            

    return nums

mapping = [3, 5, 4, 6, 2, 7, 9, 8, 0, 1 ]

nums = ["990", "332", "32" ]

print(strangeSort(mapping,nums))