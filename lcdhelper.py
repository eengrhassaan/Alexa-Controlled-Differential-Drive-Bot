# Importing Required Libraries
# PI driver Library for I2C communication of LCD
import drivers 
from time import sleep

# Main Lcd Class Helper
class LcdHelper:

    # Constructor To initialize LCD and its config parameters
    def __init__(self):
        self.display = drivers.Lcd()
        self.display.lcd_display_string("Alexa AI Bot", 1)
        return
    
    # Function to Write to 2nd Line of LCD
    def writeToLcd(self, text):
        self.display.lcd_display_string(text,2)

    # Function to clear Lcd
    def clearLcd(self):
        self.display.lcd_clear()
        self.display.lcd_display_string("Alexa AI Bot", 1)
        self.display.lcd_display_string("",2)
