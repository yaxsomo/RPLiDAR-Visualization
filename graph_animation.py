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
│ARGO LiDAR Graph Distance Animation │  YASSINE DEHHANI & EMILE BAILEY   │
│           17/03/2023               │      www.github.com/yaxsomo       │
└────────────────────────────────────┴───────────────────────────────────┘

ARGO LiDAR Distance Animation and Quality Measurement

Usage example: python3 graph_animation.py --port [port_name]

Written by Yassine DEHHANI for ARGO : The Atonomous Drone
Licensed under the MIT license.

All text above must be included in any redistribution.
"""


from adafruit_rplidar import RPLidar
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import argparse

# Set up argparse
parser = argparse.ArgumentParser(description='LiDAR Measurements Recorder for ARGO Drone')
parser.add_argument('--port', dest='port_name', default='/dev/ttyUSB0',
                    help='Serial port where the LIDAR is connected to (Linux : /dev/ttyUSB0 | MAC : /dev/tty.usbserial-1120)')
args = parser.parse_args()


PORT_NAME = args.port_name
DMAX = 4000
IMIN = 0
IMAX = 50

lidar = RPLidar(None, PORT_NAME, baudrate=256000, timeout=3)
fig = plt.figure()
ax = plt.subplot(111, projection='polar')
line = ax.scatter([0, 0], [0, 0], s=5, c=[IMIN, IMAX],cmap=plt.cm.Greys_r, lw=0)

def on_close(event):
    print("Closing the lidar..")
    try:
        lidar.stop_motor()
        lidar.disconnect()
    except Exception as e:
        print("Error while stopping the lidar:", e)
    finally:
        print("Lidar stopped and disconnected.")
        plt.close()


def update_line(num, iterator, line):
    scan = next(iterator)
    offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
    line.set_offsets(offsets)
    intens = np.array([meas[0] for meas in scan])
    line.set_array(intens)
    return line,

def run():

    ax.set_rmax(DMAX)
    ax.grid(True)
    iterator = lidar.iter_scans()
    ani = animation.FuncAnimation(fig, update_line,
        fargs=(iterator, line), interval=50, cache_frame_data=False)
    plt.show()
    fig.canvas.mpl_connect('close_event', on_close)


if __name__ == '__main__':   
    run()
