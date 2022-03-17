# Conditions:
# #
# # 1. All the zeroes to the end and
# # 2. Rest of the items to be maintianed in the ascending order.
# # Function:
# # def ordered_zeros(<array>):
# # pass
# # Sample input:
# # result = non_repeating_characters([9,6,5,9,3,2,1,0,5,0,4,6,0])
# # Sample Output: [1,2,3,4,5,5,6,6,9,9,0,0,0]


def ordered_zeros(L):
    if type(L)==list:
        L.sort()
        k = 0
        for i in range(len(L)):
            if L[i] != 0:
                L[k] = L[i]
                k += 1
        for j in range(k, len(L)):
            L[j] = 0
        return L

    else:
        return 'invalid input'

print(ordered_zeros([9,6,5,9,3,2,1,0,5,0,4,6,0]))





