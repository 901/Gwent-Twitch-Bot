
config = {

    # Details required to login to twitch IRC server
    'server': 'irc.twitch.tv',
    'port': 6667,
    'username': 'gwent_bot',
    'oauth_password': 'oauth:xxxxxxxxxxxxxxxxxxxxxxxxx', # get this from http://twitchapps.com/tmi/

    # Channel to join
    'channel': 'yourchannelhereinlowercase',
    'entering_message': 'Hello!!',

    # If set to true will display any debug data in console
    'debug': False,

    # Maximum amount of bytes to receive from socket (1024-4096)
    'socket_buffer_size': 1024,

    # If set true, the log will be saved to a txt file
    'save_log': True,
    'save_log_filepath': 'data/SantaBot/current_log.txt',
    'save_prevlog_filename': 'previous_log.txt'

} # End of Config
