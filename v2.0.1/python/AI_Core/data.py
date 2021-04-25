import sys
sys.path.append('../')
#############################################################################
#############################################################################

from examples.template.strategies import rates_subscriptions_v1
from time import sleep



""" -----------------------------------------------------------------------------------------------
    -----------------------------------------------------------------------------------------------
    SCRIPT SETUP
    ----------------------------------------------------------------------------------------------
    ----------------------------------------------------------------------------------------------
"""
_symbols = [('AAPL_H1', 'AAPL', 60), ('INTC_H1', 'INTC', 60)]


# creates object with a predefined configuration
print('\nrunning process for {}'.format(str(_symbols)))
func = rates_subscriptions_v1.rates_subscriptions(_instruments=_symbols)
func.run()

# Waits example termination
print('\nWaiting example termination...\n')
while not func.isFinished():
	sleep(1)


