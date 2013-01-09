     ____  _       _                         _ ____  _  ___             _   
    |  _ \(_)_ __ | |__   ___   __ _ _ __ __| |___ \| |/ (_)_ __  _ __ | |_ 
    | |_) | | '_ \| '_ \ / _ \ / _` | '__/ _` | __) | ' /| | '_ \| '_ \| __|
    |  __/| | | | | |_) | (_) | (_| | | | (_| |/ __/| . \| | |_) | |_) | |_ 
    |_|   |_|_| |_|_.__/ \___/ \__,_|_|  \__,_|_____|_|\_\_| .__/| .__/ \__|
                                                           |_|   |_|        


# What?

Pinboard2Kippt transfers your Pinboard bookmarks to Kippt.

# How?

    from pinboard2kippt import Pinboard2Kippt

    i = Pinboard2Kippt(pinboard_user=USER, pinboard_pass=PASS,
                       kippt_user=USER, kippt_pass=PASS)
    i.transfer()