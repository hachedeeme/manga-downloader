from mangaDownloader       import MangaDownloader
from providers.jokerFansub import JokerFansub
from providers.inmanga     import Inmanga
from providers.kissmanga   import Kissmanga
from providers.ninemanga   import Ninemanga

if __name__== "__main__":
  # +=======================+========================+=============+=========+
  # |          NAME         |        MANGA ID        | JOKERFANSUB | INMANGA |
  # +=======================+========================+=============+=========+
  # | One Piece             | one_piece              |      O      |    O    |
  # +-----------------------+------------------------+-------------+---------+
  # | Nanatsu No Taizai     | nanatsu_no_taizai      |             |    O    |
  # +-----------------------+------------------------+-------------+---------+
  # | Noku No Hero Academia | boku_no_hero_academia  |             |    O    |
  # +-----------------------+------------------------+-------------+---------+
  # | Hajime no Ippo        | hajime_no_ippo         |             |    O    |
  # +-----------------------+------------------------+-------------+---------+
  # | Dragon Ball Super     | dragon_ball_super      |             |    O    |
  # +-----------------------+------------------------+-------------+---------+
  providers = {
    "jokerfansub": {
      'op'  : JokerFansub('one_piece'),
      'dbs' : JokerFansub('dragon_ball_super')
    },
    "inmanga": {
      'op'  : Inmanga('one_piece'),
      'nnt' : Inmanga('nanatsu_no_taizai'),
      'bnha': Inmanga('boku_no_hero_academia'),
      'hni' : Inmanga('hajime_no_ippo'),
      'dbs' : Inmanga('dragon_ball_super')
    },
    "kissmanga": {
      'op' : Kissmanga('one_piece_color')
    },
    "ninemanga": {
      'ookii': Ninemanga('ookii_onnanoko_wa_daisuki'),
      'mh'   : Ninemanga('mouhitsu_hallucination'),
      'ps'   : Ninemanga('prison_school'),
      'hikyu': Ninemanga('haikyuu'),
      'nnt'  : Ninemanga('nanatsu_no_taizai'),
      'bnha' : Ninemanga('boku_no_hero_academia'),
      'bnhav': Ninemanga('vigilante_boku_no_hero_academia'),
      'hni'  : Ninemanga('hajime_no_ippo')
    }
  }
  
  provider = providers['jokerfansub']['op']
  provider = providers['ninemanga']['hni']
  # provider.set_chapters([978,979])
  provider.set_chapters(range(1201,1226))

  md = MangaDownloader(provider)
  # md.enumerate_exceptions()
  # md.upload()
  # md.download_mangas()
  # md.upload_and_donwload_last()
  # md.download_last(4)