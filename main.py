
def on_data_received():
    global Daten
    Daten = serial.read_line()
    radio.send_string(Daten)
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)


Daten = ""
Spieler = 0
radio.set_group(1)
serial.redirect(SerialPin.P14, SerialPin.P0, BaudRate.BAUD_RATE115200)

def on_forever():
    pass
basic.forever(on_forever)
