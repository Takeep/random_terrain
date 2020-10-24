import random

top_terrain = ['|----------|', ' [-| |-----| |-']
mid_terrain = ['   0000',       'L_____| |______]']
mid_terrain2 = ['   ||  ',     ' |              | ']
low_level = ['      __',      ' ________________']

def create_terrain():
    top_level = random.choice(top_terrain)
    mid_level = random.choice(mid_terrain)
    mid_level2 = random.choice(mid_terrain2)
    low_level1 =  random.choice(low_level)

    print(top_level)
    print(mid_terrain)
    print(mid_terrain2)
    print(low_level1)

    return

create_terrain()
