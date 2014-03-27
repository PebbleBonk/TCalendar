'''
Created on 23.3.2014

@author: Olli Riikonen
'''

class CorruptedSavefileError(Exception):
    '''
    classdocs
    '''


    def __init__(self, message):
        '''
        Constructor
        '''
        print(message)
        super(CorruptedSavefileError, self).__init__(message)
        
        