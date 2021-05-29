from selenium import webdriver
from time import sleep
from tkinter import *
import sys
import os
import cv2
import cv
import stat
import IPython
import pyperclip
from PIL import Image, ImageTk

from pynput.keyboard import Key, Controller
keyboard = Controller()
x=" "




def bot():
    mobile=entry.get()
    def get_text():
        driver.set_window_position(0,-2000)  #window size adjust 
        
        
        #driver.find_element_by_xpath('//span[@title= "{}"]'.format('mobile no.')).click()                      #add your mobile no. here  
        
        
        driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(mobile) 
        sleep(1)
        #driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div/div[2]').click()
        driver.find_element_by_class_name('_3j7s9').click()   #select the searched mobile no. ps class name needs to be updated after few weeks
        sleep(1)
        
        flag=0
        
        

        
        
        def txtfunc(t):
            
            
            def dele(z1):#delete a file in the get folder
                w="D:\\python\\Whatsapp Bot\\get\\"+str(z1)
                os.chmod(w, 0o777)
                os.remove(w)
                print("deleted!")
                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys('Deleted! here are updated files--')
                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
                show()
                
            def photo():#capture a photo using pc's webcam
                video_capture = cv2.VideoCapture(0)
                # Check success
                if not video_capture.isOpened():
                    raise Exception("Could not open video device")
                # Read picture. ret === True on success
                ret, frame = video_capture.read()
                cv2.imwrite('D:\python\image frm whatsapp bot\opencv'+str(count)+'.png', frame)
                a='D:\python\image frm whatsapp bot\opencv'+str(count)+'.png'
                # Close device
                video_capture.release()
                driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div').click()
                driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input').send_keys(a)
                sleep(5)
                driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]').send_keys("here is your photo")
                
                driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div').click()
            def shutdown():#shutdown pc remotely
                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys('Shutting Down')
                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()

                #os.system("shutdown /s /t 1");
            """def navigate():
                global path
                
                
                def navfurther(t,path):
                    time1=driver.find_element_by_class_name('_3Bxar').text
                    txt1=driver.find_element_by_class_name('_1AwDx').text
                    if(txt1!=t):
                        
                        t=txt1
                        
                        print(txt1)
                        print(time1)
                        path=path+"\\"+str(txt1)
                        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(path)
                        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
                        navfurther("t",path)

                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys('keep entering name of file ypu want to open \n c drive or d drive? ')
                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
                navfurther("c drive or d drive?","")"""
            def show():#view all files in get folder
                a=os.listdir("D:\\python\\Whatsapp Bot\\get")
                print (a)
                #driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("Here are all the files i your get folder")
                #driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
                for i in a:
                    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(i)
                    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
            def get(filename):#sends files to whatsapp
                file="D:\\python\\Whatsapp Bot\\get\\"+str(filename)
                driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div').click()
                driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button/input').send_keys(file)#can be used to send text as well as files in whatsapp
                sleep(5)
                driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div').click()









            def helloseq():
                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys('Hey there user! \n What would you like to do today?\n select from the list below \n 1) To view your files in get folder send Show \n 2)  To get a file from your Get folder send Get space name of your file \n 3) To Delete a file from your get folder send Delete space name of file you want to delete  \n 4) To take a picture using webcam of the laptop send Photo\n 5) To close the program send Exit \n 6) To shutdown the laptop send Shutdown \n')
                
            def close():
                sys.exit()







                

            count=0
            while(flag==0):
                
                                                
                
                time=driver.find_element_by_class_name('_3Bxar').text            #these may need to be updated
                txt=driver.find_element_by_class_name('_1AwDx').text#add
                if(txt!=t):#add
                #if(time!=t):
                    #txt=driver.find_element_by_class_name('_1AwDx').text
                    #t=time
                    t=txt
                    
                    print(txt)
                    print(time)
                    
                    if(str(txt).split(' ')[0]=="Delete" and count>0):
                        try:
                            z1=str(txt).split(' ')[1:][0]
                            dele(z1)
                        except:
                            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("can't delete this item maybe it doesnt exist or you dont have permission to delete it")
                            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
                            
                            
                        get_text()
                    elif(txt=="Photo"and count>0):
                        try:
                            photo()
                        except:
                            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("can't get photo right now maybe the web cam is off")
                            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
                        get_text()

                    elif(txt=="Shutdown" and count>0):
                        shutdown()
                    elif(txt=="Show" or txt=="show" and count>0):
                        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("Here are all the files i your get folder")
                        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
                        
                        show()
                        get_text()
                    elif(txt=="Hi" or txt=="Hello" or txt=="yo" or txt=="Hey" and count>0):
                        helloseq()
                        get_text()
                    elif(str(txt).split(' ')[0]=="get" or str(txt).split(' ')[0]=="Get" and count>0):
                        try:
                            print (str(txt).split(' ')[0])
                            filename=str(txt).split(' ')[1:][0]
                            get(filename)
                        except:
                            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("couldnt find the item. or maybe file size is too large. Remember the program is case sensitive")
                            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
                        sleep(2)
                        get_text()

                        

                    elif(txt=="Exit" and count>0):
                        close()
                    
                    
                        
                count=count+1
                
                
            
        flag=0
        txtfunc("4")
            
                
        
    l.destroy()
    bt.destroy()
    entry.destroy()
    def exit():
        root.destroy()
        
        
   
    l1=Label(root,text='press continue after scanning QR code',width='50')
    l1.grid(row=0,column=0)
    bt1=Button(root,text='CONTINUE',command=lambda: [exit(),get_text()])
    bt1.grid(row=2,column=0,columnspan=3)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu");
    driver = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_options)
    root.lift()
    driver.get('https://web.whatsapp.com/')
    sleep(2)
    
    
    
     
root=Tk()

root.minsize(200,100)

l=Label(root,text='welcome to python bot enter your mob. no.',width='50')
entry=Entry(root,width=50,borderwidth=5)#try
l.grid(row=0,column=0)
bt=Button(root,text='START',command=lambda: [bot()]) 
entry.grid(row=1,column=0,columnspan=5)#try
bt.grid(row=2,column=0,columnspan=3)


root.mainloop()





        
        
