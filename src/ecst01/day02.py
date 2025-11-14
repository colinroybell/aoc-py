from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_st01_02(DayBase):
    YEAR = "st01"
    DAY = "02"
    PREFIX = "ec"

class BinTreeNode:
    def __init__(self, id, val, letter):
        self.id = id
        self.val = val
        self.letter = letter
        self.children = [None, None]
        self.parent = None
        self.level = None

    def swapValues(self,other):
        self.val, other.val = other.val, self.val
        self.letter, other.letter = other.letter, self.letter    

class BinTree:
    def __init__(self):
        self.root = BinTreeNode(None,0,"")
        self.counts = [1]

    def add(self,id,val,letter):
        newNode = BinTreeNode(id, val, letter)
        if not self.root:
            self.root = newNode
            newNode.level = 0
            self.counts.append(1)
        else:
            node = self.root
            level = 0
            while 1:
                if val < node.val:
                    dir = 0
                else:
                    dir = 1
                print(val, node.val, dir)
                if node.children[dir]:
                    node = node.children[dir]
                    level += 1
                else:
                    node.children[dir] = newNode
                    newNode.level = level
                    newNode.parent = node
                    if len(self.counts) > level:
                        self.counts[level] += 1
                    else:
                        self.counts.append(1)
                    break

    def maxLevelStringRecurse(self,node,level):
        if node == None:
            return ""
        if node.level == level:
            return node.letter
        else:
            return self.maxLevelStringRecurse(node.children[0],level) + self.maxLevelStringRecurse(node.children[1],level) 


    def maxLevelString(self):
        max_level = 0
        max_count = 0

        for level, count in enumerate(self.counts):
            if count > max_count:
                max_count = count
                max_level = level         
        return self.maxLevelStringRecurse(self.root, max_level)    
    

    def findNode(self,id, node = None):
        if node == None:
            node = self.root  
        if node.id == id:
            return [node]
        idNodes = []
        if node.children[0]:
            idNodes.extend(self.findNode(id, node.children[0]))
            
        if node.children[1]:
            idNodes.extend(self.findNode(id, node.children[1]))
        return idNodes              

    def redo_counts_and_levels(self, level = None, node = None):
        if node == None:
            level = 0
            self.counts = []
            node = self.root
        node.level = level    
        if len(self.counts) > level:
            self.counts[level] += 1
        else:
            self.counts.append(1)
        for i in range(2):
            if node.children[i]:
                self.redo_counts_and_levels(level + 1, node.children[i])            





def part_1(input, part = 1):
    val_letter_re = re.compile(r'\[(\d+),(.)\]')
    trees = [BinTree() for _ in range(2)]
    for line in input_generator(input):
        print(line)
        fields = line.split(' ')
        if fields[0] == 'ADD':
            id = int(fields[1].split('=')[1])
            for i in range(2):
                m = val_letter_re.search(fields[i+2])
                assert m
                trees[i].add(id, int(m.group(1)),m.group(2))
        elif fields[0] == 'SWAP':
            id = int(fields[1])
            idnode = []
            for i in range(2):
                idnode.extend(trees[i].findNode(id))
            if part == 2:    
                idnode[0].swapValues(idnode[1])
            else:
                idparent = [idnode[0].parent, idnode[1].parent]
                for i in range(2):
                    this = i
                    other = 1-i
                    idnode[this].parent = idparent[other]
              
                    if idparent[this].children[0] == idnode[this]:
                        idparent[this].children[0] = idnode[other]
                    else:
                        idparent[this].children[1] = idnode[other]



        else:
            assert 0, 'bad command {}'.format(fields[0])    
    if part == 3:
        for i in range(2):
            trees[i].redo_counts_and_levels()
    return trees[0].maxLevelString()+trees[1].maxLevelString()           
       


def part_2(input):
   # Part 2 same as part 1
   return part_1(input, part = 2)


def part_3(input):
    return part_1(input, part = 3)


if __name__ == "__main__":
    Run_st01_02().run_cmdline()
