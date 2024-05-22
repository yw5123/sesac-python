def remove_duplicate(numbers):
    unique_list = []

    for n in numbers:
        if n not in unique_list:
            unique_list.append(n)

    # for n in numbers:
    #     duplicate_check = False
    #     for u in unique_list:
    #         if n == u:
    #             duplicate_check = True
    #             break
    #     if duplicate_check is False:
    #         unique_list.append(n)
    
    return unique_list

def remove_duplicate2(numbers):
    return list(set(numbers))

numbers = [1,2,4,3,2,5,1,6,2,3,5,1,7,4,8,8,1,9]
unique_numbers = remove_duplicate(numbers)
unique_numbers2 = remove_duplicate2(numbers)

print("원본 리스트: ", numbers)
print("유닉 리스트: ", unique_numbers)
print("유닉 리스트: ", unique_numbers2)