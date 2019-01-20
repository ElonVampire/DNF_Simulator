import os
for roles in os.listdir('Equip'):
    for pos in os.listdir(f'Equip/{roles}'):
        if os.path.getsize(f'Equip/{roles}/{pos}')==0:
            os.remove(f'Equip/{roles}/{pos}')
            print(f'Equip/{roles}/{pos}')
