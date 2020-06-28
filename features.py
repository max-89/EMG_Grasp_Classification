# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:44:51 2020

@author: Amina
"""

import numpy as np
import pandas as pd
import math
import time

class features_generator:
    
    def __init__(self, freq, winsize,stride):
        self.freq = freq
        self.winsize = winsize
        self.stride = stride
        
    
    
    def rms(self,data,label):
        start_time = time.time()
        shape= data.shape
        length=shape[0]
        no_of_windows= floor(((length-self.winsize)/self.stride)) +1
        
        
        empty=np.zeros((no_of_windows,shape[1]))
        gest=np.zeros((no_of_windows))
        
        start=0
        end=0
        positions=[]
        slices=[]
        
        for column in range (0,shape[1]):
            
            for row in range (0,no_of_windows):
                
               
                start= row*self.stride
                end= start+self.winsize
                
                positions.append((start,end))
                
                
                
                current=data[start:end,column]
                slices.append(current)
                sqred=current**2
                empty[row,column]=np.sqrt( sqred.mean())
        
        gest= pd.DataFrame      
        return empty,gest
    
    def iav(self,data,label):
        shape= data.shape
        length=shape[0]
        no_of_windows= floor(((length-self.winsize)/self.stride)) +1
        
        
        empty=np.zeros((no_of_windows,shape[1]))
        gest=np.zeros((no_of_windows))
        
        start=0
        end=0
        positions=[]
        slices=[]
        
        
        for column in range (0,shape[1]):
            
            for row in range (0,no_of_windows):
                
               
                start= row*self.stride
                end= start+self.winsize
                
                
                current=data[start:end,column]
                
                empty[row,column]=np.sum( np.abs(current) )
        
        gest= pd.DataFrame      

        return empty,gest
    
    
    
    def hist(self,data,label):
        
        shape= data.shape
        rows=shape[0]
        cols=shape[1]
        bins=21
        no_of_windows= math.floor(((rows-self.winsize)/self.stride)) +1
        
        
        empty=np.zeros((no_of_windows,cols*bins-1))
        empty[:]=np.NaN
        gest=np.zeros((no_of_windows))
        
        row_start=0
        row_end=0
               
        col_start=0
        col_end=0
        
        empty=np.zeros((no_of_windows,cols * bins))
        empty[:]=np.NaN
        
        for column in range (0,cols):
            col_start=col_end
            col_end=bins+col_end-1
            for row in range (0,no_of_windows):
                
                row_start= row*self.stride
                row_end= row_start+self.winsize
                
        
                current=data[row_start:row_end,column]
        
                a,b=np.histogram(current,np.linspace(-20,20,bins))
        
                a=a.reshape((1,a.shape[0]))
                
                empty[row,col_start:col_end]=a
        
        gest=label[0]    
        return empty, gest
        
               
                
                                 
                
        gest[:]=label[0]

        return empty,gest
    

    def mav(self,data,label):
            shape= data.shape
            length=shape[0]
            no_of_windows= math.floor(((length-self.winsize)/self.stride)) +1
            
            
            empty=np.zeros((no_of_windows,shape[1]))
            gest=np.zeros((no_of_windows))
            
            start=0
            end=0
            positions=[]
            slices=[]
            
            
            for column in range (0,shape[1]):
                
                for row in range (0,no_of_windows):
                    
                   
                    start= row*self.stride
                    end= start+self.winsize
                    
                    
                    current=data[start:end,column]
                    
                    empty[row,column]=np.mean( np.abs(current) )
            
            gest[:]=label[0]       
    
            return empty,gest

    def mavs(self,data,label):
            shape= data.shape
            length=shape[0]
            no_of_windows= math.floor(((length-self.winsize)/self.stride)) +1
            
            
            empty=np.zeros((no_of_windows,shape[1]))
            gest=np.zeros((no_of_windows))
            
            start=0
            end=0
            positions=[]
            slices=[]
            
            
            for column in range (0,shape[1]):
                
                for row in range (0,no_of_windows):
                    
                   
                    start= row*self.stride
                    end= start+self.winsize
                    
                    
                    current=data[start:end,column]
                    current_succ= data[start+self.stride:end+self.stride,column]
                    
                    empty[row,column]=(np.mean( np.abs(current_succ) )- np.mean( np.abs(current) ))
            
            gest[:]=label[0]      
    
            return empty,gest



    def wl(self,data,label):
            shape= data.shape
            length=shape[0]
            no_of_windows= math.floor(((length-self.winsize)/self.stride)) +1
            
            
            empty=np.zeros((no_of_windows,shape[1]))
            gest=np.zeros((no_of_windows))
            
            start=0
            end=0
            positions=[]
            slices=[]
            
            
            for column in range (0,shape[1]):
                
                for row in range (0,no_of_windows):
                    
                   
                    start= row*self.stride
                    end= start+self.winsize
                    
                    
                    current=data[start:end,column]
                    accumelative=0
                    
                    for i in range(0,current.shape[0]-1):
                        
                        accumelative= accumelative+abs(current[i+1]-current[i])
                        
                        
                        
                    
                    
                    empty[row,column]=accumelative
                
            
            gest[:]=label[0]      
    
            return empty,gest
        
        
    
    
    
    
    
        

    


