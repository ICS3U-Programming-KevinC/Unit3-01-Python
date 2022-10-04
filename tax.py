# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Oct. 3, 2022
# This program calculates tax in bc

# import tax
from operator import contains
import constants


def main():
    # ask for subtotal
    subtotal = float(input("What is your subtotal? "))

    # create extra line
    print("")

    # calculate and display tax and total
    print(
        "The tax is {0:.2f}% and your total is: ${1:.2f}".format(
            constants.TAX_RATE_BRITISH_COLUMBIA,
            subtotal * (1 + constants.TAX_RATE_BRITISH_COLUMBIA / 100),
        )
    )


if __name__ == "__main__":
    main()
