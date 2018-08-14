# PI-Maze Solver 

Code for finding the shortest path from the centre to the exit of a square or pi maze.

## Maze and solved Coordinates

The python code gives the solved location coordinates as the output which is sent via hotspot to a bot that uses these coordinates to solve the maze in realtime.

<p align="center">
  <img src="images/img_07.png" width="300"/>
</p>

<p align="center">
  <img src="images/maze07.png" width="300"/>
</p>


The bot is equipped with a camera and is programmed to follow a laser light that is shown along the path of the solved points. The laser part is done using a 3-DOF arm. Depending on the x and y corrdinates , it is programmed to move and light up the particular coordinate in real time. The bot thus follows the laser to solve the maze.

## Path guider 3 DOF arm 

The arm is made using metal blocks and has 3 servo motors, out of which 2 are to control the rotation angle in x axis, rotation angle in y axis and another to rotate the laser across 360 degrees. As the servo control is only for 180 degrees, the base servo and the top servo act as a couple to achieve the 360 degree rotation for the laser beam. The arm is coded using Arduino IDE.

<p align="center">
  <img src="images/maze07.png" width="300"/>
</p>


## Laser Following Bot

The Laser Following Bot is equipped with a camera and a Pi which is coded using Python. OpenCV functions are used to detect the red colour contours for which centroid is found. Depending on the x and y coordinates of the centroid of the contour, the bot is programmed to move left or right accordingly. Thus the Bot is made to follow the laser.

## Recognition

This work secured as one of the finalists for Eyantra -2016-2017.
