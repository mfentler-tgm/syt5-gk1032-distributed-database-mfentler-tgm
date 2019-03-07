from horizontalSearch import connect as hconnect
from verticalSearch import connect as vconnect
from combinedSearch import connect as cconnect

if __name__=='__main__':
    print('Horizontal Schema ...')
    hconnect()
    print('Vertical Schema ...')
    vconnect()
    print('Combined Schema ...')
    cconnect()