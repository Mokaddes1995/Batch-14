# # ধারাবাহিক সংখ্যা

# def consecutive_numbers(n):
    
#     a = list(map(int, input().split()))
    
#     for i in range(n - 1):
        
#         sort = False
        
#         for j in range(n - i - 1):
            
#             if a[j] > a[j + 1]:
                
#                 a[j], a[j + 1] = a[j + 1], a[j]
                
#                 sort = True
                
#         if not sort:
            
#             break

#     ConsecutiveNumbers = True
        
#     for k in range(n - 1):
        
#         if a[k + 1] - a[k] != 1:
            
#             ConsecutiveNumbers = False
            
#             break
            
        
#     if ConsecutiveNumbers:

#         return "true"
        
#     else:
        
#         return "false"
        

# n = int(input())

# print(consecutive_numbers(n))


# # স্ট্রিং দৈর্ঘ্য অনুযায়ী সর্টিং


# n = int(input())

# strings = list(input().split(" "))


# sorted_string = sorted(strings, key= lambda x: len(x), reverse=False)

# for i in sorted_string:
    
#     print(i, end=" ")


# বেজোড় ইন্টিজারটিকে খুঁজে বের কর


def get_odd_integer(arr):
    
    freq = {}
    
    for i in arr:
        
        if i not in freq:
            
            freq[i] = 1
        else:
            
            freq[i] += 1
    
    
    for key in freq.keys():
        
        if freq[key] % 2 != 0:
            
            print(key, end='')




arr = list(map(int, input().split(" ")))

get_odd_integer(arr)