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
                if listToChop[halfPart - 1] == number:
                    return (halfPart - 1)
        return -1

    def __init__(self):
        '''
        Constructor
        '''
        