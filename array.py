
# Q.1 Find a peak element which is not smaller than its neighbours
# Input: array[]= {5, 10, 20, 15}
# Output: 20
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.
#
# Input: array[] = {10, 20, 15, 2, 23, 90, 67}
# Output: 20 or 90
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67
# ________________________________________________________________________________________________________________________________________
# def findPeak(arr,n):
#     if n==1:
#         return 0
#     if arr[0]>=arr[1]:
#         return 0
#     if arr[n-1]>=arr[n-2]:
#         return n-1
#
#     for i in range(1,n-1):
#
#         if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
#             return arr[i]
#
#
# arr=[10,20,15,2,23,90,67]
# n=len(arr)
# print(findPeak(arr,n))
# ____________________________________________________________________________________________________________________________________________________

# Q.2 . Program to find the minimum (or maximum) element of an array

# def max_min(arr):
#
#     print(max(arr),'is a max number')
#     print(min(arr),'is a min number')
#
#
# arr=[1,2,3,4,5]
# max_min(arr)
#  ______________________________________________________________________________________________________________________________________________________________________________

# Q.3 array reverse

# def reverse(arr):
#     reversd_arr=arr[::-1]
#     for i in reversd_arr:
#         print(i,end=' ')
#
# arr=[1,2,3,4,5]
#
# reverse(arr)

# approach:2
# def reverse(str):
#     new_str=""
#     n=len(str)
#     for i in range(n-1,-1,-1):
#         new_str+=str[i]
#
#     print(new_str)
#
# reverse('uday')

# __________________________________________________________________________________________________________________________________________________

# Q.4 input: nums=[1,2,3] o/p= 6
#  i/p: nums=[1,2,3,4] o/p=24

# def product(nums,n):
#     count=1
#     for i in range(0,n):
#         count*=nums[i]
#     print(count)
#
#
# nums=[1,2,3,4]
# n=len(nums)
# product(nums,n)

# ____________________________________________________________________________________________________________________________________________________

# Q.5 K’th Smallest Element in Unsorted Array
# Given an array arr[] of N distinct elements and a number K, where K is smaller than the size of the array. Find the K’th smallest element in the given array.
#
# Examples:
#
# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3
# Output: 7
#
# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4
# Output: 10

# def smallest(arr,n,k):
#
#     small=sorted(arr)
#     print(small[k-1])
#
#
# arr=[7,10,4,3,20,15]
# n=len(arr)
# k=3
#
# smallest(arr,n,k)

# ___________________________________________________________________________________________________________________________

# Q.6 Given a sorted array arr[] of size N and a number X, you need to find the number of occurrences of X in given array.
#
# Note: Expected time complexity is O(log(n))
#
# Examples:
#
# Input: N = 7, X = 2, Arr[] = {1, 1, 2, 2, 2, 2, 3}
# Output: 4
# Explanation: 2 occurs 4 times in the given array.
#
# Input: N = 7, X = 4, arr[] = {1, 1, 2, 2, 2, 2, 3}
# Output: 0
# Explanation: 4 is not present in the given array.



# def occurance(arr,n,x):
#
#     count=0
#     for i in range(n):
#         if x==arr[i]:
#             count+=1
#
#     return count
#
# arr=[1,1,2,2,2,2,3]
# n=len(arr)
# x=int(input('Enter the number: '))
#
# print(occurance(arr,n,x))

# _______________________________________________________________________________________________________________________
# Q.7 Find Subarray with given Sum from Array of non-negative Numbers
# Given a 1-based indexing array arr[] of non-negative integers and an integer sum. You mainly need to return the
# left and right indexes(1-based indexing) of that subarray. In case of multiple subarrays, return the subarray indexes
# which come first on moving
# from left to right. If no such subarray exists return an array consisting of element -1.


# Input: arr[] = { 15, 2, 4, 8, 9, 5, 10, 23}, sum = 23
# Output: 2 5
# Explanation: Sum of elements between indices 2 and 5 is 2 + 4 + 8 + 9 = 23
#
# Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
# Output: 2 5
# Explanation: Sum of elements between indices 1 and 4 is 4 + 0 + 0 + 3 = 7
#
# Input: arr[] = {1, 4}, sum = 0
# Output: -1
# Explanation: There is no subarray with 0 sum


# def subarray_sum(arr, n, sum):
#     last = 0 # 3
#     start = 0 #1
#     currsum = 0  #15+2+4+8=29, #14+2=16
#     flag = False
#     res = []
#
#     # Iterate over the array
#     for i in range(n):
#         # Store sum up to current element
#         currsum += arr[i] # 15,2,
#
#         # Check if current sum is greater than or equal to given number
#         if currsum >= sum: # 16>=2300
#             last = i
#
#             # Start from starting index till current index
#             while sum < currsum and start < last:  #23 < 29 and 0<3
#                 # Subtract the element from left
#                 currsum -= arr[start]  # 29 -=arr[0]=15
#                 start += 1
#
#             # If current sum becomes equal to given number
#             if currsum == sum:  #29 == 23
#                 res.append(start + 1)
#                 res.append(last + 1)
#                 flag = True
#                 break
#
#     # If no subarray is found, store -1 in result
#     if not flag:
#         res.append(-1)
#
#     # Return the result
#     return res
#
#
# # Driver Code
# arr = [15, 2, 4, 8, 9, 5, 10, 23]
# n = len(arr)
# sum = 23
# res = subarray_sum(arr, n, sum)
# for i in res:
#     print(i, end=" ")

# _____________________________________________________________________________________________________________________________

# Q.8 Move all negative numbers to beginning and positive to end with constant extra space

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5
#
# def negative(arr,n):
#     neg=[]
#     pos=[]
#     for i in range(n):
#         if arr[i]<0:
#             neg.append(arr[i])
#         else:
#             pos.append(arr[i])
#
#     return neg+pos
#
# arr=[-12,11,-13,-5,6,-7,5,-3,-6]
# n=len(arr)
#
# print(negative(arr,n))
# or
# arr.sort(key=lambda x:x<0)
# ___________________________________________________________________________________________________________________________________
# Q.9
# Union and Intersection of two sorted arrays
# Input: arr1[] = {1, 3, 4, 5, 7}
#         arr2[] = {2, 3, 5, 6}
# Output: Union : {1, 2, 3, 4, 5, 6, 7}
#          Intersection : {3, 5}


# arr1=[1,3,4,5,7]
# arr2=[2,3,5,6]
#
# set1=set(arr1)
# set2=set(arr2)
#
# result1=list(set1.union(set2))
# result2=list(set1.intersection(set2))
#
# print(f'union:{result1}')
# print(f'intersection:{result2}')

# or

# class Solution:
#     # Function to return the count of number of elements in union of two arrays.
#     def doUnion(self, arr1, arr2):
#         set1 = set(arr1)
#         set2 = set(arr2)
#         result1 = set1.union(set2)
#
#         return len(result1)
#         # code here
