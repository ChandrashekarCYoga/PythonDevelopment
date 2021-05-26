

class BanHammer:
    def __init__(self, Bans, Ratios, track_rates=True, return_rates=True, track_subnet=True):
        '''
        Bans: a dict object matching the Bans object spec below. Main configuration for the banhammer library
        Ratios: a dict that sets a number of ratios that are relevant to the metrics defined in Bans that 
        we can use to perform actions on if needed.
        '''
        self.Bans = Bans
        self.Ratios = Ratios
        self.track_rates = track_rates
        self.return_rates = return_rates
        self.track_subnet = track_subnet
        print(Bans)
        print(Ratios)

        

    def incr(token, metric, **kwargs):
        '''
        Increments a counter for the given metric in concordance with the Bans and Ratios configurations

        Arguments:
                        token: Caller token address to track against (typically an IP address)
                        metric: User-defined Bans configuration metric that we want to increment.
                        **kwargs: Any of the keys in kwargs can override any specific setting in Bans default configuration object and should have the behavior as if that was the original config.
                Returns: a passed, stats_dict tuple where:
                        passed indicates true/false based on whether it should be blocked or not based on the configuration
                        stats_dict is a dict of "seen" request rates over the a set of periods of time 
        '''
        print("incr")

    def now(token, metric, **kwargs):
        '''
        immediately bans a given token and stores for future use
        '''
        print("now")

    def status_all():
        '''
        Returns a list of all of the current tokens, metrics, and their seen rates
        Returns:
                        stats_aggregate_dict: A slightly modified version of the stats_dict (defined below) 
                        where each key will be a metric name, and each value would be the stats_dict for that metric.
        '''

        print("status_all")
