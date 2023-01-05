# modulok

# osztályok

class Bolygo:

  # ---------------
  # konstruktor :
  # ---------------
  def __init__(self,s):
    elemek = s.strip('/n').split(';')

    self.megnev = elemek[0]   # bolygó megnevezése
    self.a = elemek[1]        # főtengely [CSE]
    self.e = elemek[2]        # excentritás
    self.fi = elemek[3]       # pályaelhajlás [fok]
    self.Y_szid = elemek[4]   # sziderikus év [nap]
    self.Y_szin = elemek[5]   # szinódikus év [nap]
    self.r_e = elemek[6]      # egyenlítő sugara [km]
    self.l = elemek[7]        # lapultság
    self.m = elemek[8]        # tömeg [földtömeg]
    self.ro = elemek[9]       # sűrűség [g/cm3]
    self.g = elemek[10]       # gravitációs gyorsulás [m/s2]
    self.P = elemek[11]       # felszíni nyomás [bar]

  # -----------------

# függvények

def betolt():
  f = open("bolygok.txt","r")

  while True:
    sor = f.readline()
    if sor == "":
      break
    else:
      bolygok.append(Bolygo(sor))

def feladat3():
  bolygok[2].g = 9.82
  bolygok[5].r_e = 60268

def feladat4():
  for i in range(0,9):
    if bolygok[i].P == 0.0:
      print(" -- {0}.".format(bolygok[i].megnev))

# programtörzs

bolygok = []

# 2. feladat
betolt()

# 3. feladat
feladat3()

# 4. feladat
feladat4()



