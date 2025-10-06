"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40
print (type (EXPECTED_BAKE_TIME))

print (EXPECTED_BAKE_TIME)
PREPARATION_TIME = 2
print (type(PREPARATION_TIME)) 


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
  
def preparation_time_in_minutes(number_of_layers):
    """Calculate total preparation time based on number of layers.

    :param number_of_layers: int - the number of layers added to the lasagna.
    :return: int - total preparation time (in minutes), where each layer takes PREPARATION_TIME minutes.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed time spent preparing and baking the lasagna.

    :param number_of_layers: int - number of layers added to the lasagna.
    :param elapsed_bake_time: int - time already spent baking in the oven.
    :return: int - total elapsed time (in minutes), combining preparation and baking.
    """
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time


