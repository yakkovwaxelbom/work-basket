import copy


def is_power_of_2(n) -> bool:
    while n != 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True


def solving_josephus_problem(n) -> int:
    if is_power_of_2(n):
        return 1
    else:
        k = 0
        while 2 ** k < n:
            k += 1
        k -= 1
        survives = (n - 2 ** k) * 2 + 1
        print(2 ** k)
        return survives


def find_nax_word(word: str) -> tuple:
    abc = {}
    for i in word:
        abc.update({i: 0})
    for i in word:
        abc.update({i: abc.get(i) + 1})
    return max([(value, key) for key, value in abc.items()])


def find_nax_word1(word) -> tuple:
    abc = {}
    for i in word:
        abc[i] = 0
    for i in word:
        abc[i] += 1
    abc.pop(' ')
    return max((value, key) for key, value in abc.items())


def euclid(a, b) -> int:
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return euclid(b, a % b)


def foreign_numbers(a, b) -> int:
    if euclid(a, b) == 1:
        return True


def third_maximum_number(array: list) -> float:
    for i in range(2):
        index = array.index(max(array))
        del array[index]
    return max(array)


def maximum_subarray(array: list, num: int) -> list:
    solution_subarray = []
    subarray, sum_subarray, start = [], 0, 0
    for i in range(len(array)):
        if sum_subarray < num:
            subarray.append(array[i])
            sum_subarray += array[i]
        if sum_subarray > num:
            while sum_subarray > num:
                sum_subarray -= subarray[0]
                subarray.pop(0)
                start += 1
        if sum_subarray == num:
            if len(solution_subarray) < len(subarray):
                solution_subarray = copy.deepcopy(subarray)
                sum_subarray -= subarray[0]
                subarray.pop(0)
                start += 1
    return solution_subarray


def both_are_zero(array, pointer_l, pointer_r):
    count_l = 0
    count_r = 0
    while pointer_l < pointer_r and array[pointer_l] == 0:
        count_l += 1
        pointer_l += 1
    while pointer_r > pointer_l and array[pointer_r] == 0:
        count_r += 1
        pointer_r -= 1
    return count_l, count_r


def both_are_one(array, pointer_l, pointer_r):
    count_l = 0
    count_r = 0
    while pointer_l < pointer_r and array[pointer_l] == 1:
        count_l += 1
        pointer_l += 1
    while pointer_r > pointer_l and array[pointer_r] == 1:
        count_r += 1
        pointer_r -= 1
    return count_l, count_r


def binary_subarray(array) -> tuple[int, int]:
    count_zero, pointer_l, pointer_r = 0, 0, len(array) - 1
    for i in range(len(array)):
        if array[i] == 0:
            count_zero += 1
    if count_zero == 0 or count_zero == len(array):
        raise ValueError("No subsection")
    while pointer_l < pointer_r:
        if (pointer_r - pointer_l + 1) / 2 == count_zero:
            return pointer_l, pointer_r
        elif (pointer_r - pointer_l + 1) / 2 > count_zero:

            if array[pointer_l] == 0 and array[pointer_r] == 0:
                l, r = both_are_zero(array, pointer_l, pointer_r)
                if l < r:
                    pointer_l += l
                    count_zero -= l
                else:
                    pointer_r -= r
                    count_zero -= r
            elif array[pointer_r] == 1:
                pointer_r -= 1
            else:
                pointer_l += 1
        elif (pointer_r - pointer_l + 1) / 2 < count_zero:
            if array[pointer_l] == 1 and array[pointer_r] == 1:
                l, r = both_are_one(array, pointer_l, pointer_r)
                if l < r:
                    pointer_l += l
                else:
                    pointer_r -= r
            elif array[pointer_r] == 0:
                pointer_r -= 1
                count_zero -= 1
            else:
                pointer_l += 1
                count_zero -= 1


def min_som_k(array, k):
    first_sum = sum(array[:k]), 0, k - 1
    all_sum = [first_sum]
    for i in range(k, len(array)):
        current_sum = sum(array[i - k + 1:i + 1]), i - k + 1, i
        all_sum.append(current_sum)
    print(all_sum)
    return min(all_sum)


def fix_array(array):
    count_l, count_r = 0, 0
    for i in range(len(array)):
        if array[i] < 0:
            count_l += 1
        else:
            break
    for i in range(len(array) - 1, -1, -1):
        if array[i] < 0:
            count_r += 1
        else:
            break
    return count_l, count_r


def max_subarray(array):
    current_sum, start_index, end_index, maximum_sum, current_max = 0, 0, 0, float("-Inf"), []
    for i in range(len(array)):
        current_sum += array[i]
        current_max.append((current_sum, start_index, i))
        if current_sum > maximum_sum:
            maximum_sum = current_sum
        elif current_sum <= 0:
            current_sum = 0
            start_index = i + 1
    return max(current_max), current_max


def find_pair_index(array, k):
    hash_table = {}
    for i in range(len(array)):
        hash_table[array[i]] = i
    print(hash_table)
    for i in range(len(array)):
        x = k - array[i]
        if x in hash_table and i != hash_table[x]:
            return i, hash_table[x]


def coin_concentration(array):
    max, pointer, array_l, array_r = 0, 0, [0], [0] * len(array)
    for i in range(1, len(array)):
        array_l.append((array_l[i - 1] + array[i - 1]) // 2)
    for i in range(len(array) - 2, -1, -1):
        array_r[i] = (array_r[i + 1] + array[i + 1]) // 2
    for i in range(0, len(array)):
        array_r[i] += array[i] + array_l[i]
        if array_r[i] > max:
            max, pointer = array_r[i], i
    if max != array[pointer]:
        return max, pointer
    raise ValueError("No move can be performed.")


def shit_coin(array):
    i, max_profit = 0, float('-inf')
    for j in range(1, len(array)):
        current = array[j] - array[i]
        if current > max_profit:
            max_profit = current
        if array[j] < array[i]:
            i = j
    return max_profit


def k_bonacci_iterative(n, k):
    array = [0] * (n + 1)
    for i in range(0, k):
        array[i] = i
    for i in range(k, n + 1):
        current = 0
        for j in range(0, k):
            current += array[i - j - 1]
        array[i] = current
    return array[n]


def k_bonacci(n, k):
    if n >= 0:
        if n < k:
            return n
        else:
            current = 0
            for i in range(1, k + 1):
                current += k_bonacci(n - i, k)
            return current
            
def prymery(n)
	if n > 0 and n % 1 == 0
		for i in range(n**1//2)
			if n % i == 0
				break
			else:
				print(true)
				
def is_valid_id(id_num):
     return sum([(int(digit) * (index % 2 + 1) // 10 + int(digit) * (index % 2 + 1) % 10) for index, digit in
                 enumerate(id_num)]) % 10 == 0


