import sys
sys.path.append('../')
#############################################################################
#############################################################################

from examples.template.strategies import traders_v1
from time import sleep



""" -----------------------------------------------------------------------------------------------
    -----------------------------------------------------------------------------------------------
    SCRIPT SETUP
    ----------------------------------------------------------------------------------------------
    ----------------------------------------------------------------------------------------------
"""
_symbols_list=[('EURUSD', 0.01), ('USDCAD', 0.01)]


# creates object with a predefined configuration
print('\nrrunning process for {}'.format(str(_symbols)))
func1 = traders_v1.traders(_symbols=_symbols_list)
func1.run()

# Waits example termination
print('Waiting example termination...')
sleep(10)
example._stop_()


