# iGrill-to-Azure-IoT
Push iGrill2 data to Azure IoT Hubs

### Requires
* [bluepy](https://github.com/IanHarvey/bluepy)
* [pycrypto](https://github.com/dlitz/pycrypto)
* requests - pip install requests

### Usage
1. Enable Bluetooth - sudo hciconfig hci0 up
2. Configure variables in app.py (ADDRESS, CONNECTION_STRING, DEVICE_ID)
3. Run app.py
