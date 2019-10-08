from challenges.fibonacci import Fibonacci

# Challenge 4 - Operators and Functions:
# For this challenge, we will be using operators and functions to tinker around w/ string concatenation and tokenization.
# String concatenation is the process of putting together a message using multiple variables.
# The application of this can be for logging or capturing variables or using a dynamic variable that is found on a page before it’s used to trigger an action.
# Tokenization is needed for breaking up a sentence or to break up a long string into arrays so that you can example each word.
# It can also be used to pull variables out of the URLs.
# There are endless uses.
#
# For this challenge, we are going to write a function that display the fibonacci sequence up to a certain number.
# If I want the fibonacci for the 9 order of the sequence, I should see 21.
# Keep your function to calculate the fibonacci sequence separate from the file that has the unittest.main().
#
# However, to add additional challenge to this challenge, instead of displaying the number 21, I want the string representation of twenty one.
# This will require you to use string concatenation to print out the string.
#
# Your console output will look something like this.
#
# 13 - thirteen
# 144 - one hundred forty four
# 7408 - seven thousand four hundred eight
#
# Now that you know how to write a function, copy your previous challenge folder and create a new folder.
# Now let’s refactor your “before” method and make it a one line call out to another function.
# The reason why we do this is so that we only have one function that does our initialization of the driver.
# Otherwise, the poor implementation would be to copy multiple lines from script to script.
# When it comes time to change the “before” method, you will have to change it in multiple places versus one.
#
# **** Do not use someone else’s library.
# You should write your own logic.
# Keep non related classes separate.  ie. Fibnacci class has no relations to convertNumbertoString class ****


Fibonacci(50)
