import time
#from uPySensors.ssd1306_i2c import Display

def lora_send(lora):
    counter = 0
    print("LoRa Sender")
    #display = Display()

    while 1:
        payload = 'Hello ({0})'.format(counter)
        print("LoRa Sender1")
        #display.show_text_wrap("{0} RSSI: {1}".format(payload, lora.packet_rssi()))
        lora.println(payload)
        print("Sending packet: {0}\n RSSI: {1}\n".format(payload, lora.packet_rssi()))
        counter += 1
        time.sleep(5)

def lora_rece(lora):
    print("LoRa Receiver")
    #display = Display() #到时候可以用LCD显示
    #lora.blink_led()
    while True:
        if lora.received_packet():
            #lora.blink_led()
            print('something here')
            payload = lora.read_payload()
            print(payload)
