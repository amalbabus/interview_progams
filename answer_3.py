# a graph data structure can be used to solve this problem
# compare two files, if they matched make parent node with childern as the two files
# compare new retried files with parent nodes , if the match make that file as it child
# else make it as new node (as parent node)
# store parent node as an element in the list along with the children (which is all the duplucate files) 
# then display the list
import filecmp

import glob
allfile =(glob.glob("/home/ubuntu/Desktop/new/*"))

for i in range(0,99):
    for j in range(0,99):
        if( filecmp.cmp(allfile[i], allfile[j]) ):
            outputlist.append(allfile[i])
            outputlist.append(allfile[j])

    
