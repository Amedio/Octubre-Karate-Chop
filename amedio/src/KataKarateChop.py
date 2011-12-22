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
            if listToChop[0] == number:
                return 0
        return -1

    def __init__(self):
        '''
        Constructor
        '''
        