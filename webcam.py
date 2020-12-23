#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[4]:


import cv2

imgcapture = cv2.VideoCapture(0)
result = True

while(result):
    ret,frame = imgcapture.read()
    cv2.imwrite("test.jpg",frame)
    result = False
    print("image captured")
    
imgcapture.release()


# In[ ]:




