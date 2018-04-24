from providers.jokerFansub import JokerFansub
from providers.inmanga     import Inmanga
from mangaDownloader import MangaDownloader

if __name__== "__main__":

  # JOKERFANSUB #########################################################################################
  #############################
  ### Descarga de One Piece ###
  #############################
  path  = 'http://reader.jokerfansub.com/read/_one_piece/es/VOL/CHAPTER/page/'
  # color = { 36: [337,338, 339], 35: [336,335,334,333,332,331,330,329,328], 34: [327,326,325,324,323,322,321,320,319,318,317], 33: [316,315,314,313,312,311,310,309,308,307,306], 32: [305,304,303,302,301,300,299,298,297,296], 31: [295,294,293,292,291,290,289,288,287,286], 30: [285,284,283,282,281,280,279,278,277,276], 29: [275,274,273,272,271,270,269,268,267,266,265], 28: [264,263,262,261,260,259,258,257,256], 27: [255,254,253,252,251,250,249,248,247], 26: [246,245,244,243,242,241,240,239,238,237], 25: [236,235,234,233,232,231,230,229,228,227], 24: [226,225,224,223,222,221,220,219,218,217], 23: [216,215,214,213,212,211,210,209,208,207,206], 22: [205,204,203,202,201,200,199,198,197,196], 21: [195,194,193,192,191,190,189,188,187], 20: [186,185,184,183,182,181,180,179,178,177], 19: [176,175,174,173,172,171,170,169,168,167], 18: [166,165,164,163,162,161,160,159,158,157,156], 17: [155,154,153,152,151,150,149,148,147,146], 16: [145,144,143,142,141,140,139,138,137], 15: [136,135,134,133,132,131,130,129,128,127], 14: [126,125,124,123,122,121,120,119,118], 13: [117,116,115,114,113,112,111,110,109], 12: [108,107,106,105,104,103,102,101,100], 11: [99,98,97,96,95,94,93,92,91], 10: [90,89,88,87,86,85,84,83,82], 9:  [81,80,79,78,77,76,75,74,73,72], 8:  [71,70,69,68,67,66,65,64,63], 7:  [62,61,60,59,58,57,56,55,54], 6:  [53,52,51,50,49,48,47,46,45], 5:  [44,43,42,41,40,39,38,37,36], 4:  [35,34,33,32,31,30,29,28,27], 3:  [26,25,24,23,22,21,20,19,18], 2:  [17,16,15,14,13,12,11,10,9], 1:  [8,7,6,5,4,3,2,1]}
  # news  = { 93: [896,895,894,893,892,891,890,889,888,887,886,885,884,883,882,881,880,879,878,877,876,875,874,873,872,871,870,869,868,867,866,865,864,863,862,861,860,859,858,857,856,855], 92: [846,845,844,843,842,841,840,839,838,837,836], 91: [835,834,833,832,831,830,829,828,827,826], 90: [825,824,823,822,821,820,819,818,817,816,815,814], 80: [813,812,811,810,809,808,807,806,805,804,803,802,801,800,799,798,797,796], 79: [795,794,793,792,791,790,789,788,787,786], 78: [785,784,783,782,781,780,779] }
  news  = { 93: [865] }
  vols  = news

  provider = JokerFansub(vols, 'http://reader.jokerfansub.com/read/_one_piece/es/', path)
  md = MangaDownloader(provider)
  # md.download_mangas()
   
  #####################################
  ### Descarga de Dragon Ball Super ###
  #####################################
  path = 'http://reader.jokerfansub.com/read/dragon_ball_super/es/VOL/CHAPTER/page/'
  vols = {
    5: [29, 28, 27], 
    4: [26, 25], 
    3: [24, 23, 22, 21, 20, 19, 18, 17], 
    2: [16, 15, 14, 13, 12, 11, 10, 9, 8, 7], 
    1: [6, 5, 4, 3, 2, 1]
  }

  provider = JokerFansub(vols, 'http://reader.jokerfansub.com/read/dragon_ball_super/es/', path)
  md = MangaDownloader(provider)
  # md.download_mangas()

  # INMANGA #############################################################################################
  # +===========+===========+
  # |   NAME    | MANGA ID  |
  # +===========+===========+
  # | One Piece | one_piece |
  # +-----------+-----------+

  # print(range(598,599))

  provider = Inmanga('One Piece', 'one_piece', range(598,903))
  md = MangaDownloader(provider)
  md.download_mangas()