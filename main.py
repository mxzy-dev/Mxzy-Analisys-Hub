import os
import requests as rq

#elements

enter = "-Нажмите Enter чтобы продолжить--}"
CLEAR = "\033[H\033[2J"
BLUE = "\033[1;34m"
RESET = "\033[0m"
banner = f"""{BLUE}
\t\t╔════════════════════════════════╗
\t\t ║                                                                                 ║
\t\t║        M X Z Y   A N A L I S Y S   H U B                     ║
\t\t ║by Mxzy.                                                                         ║
\t\t╚════════════════════════════════╝
"""

#helpers functions

def menu():
      try:
            print(banner)
            print(CLEAR)
            print(banner)
            print("\t\t\t\t\t\t--ФУНКЦИИ--")
            print("\n0. Базовый анализис веб сайтов\t\t|\t1. Выйти")
            sel = int(input("\n\n-Выберите функцию:"))
            if sel == 0:
                  retry(scan)
            elif sel == 1:
                  quit()
            else:
                  print("\n-Выберите один из вариантов!")
                  input(enter)
                  retry(menu)
      except TypeError:
            print("-Вставте цифру выбранного варианта!")
            input(enter)
            retry(menu)

def retry(x):
      print(CLEAR)
      x()

def rec(num,dir, name, x):
      with open(f"{dir}{name}", "w",encoding="utf-8") as num:
            num.write(x)

#analisys

def urly(dir):
      url = input("\n-Вставте ссылку для анализа:")
      if url == "":
            urly()
      req = rq.get(url)
      print(req)
      rsq = rq.options(url)
      print(rsq)
      print(f"доступные методы: {rsq.headers.get('Allow')} ")
      print("-----------------------------")
      rec(1,dir,"url.txt",req.url)
      rec(2,dir,"text.txt", req.text)
      rec(3,dir,"siteoffl.html", req.text)
      try:
            rec(4,dir,"json.txt",req.json())
      except rq.exceptions.JSONDecodeError:
            rec(4,dir,"json.txt","there is no json")

#start

def scan():
      print(banner)
      print(CLEAR)
      print(banner)
      try:
            d = input(f"{RESET}\n-Название созданной папки куда будут направленны результаты анализа:\n____________________________________________________________________\n")
            print("-----------------------------------------------------------------------------------")
            if d == "" :
                  print("-Вы не можете указать пустоту!")
                  retry(scan)
            dir = f"/sdcard/{d}/"
            with open(f"{dir}README.txt", "w",encoding="utf-8") as rdm:
                  rdm.write("Это универсальный инструмент созданный Mxzy. dvlp . Используйте его с умом для благих целей. Данный инструммент дает доступ только к публично досигаемой информации в рамках закона.\nBy Mxzy.")
            
      except FileNotFoundError:
            print("Поиск папки:", os.path.abspath(dir))
            print("\n\n-Вы указали несуществующую или недоступную папку.")
            input(enter)
            retry(scan)
      urly(dir)
      input(enter)
      menu()
  
#run

menu()