# PI-Maze Solver 

Code for finding the shortest path from the centre to the exit of a square maze.

The python-cv2 code gives the solved location coordinates as the output which is sent via hotspot to a bot that uses these coordinates to solve the maze in realtime.

The bot is equipped with a camera and is programmed to follow a laser light that is shown along the path of the solved points. The laser part is done using a 3-DOF arm. Depending on the x and y corrdinates , it is programmed to move and light up the particular coordinate in real time. The bot thus follows the laser to solve the maz.
