
from src.config.config_bankheist import bankheist_config
from src.config.config_roulette import roulette_config
from src.config.config_pointsystem import pointsystem_config

# To add a command:
#
#   '!<command>': {
#       'return': <return type, type a string if plain text, type function if there is logic to it>,
#       'cooldown': <cooldown time in seconds, if not defined, no cooldown is set>,
#       'argc': <number of arguments taken by the command, only if return type is command,
#                   default 0, don't count arg_username as a argument>,
#       'arg_username': <True/False, if true, will pass the username as first argument, default False>,
#       'usage': <short description about how to send the arguments of a command>
#   }
#
# If 'return' == 'command' you need to add a file src/lib/commands/<command>.py
#   with the logic to determin the return and logic of the command

commands_config = {
    # Example commands
    '!findcard': {
        'usage': '!findcard [cardname] (no spaces, use : for cards with : in their name, but nothing past : )',
        'return': 'command',
        'cooldown': 10,
        'argc': 1,
    }


} # End of commands
