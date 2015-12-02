#!/usr/bin/pyhton
# -*- coding: utf-8 -*-

import sys
import os
# Reconfigure the search path for all other modules
#sys.path.append(os.getcwd() + "/pynaoqi")

# Import the AlProxy module from naoqi to connect and play with the robot
from naoqi import ALProxy
# Import sleep to wait before launching the script
from time import sleep
import wipe
import hello
import taichi

# Define the ip address and port to connect to Nao
nao_ip = "127.0.0.1"  # 127.0.0.1 to access the virtual robot
nao_port = 38826  # The default port for connecting to the real robot is 9559

# Register the text to speech, posture and motion modules that will be used in this script
motion = ALProxy("ALMotion", nao_ip, nao_port)
tts = ALProxy("ALTextToSpeech", nao_ip, nao_port)
posture = ALProxy("ALRobotPosture", nao_ip, nao_port)

# At the beginning we wait for some time (5sec here)
sleep(5)

# Wake the robot up
motion.wakeUp()

# Ask the robot to go in stand up posture. The second parameter indicates the speed (btw 0 and 1) of execution
posture.goToPosture("StandInit", 0.8)

# First difficulty say hello while moving the arm
motion_id = hello.run_animation(motion)
tts.say("Hello there")

# Wait for the hello animation to stop
motion.wait(motion_id, 0)  # The second argument is the timeout: 0 for wait indefinitely

# Ask the robot to dance for us
taichi.dance(motion)

# The robot might be tired by now
motion_id = wipe.run_animation(motion)
tts.say("This was tyring. Let's rest a little bit")

# Wait for the wipe forehead animation to finish
motion.wait(motion_id, 0)

# Ask the robot to lay down
posture.goToPosture("LyingBack", 0.5)

# Let the robot rest for some time
sleep(3)

# The robot should stand up before anything else is executed
posture.goToPosture("Stand", 0.5)

# The robot moves forward for 50cm
motion.moveTo(0.5, 0, 0)

# The robot bids you farewell
tts.say("Farewell my good sir")

# Put the robot in rest position
motion.rest()

# Print a little message saying that this is the end
print("Thank you very much for flying with airSheffield. We hope to see you soon")
