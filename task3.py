import numpy as np
import cv2

## Reads image in HSV format. Accepts filepath as input argument and returns the HSV
## equivalent of the image.
def readImageHSV(filePath):
    #############  Add your Code here   ###############
    img=cv2.imread('D:\maze00.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ###################################################
    return hsv

## Reads image in binary format. Accepts filepath as input argument and returns the binary
## equivalent of the image.
def readImageBinary(filePath):
    #############  Add your Code here   ###############
    img=cv2.imread('D:\maze00.jpg')
    ret,binaryImage = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    ###################################################
    return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.
def findNeighbours(img,row,column):
    neighbours = []
    #############  Add your Code here   ###############
    cup=0
    cri=0
    cdown=0
    cleft=0
    r=(int)(row)
    c=(int)(column)
    for i in xrange(c*20,c*20+19):
        m,n,o=img[r*20,i]    
        if((m,n,o)==(255,255,255)):
            cup+=1
        m,n,o=img[r*20+19,i]
        if((m,n,o)==(255,255,255)):
            cdown+=1
    

    for i in xrange(r*20,r*20+19):
        m,n,o=img[i,c*20]
        if((m,n,o)==(255,255,255)):
            cleft+=1
        m,n,o=img[i,c*20+19]
        
        if((m,n,o)==(255,255,255)):
            cri+=1
    #print cup,cdown,cri,cleft
    if(cup>5):
        if(0<=r-1<=9):
            neighbours.append((r-1,c))
    if(cdown>5):
        if(0<=r+1<=9):

            neighbours.append((r+1,c))
    if(cri>5):
        if(0<=c+1<=9):

            neighbours.append((r,c+1))
    if(cleft>5):
        if(0<=c-1<=9):

            neighbours.append((r,c-1))
    #print cup,cri,cdown,cleft

    ###################################################
    return neighbours

##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
##  You can change the colourCell() functions used in the previous sections to suit your requirements.

def colourCell(img,row,column,colourVal):   ## Add required arguments here.
    
    #############  Add your Code here   ###############
    r=(int)(row)
    c=(int)(column)
    t=(int)(colourVal)
##    color=np.zeros((20,20,3),np.uint8)
##    color[0:20,0:20]=(colourVal,colourVal,colourVal)
##    img[r*20:r*20+20,c*20:c*20+20]=color

    for i in xrange(r*20,r*20+20):
        for j in xrange(c*20,c*20+20):
            r,g,b=img[i,j]
            if((r,g,b)==(255,255,255)):
                img[i,j]=(t,t,t)

    ###################################################
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
def graph(img,coords):
    #print a,b
    graph=[]
    path=[]
    #for i in xrange(0,len(coords)):
      ##  a,b=coords[i]
        #graph.append({(a,b):findNeighbours(img,a,b)})
    graph={(j[0],j[1]):findNeighbours(img,j[0],j[1]) for j in coords}
    #print graph
    #path=findpath(graph,(0,0),(4,1))
    #print path
    cv2.imshow('aaa',img)
    '''for i in xrange(0,len(path)):
        d,e=path[i]
        colourCell(img,d,e,200)
    cv2.imshow('path',img)'''
    
    #return path
    
    #graph=[]
    
    #graph={(a,b):findNeighbours(img,a,b)}
    #print graph


##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
def findPath(graph, start, end, path=[]): ## You can pass your own arguments in this space.
    #############  Add your Code here   ###############
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = findpath(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    ###################################################
  

## The findMarkers() function returns a list of coloured markers in form of a python dictionaries
## For example if a blue marker is present at (3,6) and red marker is present at (1,5) then the
## dictionary is returned as :-
##          list_of_markers = { 'Blue':(3,6), 'Red':(1,5)}


def findMarkers(img):    ## You can pass your own arguments in this space.
    list_of_markers = {}
    #############  Add your Code here   ###############
    blue = cv2.inRange(img,(110,50,50),(130,255,255))
    

    
    list_of_markers={'Blue':marker(blue,j[0],j[1]) for j in coords}
    


    ###################################################
    return list_of_markers

## The findOptimumPath() function returns a python list which consists of all paths that need to be traversed
## in order to start from the bottom left corner of the maze, collect all the markers by traversing to them and
## then traverse to the top right corner of the maze.

def findOptimumPath(i,f,rup ):     ## You can pass your own arguments in this space.
    path_array = []
    #############  Add your Code here   ###############
    path_array.append((findPath(i,rup(0))))
    for i in xrange(0,len(rup)-1):
        path_array.append((findPath(rup(i),rup(i+1))))
    path_array.append((findPath(rup(len(rup)-1))),j)                      


    ###################################################
    return path_array
        
## The colourPath() function highlights the whole path that needs to be traversed in the maze image and
## returns the final image.

def colourPath( img,path):      ## You can pass your own arguments in this space. 
    #############  Add your Code here   ###############
    for i in xrange(0,len(path)):
        d,e=path[i]
        colourCell(img,d,e,200)


    ###################################################
    return img

#####################################    Add Utility Functions Here   ###################################
##                                                                                                     ##
##                   You are free to define any functions you want in this space.                      ##
##                             The functions should be properly explained.                             ##
def marker(img,row,column):
    rup=[]                            
    r=(int)(row)
    c=(int)(column)
    for i in xrange(r*20,r*20+19):
        m,n,o=img[i,c*20]
        if((m,n,o)==(0,0,0)):
            rup.append((r,c))                     
            return (r,c)
        



##                                                                                                     ##
##                                                                                                     ##
#########################################################################################################

## This is the main() function for the code, you are not allowed to change any statements in this part of
## the code. You are only allowed to change the arguments supplied in the findMarkers(), findOptimumPath()
## and colourPath() functions.

def main(filePath, flag = 0):
    img = readImageBinary('D:\maze00.jpg')
    imgHSV = readImageHSV('D:\maze00.jpg')
    coords = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),
              (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),
              (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),
              (3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),
              (4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),
              (5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),
              (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9),
              (7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),
              (8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),
              (9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9)]
                  #coords = [(0,0)]## Acquire HSV equivalent of image.
    graph(img,coords)
    listOfMarkers = findMarkers(imgHSV )              ## Acquire the list of markers with their coordinates. 
    test = str(listOfMarkers)
    imgBinary = readImageBinary('D:\maze00.jpg')          ## Acquire the binary equivalent of image.
    initial_point = ((len(imgBinary)/20)-1,0)      ## Bottom Left Corner Cell
    final_point = (0, (len(imgBinary[0])/20) - 1)  ## Top Right Corner Cell
    pathArray = findOptimumPath(initial_point, final_point,listOfMarkers ) ## Acquire the list of paths for optimum traversal.
    print pathArray
    img = colourPath(imgBinary, pathArray)         ## Highlight the whole optimum path in the maze image
    if __name__ == "__main__":                    
        return img
    else:
        if flag == 0:
            return pathArray
        elif flag == 1:
            return test + "\n"
        else:
            return img
## Modify the filepath in this section to test your solution for different maze images.           
if __name__ == "__main__":
    filePath = "D:\maze00.jpg"                        ## Insert filepath of image here
    img = main('D:\maze00.jpg',0)                 
    #cv2.imshow("canvas", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


