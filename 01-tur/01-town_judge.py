import numpy as np
from typing import List

class Solution:
    def find_judge(self, n: int, trust: List[List[int]]) -> int:
        cand0, cand1, cand2, memb0 = [], [], [], []
        key1, key2 = False, False
        for i in range(n):
            cand0.append(trust[i][0])
            cand0.append(trust[i][1])
            cand1.append(trust[i][0])
            cand2.append(trust[i][1])
        npc1 = np.array(cand1)
        npc2 = np.array(cand2)
        memb0 = list(set(cand0))
        m = len(memb0)
        for i in range(m):
            if (np.count_nonzero(npc2 == memb0[i]) == m-1):
                key2 = True
            if (np.count_nonzero(npc1 == memb0[i]) == 0):
                key1 = True
            if key1 and key2 == True:
                return memb0[i]
        return -1

    if __name__ == '__main__':
        arr1 = [[2, 1], [3, 1], [1, 3]]
        arr2 = [[2, 1], [3, 1]]
        print(find_judge(None, len(arr1), arr1))
        print(find_judge(None, len(arr2), arr2))