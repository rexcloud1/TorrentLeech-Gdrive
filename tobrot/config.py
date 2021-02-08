from tobrot.sample_config import Config

class Config(Config):
    TG_BOT_TOKEN= "805271341:AAEC_-Ed9t78MvfCB6qzKfyoynXQxils630"
    APP_ID = "1055007"
    API_HASH = "22ba7b6be602b2d4c5aa28836e4bdc41"
    AUTH_CHANNEL = [-1001255404856]
    INDEX_LINK = "https://torrentleech.torrentleech-gdrive.workers.dev"
    GLEECH_COMMAND = "gleech"
    YTDL_COMMAND = 'ytdl'
    TELEGRAM_LEECH_COMMAND_G = "tleech"
    CLONE_COMMAND_G = "gclone"
    PYTDL_COMMAND_G = "pytdl"
    STATUS_COMMAND = "status"
    DESTINATION_FOLDER = "TorrentLeech-Gdrive"
    LEECH_COMMAND = "leech"
    #fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    # Do not delete [DRIVE] #do not delete [DRIVE] but replace remaining part with yours data..if more data use common sense
    RCLONE_CONFIG = """
[DRIVE]
type = drive
scope = drive
token = {"ac—fill—yours—data—jNc3MpTRy2PuGD_Lvsodct---fill--yours---0-18T12:11:26.58411451Z"}
team_drive = 0ABS@gautamk9PVA"""