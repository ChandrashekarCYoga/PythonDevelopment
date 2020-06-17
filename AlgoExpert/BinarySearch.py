import unittest


def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def binarySearchR(array, target):
    return binarySearchHelperR(array, target, 0, len(array) - 1)


def binarySearchHelperR(array, target, left, right):
	if left > right:
		return -1
	middle = (left + right) // 2
	potentialMatch = array[middle]
	if target == potentialMatch:
		return middle
	elif target < potentialMatch:
		return binarySearchHelperR(array, target, left, middle - 1)
	else:
		return binarySearchHelperR(array, target, middle + 1, right)


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch(
            [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)

    def test_case_2(self):
        self.assertEqual(binarySearchR(
            [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)

if __name__ == '__main__':
    unittest.main()
