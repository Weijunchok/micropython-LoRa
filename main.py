
from config_sample import *
from machine import SPI
from lora_send_rece import *
from sx127x import SX127x


device_spi = SPI(SPI.SPI_SOFT,mode=SPI.MODE_MASTER,baudrate = 10000000,
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = device_config['sck'],
        mosi = device_config['mosi'],
        miso = device_config['miso'],
        cs0=device_config['ss'])
lora = SX127x(device_spi, pins=device_config, parameters=lora_parameters)
#print(device_config['sck'])
print(device_spi)
lora_send(lora)
#lora_rece(lora)
