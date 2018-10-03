from mangaDownloader       import MangaDownloader
from providers.jokerFansub import JokerFansub
from providers.inmanga     import Inmanga
from providers.kissmanga   import Kissmanga
from providers.ninemanga   import Ninemanga

if __name__== "__main__":
  # +==================================+=================================+=============+=========+===========+
  # |                     NAME         |                 MANGA ID        | JOKERFANSUB | INMANGA | NINEMANGA |
  # +==================================+=================================+=============+=========+===========+
  # | Beelzebub                        | beelzebub                       |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Berserk                          | berserk                         |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Boin Boin Teacher                | boin_boin_teacher               |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Noku No Hero Academia            | boku_no_hero_academia           |             |    O    |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Captain Tsubasa Road to 2002     | captain_tsubasa_road_to_2002    |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Dragon Ball Super                | dragon_ball_super               |      O      |    O    |           |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Haikyuu                          | haikyuu                         |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Hajime no Ippo                   | hajime_no_ippo                  |             |    O    |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Hinomaru Zumou                   | hinomaru_zumou                  |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Hunter X Hunter                  | hunter_x_hunter                 |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Kimi Wa 008                      | kimi_wa_008                     |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Mouhitsu Hallucination           | mouhitsu_hallucination          |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Nanatsu no Taizai                | nanatsu_no_taizai               |             |    O    |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | One Piece                        | one_piece                       |      O      |    O    |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Ookii Onnanoko Wa Daisuki        | ookii_onnanoko_wa_daisuki       |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Prison School                    | prison_school                   |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
  # | Vigilante: Noku No Hero Academia | vigilante_boku_no_hero_academia |             |         |     O     |
  # +----------------------------------+---------------------------------+-------------+---------+-----------+
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
      'beelz' : Ninemanga('beelzebub'), 
      'bers'  : Ninemanga('berserk'), 
      'bbt'   : Ninemanga('boin_boin_teacher'), 
      'bnha'  : Ninemanga('boku_no_hero_academia'), 
      'ct2002': Ninemanga('captain_tsubasa_road_to_2002'), 
      'hikyu' : Ninemanga('haikyuu'), 
      'hni'   : Ninemanga('hajime_no_ippo'), 
      'hz'    : Ninemanga('hinomaru_zumou'), 
      'hxh'   : Ninemanga('hunter_x_hunter'), 
      'kw008' : Ninemanga('kimi_wa_008'), 
      'mh'    : Ninemanga('mouhitsu_hallucination'), 
      'nnt'   : Ninemanga('nanatsu_no_taizai'), 
      'op'    : Ninemanga('one_piece'), 
      'ookii' : Ninemanga('ookii_onnanoko_wa_daisuki'), 
      'ps'    : Ninemanga('prison_school'), 
      'vbnha' : Ninemanga('vigilante_boku_no_hero_academia')
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
