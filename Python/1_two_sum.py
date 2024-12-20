from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    num_set = set(nums[1::])
    for i, num in enumerate(nums):
        search_num = target - num
        if search_num in num_set:
            if search_num == num:
                if num in nums[i + 1 : :]:
                    return [i, nums.index(search_num, i + 1)]
            else:
                return [i, nums.index(search_num, i + 1)]
    return []


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))

numbers = [2, 3, 4]
target = 6
print(twoSum(numbers, target))

numbers = [1, 3, 4, 2]
target = 6
print(twoSum(numbers, target))

numbers = [3, 24, 50, 79, 88, 150, 345]
target = 200
print(twoSum(numbers, target))

numbers = [5, 25, 75]
target = 100
print(twoSum(numbers, target))

numbers = [0, 0, 3, 4]
target = 0
print(twoSum(numbers, target))

numbers = [
    12,
    13,
    23,
    28,
    43,
    44,
    59,
    60,
    61,
    68,
    70,
    86,
    88,
    92,
    124,
    125,
    136,
    168,
    173,
    173,
    180,
    199,
    212,
    221,
    227,
    230,
    277,
    282,
    306,
    314,
    316,
    321,
    325,
    328,
    336,
    337,
    363,
    365,
    368,
    370,
    370,
    371,
    375,
    384,
    387,
    394,
    400,
    404,
    414,
    422,
    422,
    427,
    430,
    435,
    457,
    493,
    506,
    527,
    531,
    538,
    541,
    546,
    568,
    583,
    585,
    587,
    650,
    652,
    677,
    691,
    730,
    737,
    740,
    751,
    755,
    764,
    778,
    783,
    785,
    789,
    794,
    803,
    809,
    815,
    847,
    858,
    863,
    863,
    874,
    887,
    896,
    916,
    920,
    926,
    927,
    930,
    933,
    957,
    981,
    997,
]
print(numbers[23], numbers[31])
print()
target = 542
print(twoSum(numbers, target))

numbers = [
    4,
    15,
    24,
    28,
    32,
    34,
    38,
    52,
    56,
    60,
    63,
    65,
    79,
    108,
    123,
    139,
    147,
    149,
    150,
    152,
    161,
    175,
    178,
    182,
    187,
    188,
    194,
    203,
    212,
    217,
    227,
    229,
    230,
    231,
    240,
    243,
    251,
    255,
    258,
    265,
    268,
    272,
    289,
    295,
    301,
    304,
    307,
    316,
    329,
    335,
    349,
    351,
    356,
    359,
    370,
    370,
    373,
    377,
    387,
    388,
    400,
    405,
    409,
    415,
    425,
    430,
    440,
    441,
    447,
    449,
    459,
    470,
    471,
    484,
    493,
    494,
    508,
    509,
    510,
    523,
    527,
    529,
    533,
    542,
    547,
    555,
    566,
    570,
    619,
    620,
    627,
    636,
    643,
    645,
    648,
    650,
    657,
    659,
    669,
    677,
    685,
    689,
    699,
    704,
    710,
    721,
    727,
    736,
    740,
    745,
    766,
    771,
    773,
    781,
    795,
    805,
    817,
    843,
    849,
    851,
    860,
    873,
    899,
    907,
    950,
    955,
    959,
    965,
    968,
    977,
    988,
    989,
]
target = 718
print(twoSum(numbers, target))
