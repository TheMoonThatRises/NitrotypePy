from ...bootstrap import bootstrap

def loot(loot_id = 0):
    loot_list = bootstrap.bootstrap('loot')

    for loot in loot_list:
        if loot['lootID'] == loot_id:
            return loot

    return False
