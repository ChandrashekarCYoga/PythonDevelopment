

# define actions. all actions are called with args:
#         scope: any string or number, e.g. "1.2.3.4"
#         duration: action_duration
#         key: the lookup key for config inside self.bans, e.g. "login_failed"
#         window: time window
#         limit: max count within window
class Action:
    """ define actions to be executed """
    @staticmethod
    def block_local(token, duration, *args):
        pass

    @staticmethod
    def report_central(token, duration, *args):
        pass

    @staticmethod
    def record_local(token, duration, key, window, limit):
        pass


# configure ban types
Bans = {
    # arbitrary `metric` name to be used in banhammer arguments
    "login_failed": {
        # hierarchical threshold triggers
        "thresholds": [
            {
                # how many calls of this metric?
                "limit": 10,
                # how long should the window be?
                "window": 3600,
                # what action to take (if any) and how long that "block" should persist
                # for example: if another event occurs during this window (different from the above window)
                # instantly run action
                "action": [Action.block_local],
                "action_duration": 3600,
                # if one of these mitigators "metrics" is already triggered (i.e. over limit)
                # then actions will be suppressed. references existing trigger name.
                # checks first mitigator trigger threshold only.
                "mitigators": ["login_successful"]
            },
            {
                "limit": 100,
                "window": 3600,
                "action": [Action.report_central],
                "action_duration": 86400
            }
        ],
        # linked ratios to evaluate when triggered
        "ratios": ["login_failed__to__login_successful"]
    },
    # local metric only
    "login_successful": {
        "thresholds": [
            {
                "limit": 10,
                "window": 60,
                "action": [Action.record_local],
                "action_duration": 3600
            },
        ],
        "ratios": ["login_failed__to__login_successful"]
    }
}


# if either top or bottom value is 0, 1 will be used.
Ratios = {
    # ratio name to be used by `Bans` configuration above as needed
    # this defines basically a simple equation that can be used and criteria set on
    "login_failed__to__login_successful": {
        # metric name and minimum count that if met will treated as the dividend of the ratio
        # will not trigger the action below unless top counter exceeds this value
        "top": "login_failed",
        "top_minimum": 20,
        # metric name to be used as the divisor in the ratio
        "bottom": "login_successful",
        # only take action below if ratio exceeds this value
        # ie don't do anything if (login_failed / login_successful)  < 10:1
        "ratio_max": 10,
        # action to take when this ratio is exceeded
        # actions functions receive all ratio args and stats dict in their kwargs
        "action": [Action.block_local, Action.report_central],
    }
}
