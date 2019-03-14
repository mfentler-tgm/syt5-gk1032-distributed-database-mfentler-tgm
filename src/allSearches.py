from horizontalSearch import connect as hconnect
from verticalSearch import connect as vconnect
from combinedSearch import connect as cconnect

from horizontalSearch import ek as hek
from verticalSearch import ek as vek
from combinedSearch import ek as cek

if __name__=='__main__':
    print('Horizontal Schema ...')
    hconnect()
    print('Vertical Schema ...')
    vconnect()
    print('Combined Schema ...')
    cconnect()
    print('....!! Now comes the EK !!....')
    hek()
    vek()
    cek()