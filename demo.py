import cv2
import streamlit as st
import numpy as np
from PIL import Image
image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
option=st.sidebar.selectbox('Select one',(None,'Flip1','Flip2','Flip3'))
option1=st.sidebar.selectbox('Select one',(None,'opt1','opt2','opt3','opt4','opt5','opt6','opt7'))
opt=st.sidebar.slider("Enhance",0.0,10.0,0.1)
opt1=st.sidebar.slider("Brightness",min_value=-50, max_value=50, value=0)
opt2=st.sidebar.slider("Blur",0.5,3.5)
if image_file is not None:
    col1,col2=st.columns(2)
    with col1:
         original_image = Image.open(image_file)
         original_image = np.array(original_image)
         st.image(original_image)
         img2=original_image.copy()
    with col2:
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
        if opt:
            img2=cv2.detailEnhance(img2,sigma_s=opt)  
        if opt1:
            img2 = cv2.convertScaleAbs(img2, beta=opt1)
        if opt2:
           img2= cv2.GaussianBlur(img2, (11, 11),opt2)
        st.image(img2)
        btn=st.button('Download')
        if btn: 
            img3=cv2.cvtColor(img2,cv2.COLOR_RGB2BGR) 
            cv2.imwrite('Edit_img.jpeg',img3)
     
