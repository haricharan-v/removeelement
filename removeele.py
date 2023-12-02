from typing import List
def remove_element(nums: List[int], target: int) -> int:
    index = 0

    while index < len(nums):
        if nums[index] == target:
            nums.pop(index)
        else:
            index += 1

    return len(nums)

def main():
    # Take user input for the list
    nums_input = input("Enter a list of integers separated by space: ")
    nums = list(map(int, nums_input.split()))

    # Take user input for the target integer
    target = int(input("Enter the target integer: "))

    # Call the remove_element function
    result = remove_element(nums, target)

    # Display the result
    print(f"Modified list: {nums}")
    print(f"Length of modified list: {result}")

main()
