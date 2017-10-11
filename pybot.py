# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 10:26:03 2017

@author: Nano
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, ReleaseKey, Z, Q, S, D

def process_img(original_image):
        processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        #processed_img = cv2.Canny(processed_img, 200, 300)

        #vertices = np.array([[0,500], [0, 260], [300, 200], [400, 200], [680, 260], [680, 520],], np.int32)

        #processed_img = roi(processed_img, [vertices])
        
        return processed_img

##def roi(img, vertices):
##        
##        mask = np.zeros_like(img)
##        cv2.fillPoly(mask, vertices, 255)
##        masked = cv2.bitwise_and(img, mask)
##        
##        return masked

def main():
##        for i in list(range(4))[::-1]:
##                print(i+1)
##                time.sleep(1)
                
        while(True):
                screen =  np.array(ImageGrab.grab(bbox=(0,0, 680, 520)))
                new_screen = process_img(screen)

                #pyautogui.locateOnScreen('mat.jpg')

                cv2.imshow('window', new_screen)
                #cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
                if cv2.waitKey(25) & 0xFF == ord('q'):
                        cv2.destroyAllWindows()
                        break
main()
