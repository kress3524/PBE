import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

# Configurar I2C en la Raspberry Pi
i2c = busio.I2C(board.SCL, board.SDA)

# Inicializar el módulo PN532
pn532 = PN532_I2C(i2c, debug=False)

# Obtener el firmware para comprobar comunicación
ic, ver, rev, support = pn532.firmware_version
print(f"PN532 encontrado: chip {ic:#x}, versión {ver}.{rev}")

# Configurar el PN532 para leer tarjetas NFC
pn532.SAM_configuration()

print("Acerque una tarjeta NFC...")
while True:
    uid = pn532.read_passive_target(timeout=1.0)
    if uid:
        print(f"Tarjeta detectada. UID: {uid.hex().upper()}")
        break
