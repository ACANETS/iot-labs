import Adafruit_MCP9808.MCP9808 as mcp
import argparse
from time import sleep
from sys import exit

parser = argparse.ArgumentParser(description='Outputs the ambient temperature.')
parser.add_argument('unit', metavar='unit', type=str, nargs=1, help='the temperature unit to be used (celcius, fahrenheit, kelvin)')
args = parser.parse_args()

unit = args.unit[0]

sensor = mcp.MCP9808()
sensor.begin()

print('Displaying temperature in the requested unit. Use Ctrl-C to stop.')

#Main loop for displaying the temperature.
#The function call is a high-level function call to the i2c bus on the pi. It reads from the default address of the temperature sensor (0x18) at device register (0x05). That device register holds the ambient temperature.

while True:
    temp = sensor.readTempC()
    if(unit == 'F' or unit == 'fahrenheit'):
        temp = temp * (9.0/5.0) + 32.0
    elif(unit == 'K' or unit == 'kelvin'):
        temp += 273
    elif(unit != 'C' and unit != 'celcius'): 
        print('Invalid argument')
        exit()

    print 'current temp: {0:3.3f}'.format(temp)
    sleep(2)
