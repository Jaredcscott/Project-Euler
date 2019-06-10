# Problem specification:
# Write a program which, given a gap of size GAP and a list of block lengths,
# prints out each combination of blocks which together exactly fill the gap

GAP   = 127
WHITE = [8, 10, 11, 20, 21, 22, 30, 32, 42, 50, 51]
BLUE  = [4, 7, 8, 11, 12, 15, 19, 23, 30, 34, 42]

# Helper functions for readability
def first(L):
    return L[0]

def rest(L):
    return L[1:]

def empty(L):
    return L == []


# Recursive solution function solution
# gap    = Size of the gap that we're trying to fill
# blocks = Which blocks are we still considering to use
# sln    = Solution so far; which blocks we're considering to be part of our solution
def solve(gap, blocks, sln):
        print("TODO")


print("The solutions to the white puzzle are:")
solve(GAP, WHITE, [])

print()

print("The solutions to the blue puzzle are:")
solve(GAP, BLUE, [])