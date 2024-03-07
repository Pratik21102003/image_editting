import streamlit as st
import numpy as np 
import pandas as pd
import cv2
img=st.file_uploader("Upload an image")
option=st.sidebar.selectbox('Select one',(None,'Flip1','Flip2','Flip3'))
option1=st.sidebar.selectbox('Select one',(None,'opt1','opt2','opt3','opt4','opt5','opt6','opt7'))
if img:
    col1,col2=st.columns(2)
    with col1:
        image=cv2.imread(img.name)
        img1=image.copy()
        st.image(img) 
                          
    with col2:
        img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)  # Convert to RGB format because opencv BGR leta hai or streamlit RGB
        if option==None:
            pass
        if option=='Flip1':
            img2=cv2.flip(img2,1)
        if option=='Flip2':
            img2=cv2.flip(img2,-1)
        if option=='Flip3':
            img2=cv2.flip(img2,0) 
        if option1==None:
            pass
        if option1 == 'opt1':
            img2[:, :, 0]=0
        elif option1 == 'opt2':
            img2[:, :, 1]=0
        elif option1 == 'opt3':
            img2[:, :,2]=0
        elif option1 == 'opt4':
            img2[:,:,0:2]=0
        elif option1=='opt5':
            img2[:,:,1:3]=0
        elif option1=='opt6':
            img2[:,:,0:3:2]=0
        elif option1 == 'opt7':
            img2 =cv2.cvtColor(img2,cv2.COLOR_RGB2BGR)  
        opt=st.sidebar.slider("Enhance",0.0,10.0,0.1)
        if opt:
            img2=cv2.detailEnhance(img2,sigma_s=opt)  
        st.image(img2)
        btn=st.button('Download')
        if btn: 
            img3=cv2.cvtColor(img2,cv2.COLOR_RGB2BGR) 
            cv2.imwrite('Edit_img.jpeg',img3)
     