import board
import busio
import displayio
import adafruit_uc8179

displayio.release_displays()

spi=busio.SPI(board.D8, board.D10)  # SCK, MOSI

display_bus=displayio.FourWire(
    spi,
    command=board.D6,      # DC
    chip_select=board.D7,  # CS
    reset=board.D9         # RST
)

display = adafruit_uc8179.UC8179(
    display_bus,
    width=800,
    height=480,
    busy_pin=board.D5
)

def get_display():
    return display