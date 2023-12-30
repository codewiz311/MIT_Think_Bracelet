# Import necessary libraries
from gpiozero import LED, PWMOutputDevice
import picamera, serial, time

# Define GPIO pin numbers
leds_pin = 17
gps_pin = 15
motor_pin = 21

# Initialize LEDs and Motor
leds = LED(leds_pin)
motor = PWMOutputDevice(motor_pin)

points = [] # Places where alert was activated (anomalies)
max_dis = 10 # Maximum distance from edge before alert (change this value based on specific park/trail)
vibration = 10 # Vibration amount (experimental)

# Function to capture video from four cameras
def capture_video(): 
    pass

# Function to stitch video feeds together
def video_stitch(): 
    pass

# Function to get distance to edge
def get_dis_to_edge(): 
    pass

# Function determine if too close to edge
def too_close():
    if get_dis_to_edge() < max_dis:
        return True
    return False

# Function to alert user
def alert_user():
    # The coordinates of the bracelet should be stored every time an alert is activated
    global points
    points.append(read_gps_data())

    motor.value = vibration
    for i in range(10): # Change the number based on how many times you want the LEDs to flash on and off
        leds.on()
        time.sleep(.25)
        leds.off()
        time.sleep(.25)
        if too_close() == False: # If the user is no longer too close, stop flashing the LEDs and turn the motor off
            break
    motor.value = 0

# Function to read GPS data
def read_gps_data(): 
    pass

if __name__ == "__main__": 
    while True:
        if too_close():
            alert_user()
