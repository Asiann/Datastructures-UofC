# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                maxHeight = 0
                for vertex in range(self.n):
                    node = self.parent[vertex]
                    height = 1
                    while not node == -1:
                        node = self.parent[node]
                        height += 1
                    if height > maxHeight:
                        maxHeight = height

                return maxHeight

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
