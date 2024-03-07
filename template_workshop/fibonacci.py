class Fibonacci:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        ##### YOUR CODE HERE #####
        # Check if n is 0
        if n == 0:
            return 0
        # Check if n is 1,2
        elif n == 1 or n == 2:
            return 1
        else:
            fibSeq = [0, 1]  # Starting points of the Fibonacci sequence
            for i in range(2, n + 1):
                fibSeq.append(fibSeq[i - 1] + fibSeq[i - 2])
            return fibSeq[n]
        ##########################