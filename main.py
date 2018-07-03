from mangaDownloader       import MangaDownloader
from providers.jokerFansub import JokerFansub
from providers.inmanga     import Inmanga

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
    }
  }
  provider = providers['inmanga']['op']
  # provider.set_chapters([900])

  md = MangaDownloader(provider)
  # md.upload()
  # md.download_mangas()
  # md.upload_and_donwload_last()