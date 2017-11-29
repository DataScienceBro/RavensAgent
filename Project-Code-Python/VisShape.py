import math

class VisShape:

    def spanArea(self, arr, r, c):
        if arr[r,c] == 0:
            # self.centroid
            self.top = min(r, self.top)
            self.bottom = max(r, self.bottom)
            self.left = min(c, self.left)
            self.right = max(c, self.right)
            arr[r,c] = 1
            return 1 + sum([self.spanArea(arr, r + dr, c + dc) for dr, dc in ((-1,-1), (-1, 0), (-1, 1), (1,-1), (1,0), (1,1))])
            # continue dfs
        else:
            return 0



    def __init__(self, r, c, arr):
        self.top = r
        self.bottom = r
        self.left = c
        self.right = c


        self.area = self.spanArea(r, c, arr)
        self.rectangularity = self.area / ((self.bottom - self.top) * (self.right - self.left))

    # def rectangularity(self):
    #     return self.area / ((self.bottom - self.top) * (self.right - self.left))
