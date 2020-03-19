import json

class SegNode:
    def __init__(self, l, r, sms):
        self.l = l 
        self.r = r 
        self.sum = sms[r+1]-sms[l]
        if l == r:
            self.left = None 
            self.right = None 
        else:
            mi = (l+r)//2
            self.left = SegNode(l, mi, sms)
            self.right = SegNode(mi+1, r, sms)

    def update(self, i, val):
        if i < self.l or i > self.r:
            return -1
        if self.l == self.r:
            tmp = self.sum
            self.sum = val
            return val - tmp
        mi = (self.l + self.r) // 2
        if i <= mi:
            diff = self.left.update(i, val)
        else:
            diff = self.right.update(i, val)
        self.sum += diff
        return diff

    def sumrange(self, i, j):
        if j < i or j < self.l or i > self.r:
            return 0
        if i == self.l and j == self.r:
            return self.sum
        mi = (self.l+self.r)//2
        return self.left.sumrange(i, min(mi, j)) + self.right.sumrange(max(i, mi+1), j)
    
    def __str__(self):
        dct = dict()
        for k, v in self.__dict__.items():
            try:
                dct[k] = json.loads(str(v))
            except:
                dct[k] = str(v)
        return json.dumps(dct, indent=4)


class NumArray(SegNode):
    def __init__(self, nums):
        sms = [0]
        for k in nums:
            sms.append(sms[-1]+k)
        super().__init__(0, len(nums)-1, sms)


if __name__ == '__main__':
    nums = [1, 3, 2, 4]
    node = NumArray(nums)
    node.update(2, 1)
    
    print(node)
    print(node.sumrange(1,2))