'''
Problem: There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

 

Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2
'''

from typing import List 

class Solution:
    '''
    Complexity: O(m*n) time and O(m) space
    Idea: Use sums arrays (a1, a2, ..., an => a1, a1+a2, ..., a1+...+a(n-1)) whose meanings are the distances from 
    every slits to the leftmost of the walls. You want the slice to be aligned with the slit that cuts through least bricks, 
    which is equivalent to that the distance fr that slit to the leftmost of the wall appears most when we traverse each line
    of the wall
    '''
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall or not wall[0]:
            return 0
        n = len(wall)
        m = max([len(l) for l in wall])
        if m == 1:
            return n
        sms = dict()
        for line in wall:
            S = 0
            for u in line[:-1]:
                S += u
                if S not in sms:
                    sms[S] = 0
                sms[S] += 1
        
        return n - max([v for _, v in sms.items()])