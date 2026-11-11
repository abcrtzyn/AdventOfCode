from typing import Dict, Tuple


player_health = 50
mana = 500


with open('Day22/input.txt') as f:
    lines = f.readlines()
    boss_health = int(lines[0].split()[-1])
    BOSS_DAMAGE = int(lines[1].split()[-1])


DP: Dict[Tuple[int, int, int, int, int, int],int] = {}

def boss_turn(ph: int,mana: int,bh: int,shield: int,poison: int,recharge: int, part2: bool) -> int:#,actions):
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
    
    return player_turn(ph-max(1,BOSS_DAMAGE-armour),mana,bh,shield,poison,recharge,part2)#,actions)


def player_turn(ph: int,mana: int,bh: int, shield: int,poison: int,recharge: int, part2: bool) -> int:#,actions):
    #print(ph,mana,bh,shield,poison,recharge,actions)
    key = (ph,mana,bh,shield,poison,recharge) 
    if key in DP:
        return DP[key]
    
    # hard mode lose 1 hp
    if part2:
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
        res = boss_turn(ph,mana-53,bh-4,shield,poison,recharge, part2)#,actions)
        if res != -1:
            mana_used = min(mana_used,res+53)
        #actions.pop()
    if mana >= 73:
        # drain
        #actions.append('d')
        res = boss_turn(ph+2,mana-73,bh-2,shield,poison,recharge, part2)#,actions)
        if res != -1:
            mana_used = min(mana_used,res+73)
        #actions.pop()
    if mana >= 113 and shield == 0:
        # shield
        #actions.append('s')
        res = boss_turn(ph,mana-113,bh,6,poison,recharge, part2)#,actions)
        if res != -1:
            mana_used = min(mana_used,res+113)
        #actions.pop()
    if mana >= 173 and poison == 0:
        # poison
        #actions.append('p')
        res = boss_turn(ph,mana-173,bh,shield,6,recharge, part2)#,actions)
        if res != -1:
            mana_used = min(mana_used,res+173)
        #actions.pop()
    if mana >= 229 and recharge == 0:
        # recharge
        #actions.append('r')
        res = boss_turn(ph,mana-229,bh,shield,poison,5, part2)#,actions)
        if res != -1:
            mana_used = min(mana_used,res+229)
        #actions.pop()
    if mana_used == 1000000000000:
        mana_used = -1

    if key not in DP:
        DP[key] = mana_used
    
    return mana_used

# this is a search problem

print('Part 1:',player_turn(player_health,mana,boss_health,0,0,0,False))
DP = {}  # pyright: ignore[reportConstantRedefinition]
print('Part 2:',player_turn(player_health,mana,boss_health,0,0,0,True))
