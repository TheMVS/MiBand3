# MiBand3
Library to work with Xiaomi MiBand 3

Base lib provided by Leo Soares
Additional debug & fixes was made by Volodymyr Shymanskyy

# Run

### Install dependencies

`pip install -r requirements.txt`

Turn on your Bluetooth

Unpair you MiBand2 from current mobile apps

Find out your MiBand3 MAC address

```sudo hcitool lescan```

Run this to auth device

```python main.py MAC_ADDRESS --init```

If you having problems(BLE can glitch sometimes)

```sudo hciconfig hci0 reset```
