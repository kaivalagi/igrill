import json
import time
from igrill import IGrillV2Peripheral
from azureiot import azureiot

ADDRESS = '<MacAddressOfiGrill2>'
CONNECTION_STRING = 'HostName=<IoTHubHostName>.azure-devices.net;SharedAccessKey=<SAK>'
DEVICE_ID = '<IoTHubDeviceName>'
INTERVAL = 5
MESSAGE_FORMAT = '{"Battery":%s,"Probe1":%s,"Probe2":%s,"Probe3":%s,"Probe4":%s}'

DEBUG = True

iotclient = azureiot(CONNECTION_STRING)

if __name__ == '__main__':

    periph = IGrillV2Peripheral(ADDRESS)

    while True:

        temps = periph.read_temperature()
        battery = periph.read_battery()
        message = MESSAGE_FORMAT % (battery, temps[1], temps[2], temps[3], temps[4])

        iotclient.sendMessage(DEVICE_ID, message )

        if DEBUG:
            print message

        time.sleep(INTERVAL)

