import cv2
import numpy
import tkinter as tk
from tkinter import filedialog
#from skimage import color
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
tst=cv2.imread(file_path)
a=tst
a=cv2.resize(a,(256,256))
b = cv2.cvtColor(a, cv2.COLOR_BGR2LAB)
#cv2.imshow('lab',b)
[r,c,p]=a.shape
gr=numpy.zeros((r,c),'double')
red=a[:,:,2]
green=a[:,:,1]
blue=a[:,:,0]
gray= 0.29*a[:,:,2] + 0.59*a[:,:,1] + 0.11*a[:,:,0]
gr=b[:,:,0]
gr1=numpy.uint8(gr)
im=numpy.reshape(gr,(1, r*c))
print(im)
k1=numpy.double(110)
k2=numpy.double(120)
k3=numpy.double(130)
dif1=numpy.zeros((1,numpy.size(im)))
dif2=numpy.zeros((1,numpy.size(im)))
dif3=numpy.zeros((1,numpy.size(im)))
l1=list()
l2=list()
l3=list()
for j in range(50):
          for i in range(numpy.size(im)):
                    dif1[0][i]=abs(im[0][i]-k1)
                    dif2[0][i]=abs(im[0][i]-k2)
                    dif3[0][i]=abs(im[0][i]-k3)
                    if((dif1[0][i]<dif2[0][i]) and (dif1[0][i]<dif3[0][i])):
                              l1.append(im[0][i])
                    elif((dif2[0][i]<dif1[0][i]) and (dif2[0][i]<dif3[0][i])):
                              l2.append(im[0][i])
                    else:
                              l3.append(im[0][i])

          k1=numpy.mean(l1)
          k2=numpy.mean(l2)
          k3=numpy.mean(l3)
          print(k1,k2,k3)
          l1=list()
          l2=list()
          l3=list()

op=numpy.zeros((r,c),'double')
for i in range(r):
          for j in range(c):
                    if(abs(gr[i][j]-k1)<= abs(gr[i][j]-k2) and abs(gr[i][j]-k1)<=abs(gr[i][j]-k3)):
                              op[i][j]=k1
                    elif(abs(gr[i][j]-k2)<= abs(gr[i][j]-k1) and abs(gr[i][j]-k2)<=abs(gr[i][j]-k3)):
                              op[i][j]=k2
                    else:
                              op[i][j]=k3


cl1re=numpy.zeros((r,c),'uint8')
cl1gr=numpy.zeros((r,c),'uint8')
cl1bl=numpy.zeros((r,c),'uint8')

cl2re=numpy.zeros((r,c),'uint8')
cl2gr=numpy.zeros((r,c),'uint8')
cl2bl=numpy.zeros((r,c),'uint8')

cl3re=numpy.zeros((r,c),'uint8')
cl3gr=numpy.zeros((r,c),'uint8')
cl3bl=numpy.zeros((r,c),'uint8')
for i in range(r):
          for j in range(c):
                    if(op[i][j]==k1):
                              cl1re[i][j]=red[i][j]
                              cl1gr[i][j]=green[i][j]
                              cl1bl[i][j]=blue[i][j]
                    elif(op[i][j]==k2):
                              cl2re[i][j]=red[i][j]
                              cl2gr[i][j]=green[i][j]
                              cl2bl[i][j]=blue[i][j]
                    else:
                              cl3re[i][j]=red[i][j]
                              cl3gr[i][j]=green[i][j]
                              cl3bl[i][j]=blue[i][j]
clust1=cv2.merge((cl1bl,cl1gr,cl1re))
clust2=cv2.merge((cl2bl,cl2gr,cl2re))
clust3=cv2.merge((cl3bl,cl3gr,cl3re))
cv2.imshow('cluster1',clust1)
cv2.imshow('cluster2',clust2)
cv2.imshow('cluster3',clust3)
cv2.waitKey(4000)
choice=int(input('enter the cluster number where disease is identified'))
if(choice==1):
          redcl=red
          greencl=green
          bluecl=blue
          
          for i in range(r):
                    for j in range(c):
                              if(op[i][j]==k1 and gray[i][j]<200):
                                        redcl[i][j]=numpy.uint8(255)
                                        greencl[i][j]=numpy.uint8(0)
                                        bluecl[i][j]=numpy.uint8(0)
          cluster1=cv2.merge((bluecl,greencl,redcl))
          cv2.imshow('disease',cluster1)
          cv2.waitKey(0)

elif(choice==2):
          redcl=red
          greencl=green
          bluecl=blue
          
          for i in range(r):
                    for j in range(c):
                              if(op[i][j]==k2 and gray[i][j]<200):
                                        redcl[i][j]=numpy.uint8(255)
                                        greencl[i][j]=numpy.uint8(0)
                                        bluecl[i][j]=numpy.uint8(0)
          cluster2=cv2.merge((bluecl,greencl,redcl))
          cv2.imshow('disease',cluster2)
          cv2.waitKey(0)
else:
          redcl=red
          greencl=green
          bluecl=blue
          
          for i in range(r):
                    for j in range(c):
                              if(op[i][j]==k3 and gray[i][j]<200):
                                        redcl[i][j]=numpy.uint8(255)
                                        greencl[i][j]=numpy.uint8(0)
                                        bluecl[i][j]=numpy.uint8(0)
          cluster3=cv2.merge((bluecl,greencl,redcl))
          cv2.imshow('disease',cluster3)
          cv2.waitKey(0)

                              
                              
                       
