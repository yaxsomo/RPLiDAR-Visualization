"""
ARGO LIDAR Point Map Data Visalization

Written by Yassine DEHHANI for ARGO : The Atonomous Drone
Licensed under the MIT license.

All text above must be included in any redistribution.
"""

import os
from math import cos, sin, pi, floor
import pygame
from adafruit_rplidar import RPLidar
import argparse

# Set up argparse
parser = argparse.ArgumentParser(description='LiDAR Point Map Visualization for ARGO Drone')
parser.add_argument('--port', dest='port_name', default='/dev/ttyUSB0',
                    help='Serial port where the LIDAR is connected to (Linux : /dev/ttyUSB0 | MAC : /dev/tty.usbserial-1120)')
parser.add_argument('--size', dest='display_size', default='1720x1080', type=str,
                    help='Size of the display in pixels ("Width"x"Height")')
args = parser.parse_args()

# Set up pygame and the display
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
WIDTH, HEIGHT = map(int, args.display_size.split('x'))
lcd = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)
lcd.fill((0,0,0))
pygame.display.update()

# Setup the RPLidar
lidar = RPLidar(None, args.port_name, baudrate=256000, timeout=3)


# used to scale data to fit on the screen
max_distance = 0

#pylint: disable=redefined-outer-name,global-statement
def process_data(data):
    global max_distance
    lcd.fill((0,0,0))
    for angle in range(360):
        distance = data[angle]
        if distance > 0:                  # ignore initially ungathered data points
            max_distance = max([min([5000, distance]), max_distance])
            radians = angle * pi / 180.0
            x = distance * cos(radians)
            y = distance * sin(radians)
            point = (int((x / max_distance * (WIDTH/2)) + (WIDTH/2)), int((y / max_distance * (HEIGHT/2)) + (HEIGHT/2)))
            lcd.set_at(point, pygame.Color(255, 255, 255))
    pygame.display.update()


scan_data = [0]*360

try:
    print(lidar.info)
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])] = distance
        process_data(scan_data)

except KeyboardInterrupt:
    print('Stoping...')
    lidar.stop()
    print("Scanning process stopped")
    lidar.stop_motor()
    print("Motor stopped")
    lidar.disconnect()
    print("Lidar disconnected")

    


