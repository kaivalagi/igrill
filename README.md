# iGrill-to-Azure-IoT
Push iGrill2 data to Azure IoT Hub

### Requires
* [bluepy](https://github.com/IanHarvey/bluepy)
& [pycrypto]()
* requests - pip install requests

## Usage
### iGrill
1. Enable Bluetooth - sudo hciconfig hci0 up
2. Start the iGrill app and connect it to your iGrill2. 
3. Set an alarm for any of the connected probes.
4. Disconnect the iGrill app and run app.py