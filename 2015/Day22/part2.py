player_health = 50
mana = 500

boss_health = 51
boss_damage = 9

DP = {}

def boss_turn(ph,mana,bh,bd,shield,poison,recharge):#,actions):
    #print(ph,mana,bh,shield,poison,recharge,actions)
    if bh <= 0:
        # winning action
        #print('kill')
        return 0
    
    if shield > 0:
        armour = 7
        shield -= 1
    else:
        armour = 0
    if poison > 0:
        bh -= 3
        poison -= 1
    if recharge > 0:
        mana += 101
        recharge -= 1

    if bh <= 0:
        # winning action
        #print('kill')
        return 0
    
    return player_turn(ph-max(1,bd-armour),mana,bh,bd,shield,poison,recharge)#,actions)

def player_turn(ph,mana,bh,bd,shield,poison,recharge):#,actions):
    #print(ph,mana,bh,shield,poison,recharge,actions)
    key = (ph,mana,bh,shield,poison,recharge) 
    if key in DP:
        #print(key,DP[key])
        return DP[key]
    
    # hard mode lose 1 hp
    ph -= 1
    # if ph and bh still greater than 0, keep going
    if ph <= 0:
        # losing
        #print('dead')
        return -1
    
    # handle effects
    if shield > 0:
        shield -= 1
    if poison > 0:
        bh -= 3
        poison -= 1
    if recharge > 0:
        mana += 101
        recharge -= 1


    if bh <= 0:
        # winning
        #print('kill')
        return 0
    
    # try to all 5 actions
    mana_used = 1000000000000
    
    if mana < 53:
        # cant cast anything, lose
        #print('energy')
        return -1
    if mana >= 53:
        # missile
        #actions.append('m')
        res = boss_turn(ph,mana-53,bh-4,bd,shield,poison,recharge)#,actions)
        if res != -1:
            mana_used = min(mana_used,res+53)
        #actions.pop()
    if mana >= 73:
        # drain
        #actions.append('d')
        res = boss_turn(ph+2,mana-73,bh-2,bd,shield,poison,recharge)#,actions)
        if res != -1:
            mana_used = min(mana_used,res+73)
        #actions.pop()
    if mana >= 113 and shield == 0:
        # shield
        #actions.append('s')
        res = boss_turn(ph,mana-113,bh,bd,shield+6,poison,recharge)#,actions)
        if res != -1:
            mana_used = min(mana_used,res+113)
        #actions.pop()
    if mana >= 173 and poison == 0:
        # poison
        #actions.append('p')
        res = boss_turn(ph,mana-173,bh,bd,shield,poison+6,recharge)#,actions)
        if res != -1:
            mana_used = min(mana_used,res+173)
        #actions.pop()
    if mana >= 229 and recharge == 0:
        # recharge
        #actions.append('r')
        res = boss_turn(ph,mana-229,bh,bd,shield,poison,recharge+5)#,actions)
        if res != -1:
            mana_used = min(mana_used,res+229)
        #actions.pop()
    if mana_used == 1000000000000:
        mana_used = -1

    if key not in DP:
        DP[key] = mana_used
    
    return mana_used

# this is a search problem

print(player_turn(player_health,mana,boss_health,boss_damage,0,0,0))