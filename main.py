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
      'op'    : Ninemanga('one_piece'),
      'beelz' : Ninemanga('beelzebub'),
      'bers'  : Ninemanga('berserk'),
      'ct2002': Ninemanga('captain_tsubasa_road_to_2002'),
      'ookii' : Ninemanga('ookii_onnanoko_wa_daisuki'),
      'mh'    : Ninemanga('mouhitsu_hallucination'),
      'ps'    : Ninemanga('prison_school'),
      'hikyu' : Ninemanga('haikyuu'),
      'nnt'   : Ninemanga('nanatsu_no_taizai'),
      'hxh'   : Ninemanga('hunter_x_hunter'),
      'bnha'  : Ninemanga('boku_no_hero_academia'),
      'vbnha' : Ninemanga('vigilante_boku_no_hero_academia'),
      'bbt'   : Ninemanga('boin_boin_teacher'),
      'hni'   : Ninemanga('hajime_no_ippo')
    }
  }
  
  provider = providers['jokerfansub']['op']
  provider = providers['ninemanga']['beelz']
  # provider.set_chapters([978,979])
  # provider.set_chapters(range(1,46))

  md = MangaDownloader(provider)
  # md.download_full_manga()
  # md.enumerate_exceptions()
  # md.upload()
  # md.download_mangas()
  # md.upload_and_donwload_last()
  # md.download_last(3)
