"""
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│  █████╗ ██████╗  ██████╗  █████╗   ██╗     ██╗██████╗  █████╗ ██████╗  │
│ ██╔══██╗██╔══██╗██╔════╝ ██╔══██╗  ██║     ██║██╔══██╗██╔══██╗██╔══██╗ │
│ ███████║██████╔╝██║  ██╗ ██║  ██║  ██║     ██║██║  ██║███████║██████╔╝ │
│ ██╔══██║██╔══██╗██║  ╚██╗██║  ██║  ██║     ██║██║  ██║██╔══██║██╔══██╗ │
│ ██║  ██║██║  ██║╚██████╔╝╚█████╔╝  ███████╗██║██████╔╝██║  ██║██║  ██║ │
│ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚════╝   ╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ │
├────────────────────────────────────┬───────────────────────────────────┤
│  ARGO LiDAR Measurements Recorder  │  YASSINE DEHHANI & EMILE BAILEY   │
│           17/03/2023               │      www.github.com/yaxsomo       │
└────────────────────────────────────┴───────────────────────────────────┘

ARGO LiDAR Measurements Recorder

Usage example: python3 record_measurments.py --port [port_name] --f [file_name.txt]

Written by Yassine DEHHANI for ARGO : The Atonomous Drone
Licensed under the MIT license.

All text above must be included in any redistribution.
"""


from adafruit_rplidar import RPLidar
import argparse



# Set up argparse
parser = argparse.ArgumentParser(description='LiDAR Measurements Recorder for ARGO Drone')
parser.add_argument('--port', dest='port_name', default='/dev/ttyUSB0',
                    help='Serial port where the LIDAR is connected to (Linux : /dev/ttyUSB0 | MAC : /dev/tty.usbserial-1120)')
parser.add_argument('--f', dest='file_name', default='measurements.txt', type=str,
                    help='Specify the file name')
args = parser.parse_args()


PORT_NAME = args.port_name


def run(path):
    '''Main function'''
    lidar = RPLidar(None, PORT_NAME, baudrate=256000, timeout=3)
    outfile = open(path, 'w')
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for measurment in lidar.iter_measurments():
            line = '\t'.join(str(v) for v in measurment)
            outfile.write(line + '\n')
    except KeyboardInterrupt:
        print('Stoping...')
        lidar.stop()
        print("Scanning process stopped")
        lidar.stop_motor()
        print("Motor stopped")
        lidar.disconnect()
        print("Lidar disconnected")

if __name__ == '__main__':
    run(args.file_name)
