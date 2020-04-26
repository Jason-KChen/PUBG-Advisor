import math

weaponKillMapArr = [{},{},{},{},{},{},{},{},{},{}]
maxWeaponArr = ['', '', '', '', '', '', '', '', '', '']

count = 0
f = open('../PUBG_DATA/Baltic_Main_data.txt', 'r')
for line in f:
    # print(line)
    count += 1
    if (count % 1000000) == 0: 
        print('first iter count: ' + str(count))
    lineArr = line.split(',')
    stage = math.floor(float(lineArr[7]))
    weaponName = lineArr[8]
    scope = lineArr[12]
    muzzle = lineArr[13]

    if weaponName not in weaponKillMapArr[stage - 1]:
        weaponKillMapArr[stage - 1][weaponName] = 1
    else:
        weaponKillMapArr[stage - 1][weaponName] += 1
    
    if 'max' not in weaponKillMapArr[stage - 1] or weaponKillMapArr[stage - 1][weaponName] > weaponKillMapArr[stage - 1]['max']:
        weaponKillMapArr[stage - 1]['max'] = weaponKillMapArr[stage - 1][weaponName]
        maxWeaponArr[stage - 1] = weaponName

f.close()

for i in range(9):
    print('stage: ' + str(i))
    print('weapon: ' + maxWeaponArr[i])
    print('kill: ' + str(weaponKillMapArr[i]['max']))



scopeMapArr = [{},{},{},{},{},{},{},{},{},{}]
maxScopeArr = ['', '', '', '', '', '', '', '', '', '']
muzzleMapArr = [{},{},{},{},{},{},{},{},{},{}]
maxMuzzleArr = ['', '', '', '', '', '', '', '', '', '']

f = open('../PUBG_DATA/Baltic_Main_data.txt', 'r')
# print(len(f.read()))
count = 0
for line in f:
    count += 1
    if (count % 1000000) == 0: 
        print('second iter ount: ' + str(count))
    lineArr = line.split(',')
    stage = math.floor(float(lineArr[7]))
    weaponName = lineArr[8]
    scope = lineArr[12]
    muzzle = lineArr[13]

    for i in range(9):
        if i == stage and weaponName == maxWeaponArr[i]:
            if scope not in scopeMapArr[i]:
                scopeMapArr[i][scope] = 1
                # print(scopeMapArr[i][scope])
            else:
                scopeMapArr[i][scope] += 1
                # print(scopeMapArr[i][scope])
            if 'max' not in scopeMapArr[i] or scopeMapArr[i][scope] > scopeMapArr[i]['max']:
                scopeMapArr[i]['max'] = scopeMapArr[i][scope]
                maxScopeArr[i] = scope
                # print(scopeMapArr[i]['max'])
                # print(maxScopeArr[i])

            if muzzle not in muzzleMapArr[i]:
                muzzleMapArr[i][muzzle] = 1
            else:
                muzzleMapArr[i][muzzle] += 1
            if 'max' not in muzzleMapArr[i] or muzzleMapArr[i][muzzle] > muzzleMapArr[i]['max']:
                muzzleMapArr[i]['max'] = muzzleMapArr[i][muzzle]
                maxMuzzleArr[i] = muzzle
    
f.close()

for i in range(9):
    print('stage: ' + str(i))
    print('weapon: ' + maxWeaponArr[i])
    print('kill: ' + str(weaponKillMapArr[i]['max']))
    print('scope: ' + maxScopeArr[i])
    print('muzzle: ' + maxMuzzleArr[i])