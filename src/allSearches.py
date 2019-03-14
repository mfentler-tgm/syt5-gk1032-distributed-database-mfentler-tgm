from horizontalSearch import connect as hconnect
from horizontalSearch import ek as ekH
from verticalSearch import connect as vconnect
from verticalSearch import ek as ekV
from combinedSearch import connect as cconnect
from combinedSearch import ek as ekC

if __name__=='__main__':
    print('Horizontal Schema ...')
    hconnect()
    print('Horizontal Schema Counts ...')
    ekH()
    print('Vertical Schema ...')
    vconnect()
    print('Vertical Schema Counts ...')
    ekV()
    print('Combined Schema ...')
    cconnect()
    print('Combined Schema Counts ...')
    ekC()