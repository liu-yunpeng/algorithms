class GrayCode:
    def __init__(self):
        self.candidates = []
        self.result = []

    def check_binary(self, a, b):
        # a = '{0:08b}'.format(a)
        # b = '{0:08b}'.format(b)

        return self.isPowerOfTwo(a ^ b)

    def isPowerOfTwo(self, x ):
 
        # First x in the below expression is
        # for the case when x is 0
        return x and (not(x & (x - 1)))
 


    def grayCode(self, n):

        for i in range(n):
            self.candidates.append(i)

        def backtrack():
            if len(self.result) == n:
                return self.result

            for c in self.candidates:
                if self.result:
                    cond = self.check_binary(c, self.result[-1])
                else:
                    cond = True
                if cond:
                    self.candidates.remove(c)
                    self.result.append(c)
                    backtrack()
                    if len(self.result) == n:
                        return self.result
                    else:
                        self.result.pop()
                        self.candidates.append(c)

            

        backtrack()
        return self.result


s = GrayCode()
n = 7
res = s.grayCode(n)
print(res)
print(['{0:04b}'.format(i) for i in res])