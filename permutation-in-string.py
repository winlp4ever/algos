'''problem:

'''

class Solution:
    '''complexity:
        window technique
        O(n) time and space
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        if len(s2) < len(s1):
            return False
        trg = dict()
        for c in s1:
            if c not in trg:
                trg[c] = 0
            trg[c] += 1
            
        l = len(s1)
        same = 0
        win = dict()
        
        # init window
        for c in trg:
            win[c] = 0
        for c in s2[:l]:
            if c in trg:
                win[c] += 1
                
        for c in win:
            if trg[c] == win[c]:
                same += 1
                

        if same == len(trg):
            return True
        
        n = len(s2)
        for i in range(n-l):
            if s2[i] in win:
                if win[s2[i]] == trg[s2[i]]:
                    same -= 1
                win[s2[i]] -= 1
                if win[s2[i]] == trg[s2[i]]:
                    same += 1
            if s2[i+l] in win:
                if win[s2[i+l]] == trg[s2[i+l]]:
                    same -= 1
                win[s2[i+l]] += 1
                if win[s2[i+l]] == trg[s2[i+l]]:
                    same += 1
                    if same == len(trg):
                        return True
        return False