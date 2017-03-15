# External module imports
import RPi.GPIO as GPIO
import time
import signal

## Pin definitons in Broadcom pin numbering
# YELLOW_PIN = 22
# BLUE_PIN = 27
# RED_PIN = 4
# GREEN_PIN = 17
# BEEPER_PIN = 23
# GPIO.setmode(GPIO.BCM) # Broadcom pin numbering scheme

## Pin definitions in Raspberry Pi pin numbering
YELLOW_PIN = 15
BLUE_PIN = 13
RED_PIN = 7
GREEN_PIN = 11
BEEPER_PIN = 16
BUTTONS = {7: "RED", 11: "GREEN", 13: "BLUE", 15: "YELLOW"}
GPIO.setmode(GPIO.BOARD) # Raspberry Pi pin numbering scheme

## Set up GPIO
GPIO.setup(BEEPER_PIN, GPIO.OUT) # beeper pin set as output
GPIO.setup(YELLOW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(BLUE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(RED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(GREEN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Functions
def beep(pin, interval):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(pin, GPIO.LOW)

def button_press(pin):
    """Called when a GPIO button is pressed down
    """
    if pin in BUTTONS:
        print("YEAH {}".format(BUTTONS[pin]))
        if pin == GREEN_PIN:
            beep(BEEPER_PIN, 0.05)
    else:
        print("What button on pin {}?".format(pin))

## Enable GPIO interrupts
## http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-2
GPIO.add_event_detect(GREEN_PIN, GPIO.FALLING, callback=button_press, bouncetime=100)
GPIO.add_event_detect(RED_PIN, GPIO.FALLING, callback=button_press, bouncetime=100)
GPIO.add_event_detect(YELLOW_PIN, GPIO.FALLING, callback=button_press, bouncetime=100)
GPIO.add_event_detect(BLUE_PIN, GPIO.FALLING, callback=button_press, bouncetime=100)

class GracefulKiller:
    """Catch kill signals to shut down properly
    """
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self,signum, frame):
        self.kill_now = True

if __name__ == "__main__":
    print("Here we go!")
    try:
        killer = GracefulKiller()
        while True:
            time.sleep(0.2)
            if killer.kill_now:
                break
    finally: # when killed, exit cleanly
        GPIO.cleanup() # cleanup all GPIO
        print("Shutdown received")
