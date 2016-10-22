# python3
# Steady hands game
import RPi.GPIO as GPIO
import time
from Adafruit_LED_Backpack import SevenSegment


# set up and start the display.
display = SevenSegment.SevenSegment()
display.begin()


# use BCM GPIO numbering - use anything else and you are an idiot!
GPIO.setmode(GPIO.BCM)
# set up GPIO input pins
# (pull_up_down be PUD_OFF, PUD_UP or PUD_DOWN, default PUD_OFF)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO 0 & 1 have hardware pull ups fitted in the Pi so don't enable them
# 0 & 1 will be used for seven segment display. So, turn hardware pull ups on.
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print("Hi from Python :- Steady Hands game")
delay = range(0, 5000)
dum = 0
start_rest = 4
end_rest = 22
wire = 17
while True:
# wait until the wand is at the start
	print("Move the loop to the start rest")
	while GPIO.input(start_rest) != 0:
		time.sleep(0.8)
	
# now we are at the start of the bendy wire
	print("Start when you are ready")
# wait until the loop is lifted off the wire
	while GPIO.input(start_rest) == 0:
		time.sleep(0.1)
	print("Your off")
# time the run to the other rest
	penalty = 0
	display.clear()
	display.print_float(penalty, decimal_digits=0, justify_right=False)
	display.write_display()		
	run_time = time.clock()
	while GPIO.input(end_rest) != 0:
		if GPIO.input(wire) == 0:
			penalty = penalty + 1
			print("Penalties total", penalty, " points")
			display.clear()
			display.print_float(penalty, decimal_digits=0, justify_right=False)
			display.write_display()
			time.sleep(0.07)
                score = time.clock() - run_time + (penalty * 0.07)
	print("The run time was", score, "seconds with", penalty, "Penalty points")
# finished a run so start again
