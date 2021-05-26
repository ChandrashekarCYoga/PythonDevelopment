from banhammer import BanHammer

# Assume that we're using the spec definition of the `Bans` and `Ratios` objects above
from my_triggers import Bans, Ratios

# default construction
BAN = BanHammer(Bans, Ratios)

# you can also set these params as defaults on init:
BAN = BanHammer(Bans, Ratios, track_rates=True,
                return_rates=True, track_subnet=True)
