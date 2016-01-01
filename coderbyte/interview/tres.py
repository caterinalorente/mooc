def solution(A):
    index_of_biggest_number_so_far = 0
    
    for i in range(len(A)-1):
        if A[i] > A[i+1]: 
            index_of_biggest_number_so_far = i
            break
    for i in range(index_of_biggest_number_so_far + 1, len(A)):
        if A[index_of_biggest_number_so_far] < A[i]:
            return True
    return False

print(solution([1, 5, 3, 3, 7]))
print(solution([1, 3, 5, 3, 4]))
print(solution([1, 3, 5]))