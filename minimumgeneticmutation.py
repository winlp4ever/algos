'''Problem:

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
 

Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
 

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
 

Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
'''

import collections
from typing import List
class Solution:
    '''
    idea: bfs
    complexity: O(e) where e is nb of edges (pair of adjacent genes - genes differ from each other
    exactly at 1 index) in time and O(n) in space (n = nb of genes in bank)
    '''
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # We can remove this, but kept it for avoiding the duplicates.
        bank = set(bank)
        # This can be a simple list, doesn't matter
        valid_choices_list = "ACGT"

        queue = collections.deque([start])
        # visited item can be removed from the bank, but that's not preferable.
        visited = set()
        mutation_count = -1

        while(queue):
            size = len(queue)
            mutation_count += 1

            for i in range(size):
                cur_mutation = queue.popleft()
                visited.add(cur_mutation)
                if cur_mutation == end:
                    return mutation_count
                for j in range(len(cur_mutation)):
                    for c in valid_choices_list:
                        next_mutation = cur_mutation[:j] + c + cur_mutation[j+1:]
                        if next_mutation in bank:
                            if next_mutation not in visited:
                                visited.add(next_mutation)
                                queue.append(next_mutation)                                

        return -1