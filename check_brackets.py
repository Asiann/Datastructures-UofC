# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    index = -1
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            # Process opening bracket, write your code here

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                index = i;
                break
            opened = opening_brackets_stack.pop()

            if not are_matching(opened, next):
                index = i
                break
            #Process closing bracket, write your code here
    if opening_brackets_stack:
        index = i
    if not index == -1:
        return str(index)
    else:
        return "Success"




def main():
    while "iop":
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)




    # Printing answer, write your code here


if __name__ == "__main__":
    main()
