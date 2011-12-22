'''
Created on 22/12/2011

@author: ruben
'''

class KarateChopper(object):
    '''
    classdocs
    '''

    def chop(self, number, listToChop):
        if len(listToChop) > 0:
            halfPart = len(listToChop) / 2
            if listToChop[halfPart] == number:
                return halfPart
            else:
                if listToChop[halfPart] < number:
                    leftListToChop = self.getList(listToChop, 0, halfPart)
                    return self.chop(number, leftListToChop)
                if listToChop[halfPart] > number:
                    rightListToChop = self.getList(listToChop, halfPart + 1, len(listToChop))
                    return self.chop(number, rightListToChop)
        return -1
    
    def getList(self, list, initial, finish):
        result = []
        
        for i in range(initial, finish):
            result.append(list[i])
            
        return result;

    def __init__(self):
        '''
        Constructor
        '''
        