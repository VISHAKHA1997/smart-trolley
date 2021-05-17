import RPi.GPIO as a
import serial
import urllib
import time

a.setmode(a.BOARD)
status = 40
swtr2=38
a.setup(status,a.IN)
a.setup(swtr2,a.IN)
              
data1 = serial.Serial(
                    port='/dev/ttyS0',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
                    #timeout=1 # must use when using data.readline()
                    #)	
print (" ")
No_of_item = 0
Total_sum = 0
p119 = False
pA29 = False
pE4C = False
p3B9 = False
pA33 = False
data="hello"
link = "http://mahavidyalay.in/AcademicDevelopment/ServerDemo/Led27.php?status=%s"
      
def data_url():
   f = urllib.urlopen(link % data)
   print(f.read())
   f.close()
   time.sleep(1)

try:     
   while 1:
      if(a.input(swtr2)==1):
         print("Trolley 1")
         while a.input(status) == False:
            data = "S"
            f = urllib.urlopen(link % data)
            f.close()
            time.sleep(1)
            print("Slide Sw to Srt")
            No_of_item = 0
            Total_sum = 0
            p119 = False
            pA29 = False
            pE4C = False
            p3B9 = False
            pA33 = False
         
         while a.input(status) == True:
            print ("Place the card")
            x=data1.read(12)#print upto 10 data at once and remaining on the second line
            print x
            if(x == "5100AACC92A5"): #Marri Gold to add send 1, to remove send 2
               if(p119 == False):
                  print("Mari Gold")
                  price=15
                  print(price)
                  No_of_item = No_of_item + 1
                  Total_sum = Total_sum + 15
                  data = "1"
                  data_url()
                  p119 = True
               elif(p119 == True):
                  print("Mari Gold")
                  No_of_item = No_of_item - 1
                  Total_sum = Total_sum - 15
                  data = "2"
                  data_url()
                  p119 = False
                     
            elif(x == "5100AAB45C13"): #school bag to add send 3, to remove send 4
               if(pA29 == False):
                  price=700
                  print(price)
                  No_of_item = No_of_item + 1
                  Total_sum = Total_sum + 700
                  data="3"
                  data_url()
                  pA29 = True
               elif(pA29 == True):
                  No_of_item = No_of_item - 1
                  Total_sum = Total_sum - 700
                  data="4"
                  data_url()
                  pA29 = False    
            elif(x == "5100AADA6544"): # sugar to add send 5, to remove send 6
               if(pE4C == False):
                  price=400
                  print(price)
                  print("Sugar- 10Kg")
                  No_of_item = No_of_item + 1
                  Total_sum = Total_sum + 400
                  data="5"
                  data_url()
                  pE4C = True
elif(pE4C == True):
                  print("Sugar- 10Kg")
                  No_of_item = No_of_item - 1
                  Total_sum = Total_sum - 400
                  data="6"
                  data_url()
                  pE4C = False    
            elif(x == "5100AA7BC343"): # fair & lovely to add send 7, to remove send 8
               if(p3B9 == False):
                  print("Fair & lovely - 200gm")
                  price=200
                  print(price)
                  No_of_item = No_of_item + 1
                  Total_sum = Total_sum + 200
                  #lcd_send_data()
                  data_url()
                  p3B9 = True
                  data="7"
                  data_url()
               elif(p3B9 == True):
                  print("Fair & lovely - 200gm")
                  No_of_item = No_of_item - 1
                  Total_sum = Total_sum - 200
                  #lcd_send_data()
                  data="8"
                  data_url()
                  p3B9 = False       
            elif(x == "5100AAD62C01"): # nirma to add send 9, to remove send A
               if(pA33 == False):
                  print("Washing Powder Nirma - 5Kg")
                  price=300
                  print(price)
                  No_of_item = No_of_item + 1
                  Total_sum = Total_sum + 300
                  data="9"
                  data_url()
                  pA33 = True
               elif(pA33 == True):
                  print("Washing Powder Nirma - 5Kg")
                  No_of_item = No_of_item - 1
                  Total_sum = Total_sum - 300
                  data="A"
                  data_url()
                  pA33 = False   
            print(No_of_item)
            print(Total_sum)
         data="P"
         f = urllib.urlopen(link % data)
         print(f.read())
         f.close()
         time.sleep(30)
      else:
         print("Trolley 2")
         while a.input(status) == False:
            data = "S"
            f = urllib.urlopen(link % data)
            f.close()
            time.sleep(1)
            print("Slide Sw to Srt")
            No_of_item = 0
            Total_sum = 0
            p119 = False
            pA29 = False
            pE4C = False
          p3B9 = False
            pA33 = False
         while a.input(status) == True:
            print ("Place the card")
            x=data1.read(12)#print upto 10 data at once and the remaining on the second line
             print x
            if(x == "5100AACC92A5"): #Marri Gold to add send 1, to remove send 2
               if(p119 == False):
                  print("Mari Gold")
                  price=15
                  print(price)
                  No_of_item = No_of_item + 1
                  Total_sum = Total_sum + 15
                  data = "1"
                  data_url()
                  p119 = True
               elif(p119 == True):
                  print("Mari Gold")
                  No_of_item = No_of_item - 1
                  Total_sum = Total_sum - 15
                  data = "2"
                  data_url()
                  p119 = False
            elif(x == "5100AAB45C13"): #school bag to add send 3, to remove send 4
               if(pA29 == False):
                  price=700
                  print(price)
                  No_of_item = No_of_item + 1
                  Total_sum = Total_sum + 700
                  data="3"
                  data_url()
                  pA29 = True
               elif(pA29 == True):
                  No_of_item = No_of_item - 1
                  Total_sum = Total_sum - 700
                  data="4"
                  data_url()
                  pA29 = False    
            elif(x == "5100AADA6544"): # sugar to add send 5, to remove send 6
               if(pE4C == False):
                  price=400
                  print(price)
                  print("Sugar- 10Kg")
                  No_of_item = No_of_item + 1
                  Total_sum = Total_sum + 400
                  #lcd_send_data()
                  data="5"
                  data_url()
                  pE4C = True
               elif(pE4C == True):
                  print("Sugar- 10Kg")
                  No_of_item = No_of_item - 1
                  Total_sum = Total_sum - 400
                  #lcd_send_data()
                  data="6"
                  data_url()
                  pE4C = False    
            elif(x == "5100AA7BC343"): # fair & lovely to add send 7, to remove send 8
               if(p3B9 == False):
                  print("Fair & lovely - 200gm")
                  price=200
                  print(price)
                  No_of_item = No_of_item + 1
                  Total_sum = Total_sum + 200
                   data_url()
                  p3B9 = True
                  data="7"
                  data_url()
               elif(p3B9 == True):
                  print("Fair & lovely - 200gm")
                  No_of_item = No_of_item - 1
                  Total_sum = Total_sum - 200
                  data="8"
                  data_url()
                  p3B9 = False    
            elif(x == "5100AAD62C01"): # nirma to add send 9, to remove send A
               if(pA33 == False):
                  print("Washing Powder Nirma - 5Kg")
                  price=300
                  print(price)
                  No_of_item = No_of_item + 1
                  Total_sum = Total_sum + 300
                  #lcd_send_data()
                  data="9"
                  data_url()
                  pA33 = True
               elif(pA33 == True):
                  print("Washing Powder Nirma - 5Kg")
                  No_of_item = No_of_item - 1
                  Total_sum = Total_sum - 300
                  data="A"
                  data_url()
                  pA33 = False   
                 print(No_of_item)
            print(Total_sum)
data="Q"
         f = urllib.urlopen(link % data)
         print(f.read())
         f.close()
         time.sleep(30)   
except KeyboardInterrupt:
       data1.close()
