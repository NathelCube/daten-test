serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    Daten = serial.readLine()
    radio.sendString(Daten)
})
let Daten = ""
let Spieler = 0
radio.setGroup(1)
serial.redirect(
SerialPin.P14,
SerialPin.P0,
BaudRate.BaudRate115200
)
basic.forever(function () {
	
})
