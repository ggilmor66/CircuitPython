import board
from analogio import AnalogOut

analog_out = AnalogOut(board.A0)

while True:
    # Count up from 0 to 65535, with 64 increment
    # which ends up corresponding to the DAC's 10-bit range
    for i in range(33000, 65000, 1):
        analog_out.value = i
    for i in range(65000,33000 , -1):
        analog_out.value = i