from urllib import request
import time
url = "http://mahavidyalay.in/AcademicDevelopment/ServerDemo/ShowLed27.php"
product = 0
amount = 0
mari = False
School_bag = False
Sugar = False
Fair = False
Nirma = False
status = True
while(1):
      #print(status)
      #f = urllib.urlopen(link)
      response = request.urlopen(url)
      #m = f.read()
      m=response.read()
      #print(m)
      if(m == b'S'):
            product = 0
            amount = 0
            mari = False
            School_bag = False
            Sugar = False
            Fair = False
            Nirma = False
            status = True
      elif(m == b'P'):
            if(status == True):
                  status = False
      elif(m == b'Q'):
            if(status == True):
                  status = False
      elif(m == b'1'):
            if(mari ==  False):
                  product = product + 1;
                  amount = amount + 15;
                  mari = True
      elif(m == b'2'):
            if(mari ==  True):
                  product = product - 1;
                  amount = amount - 15;
                  mari = False
      elif(m == b'3'):
            if(School_bag ==  False):
                  product = product + 1;
                  amount = amount + 700;
                  School_bag = True
      elif(m == b'4'):
            if(School_bag ==  True):
                  product = product - 1;
                  amount = amount - 700;
                  School_bag = False
      elif(m == b'5'):   
            if(Sugar ==  False):
                  product = product + 1;
                  amount = amount + 400;
                  Sugar = True
      elif(m == b'6'):
            if(Sugar ==  True):
                  product = product - 1;
                  amount = amount - 400;
                  Sugar = False
      elif(m == b'7'):
            if(Fair ==  False):
                  product = product + 1;
                  amount = amount + 200;
                  Fair = True
      elif(m == b'8'):
            if(Fair ==  True):
                  product = product - 1;
                  amount = amount - 200;
                  Fair = False
      elif(m == b'9'):
            if(Nirma ==  False):
                  product = product + 1;
                  amount = amount + 300;
                  Nirma = True
      elif(m == b'A'):
            if(Nirma ==  True):
                  product = product - 1;
                  amount = amount - 300;
                  Nirma = False
      if(status == True):      
            print("Total Product = %d" % product)
            print(product)
            print(amount)
            print("Amount = %s"  % amount)

      if(status == False):
            print("===========================================================")
            print("===========================================================")
            if(m == b'P'):
                  print("Bill of Trolley1")
            elif(m == b'Q'):
                  print("Bill of Trolley2")
                print("===========================================================")
            print("===========================================================")
            if(mari == True):
                  print("Britaniya Mari Gold = 15/-")
            if(School_bag ==  True):
                  print("School Bag = 700/-")
            if(Sugar ==  True):
                  print("Sugar 10Kg = 400/-")
            if(Fair ==  True):
                  print("Fair & Lovely = 200/-")
            if(Nirma ==  True):
                  print("Washing Powder Nirma = 300/-")
            print("------------------------------------------------------------")
            print("Total Amount = %d/-" %amount)
            print("============================================================")
            time.sleep(20)
