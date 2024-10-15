import RPi.GPIO as GPIO
import time

# Set the pin numbering mode
GPIO.setmode(GPIO.BOARD)

# Set up the GPIO pin (pin 11 in this case) as an output
GPIO.setup(0, GPIO.OUT)

try:
    while True:
        GPIO.output(0, GPIO.HIGH)  # Turn on the LED
        time.sleep(1)               # Wait for 1 second
        GPIO.output(0, GPIO.LOW)   # Turn off the LED
        time.sleep(1)               # Wait for 1 second
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on CTRL+C exit
