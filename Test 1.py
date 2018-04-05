import logging
import time

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/250K'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI) as scf:
        # We take off when the commander is created
        with MotionCommander(scf) as mc:

            ########## Test 1.1 ##########
##            mc.up(.8)
##            time.sleep(1)
##            mc.forward(2, velocity=.2)
##            time.sleep(1)
            ##############################

            ########## Test 1.2 ##########
##            mc.up(.8)
##            time.sleep(1)
##            mc.circle_right(.5, velocity=.2, angle_degrees=180)
##            time.sleep(1)
##            mc.circle_left(.5, velocity=.2, angle_degrees=180)
##            time.sleep(1)
            ##############################

            ########## Test 1.3 ##########
##            mc.up(.3)
##            time.sleep(.5)
##            mc.forward(.3, velocity=.2)
##            time.sleep(.5)
##            mc.turn_right(90, rate=90)
##            time.sleep(.5)
##            mc.forward(.4,velocity=.2)
##            time.sleep(.5)
##            mc.turn_left(90, rate=90)
##            time.sleep(.5)
##            mc.forward(.4, velocity=.2)
##            time.sleep(.5)
##            mc.turn_left(90, rate=90)
##            time.sleep(.5)
##            mc.forward(.4, velocity=.2)
##            time.sleep(.5)
##            mc.turn_right(90, rate=90)
##            time.sleep(.5)
##            mc.forward(1.3, velocity=.2)
##            time.sleep(.5)
            ##############################

            ########## Test 1.4 ##########
##            mc.up(.8)
##            time.sleep(1)
##            mc.forward(2/3, velocity=.2)
##            mc.forward(2/3, velocity=.4)
##            mc.forward(2/3, velocity=.2)
            ##############################

            ########## Test 1.5 ##########
##            mc.up(.3)
##            time.sleep(1)
##            mc.forward(1,velocity=.2)
##            time.sleep(1)
##            mc.up(.5)
##            time.sleep(1)
##            mc.forward(1,velocity=.2)
##            time.sleep(1)
            ##############################

            ########## Test 1.6 ##########
##            mc.up(.3)
##            time.sleep(.5)
##            mc.forward(.3, velocity=.2)
##            time.sleep(.5)
##            mc.turn_right(90, rate=90)
##            time.sleep(.5)
##            mc.forward(.4,velocity=.2)
##            time.sleep(.5)
##            mc.up(.25)
##            time.sleep(.5)
##            mc.turn_left(90, rate=90)
##            time.sleep(.5)
##            mc.forward(.4, velocity=.2)
##            time.sleep(.5)
##            mc.up(.25)
##            time.sleep(.5)
##            mc.turn_left(90, rate=90)
##            time.sleep(.5)
##            mc.forward(.4, velocity=.2)
##            time.sleep(.5)
##            mc.down(.25)
##            time.sleep(.5)
##            mc.turn_right(90, rate=90)
##            time.sleep(.5)
##            mc.forward(1.3, velocity=.2)
##            time.sleep(.5)
            ##############################
