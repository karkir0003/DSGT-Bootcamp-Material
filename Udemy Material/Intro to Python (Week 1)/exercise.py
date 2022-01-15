#This file contains the functions you will need to implement for Drill 1 of DSGT Bootcamp

def cube(n):
    """
    Given a number n, return the cube of the number. For example, cube(4) = 64
    """
    #YOUR CODE HERE
    raise NotImplementedError("Did not implement the cube function")

def factorial(n):
    """
    Given a number n, return n!. Make sure to handle the relevant edge cases
    """
    #YOUR CODE HERE
    raise NotImplementedError("Did not implement the factorial function")

def count_digits(n):
    """
    Given a non-negative integer, return the number of digits
    """
    #YOUR CODE HERE
    raise NotImplementedError("Did not implement the count_digits function")

def average_grade(scores, targetGrade):
    """
      Given a set of exam scores as such: {"Exam 1": 43, "Exam 2": 59, "Exam 3": 60, "Exam 4": 90}
  
      Find how much the student will need to score on the final exam to acheive the target grade. Assume that all exams (including the final exam) are weighted equally
      for the sake of simplicity.

      In the above example, if the student wants to have a target grade of 70, the student will need to score a 98 on the final (70* 5 exams = 43+59+60+90 + X. Solve the equation for X)

      Assume that scores will always be a nonempty dictionary
    """
    #YOUR CODE HERE
    raise NotImplementedError("Did not implement the average_grade function")

def slice_product(numList, start_pos, end_pos):
    """
    Given a list of numbers, a start index, and end index, find the product of the entries in the given slice. Below is an example

    Suppose that the list is [1,2,3,4,5], start_pos = 1, end_pos = 3, then slice_product should return 24 (lists are zero-indexed in the sense that the first element in the list is at index 0, so 2*3*4 = 24)

    If the start_pos is a negative number, raise/throw a ValueError with an informative reason. If the end_pos is an integer that is at least the length of the list, raise/throw a ValueError (eg: in the above array, if end_pos >= 5, raise a ValueError.)

    If the end_pos is smaller than the start_pos, raise/throw a ValueError as well. The start_pos and end_pos are guaranteed to be integers.
    """
    #YOUR CODE HERE
    raise NotImplementedError("Did not implement slice_product function")

def encrypt(message, shift):
    """
    This function is responsible for encrypting a message using Caesar Cipher. The Caesar Cipher is basically shifting the alphabet. For example, if the shift is 2, then a becomes c, b becomes d and so on.
    If the shift is 1, then a becomes b, b becomes c and so on.

    Helpful Link to understand Caesar Cipher: https://medium.com/blockgeeks-blog/cryptography-for-dummies-part-2-the-caesar-cipher-665106afac78

    If the shift value is negative, you will need to perform a manipulation to find an equivalent shift value (for example if shift was -27, the equivalent shift value that's positive is 25)

    (Hint: For the shift value case, think mathematically how the Cipher works)

    Caesar Cipher is case insensitive!!! ("J" shifted by 3 should be treated the same as "j" shifted by 3 for example). How can you use this property to simplify your solution?
    """
    #YOUR CODE HERE
    raise NotImplementedError("Did not implement encrypt function")

def decrypt(message, shift):
    """
    Same rules as encrypt, but decrypt the message
    """
    #YOUR CODE HERE
    raise NotImplementedError("Did not implement decrypt function")
