# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September',
          'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September',
          'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# write your update damages function here:

new_damages=[]
def calculate_damages(data):
    conversion = {"M": 1000000,
                  "B": 1000000000}
    for temp in damages:
        if temp == "Damages not recorded":
            new_damages.append(temp)
        if temp[-1] == 'M':
            new_damages.append(float(temp[0:-1]) * 1000000)
        if temp[-1] == 'B':
            new_damages.append(float(temp[0:-1]) * 1000000000)
    return new_damages


new_damages = calculate_damages(damages)
print(new_damages)


# write your construct hurricane dictionary function here:

def hurricanes_dict(names, months, years, max_sustained_winds,areas_affected, deaths, new_damages):
    hurricanes = {}
    hurricanes_num = len(names)
    for i in range(hurricanes_num):
        hurricanes[names[i]] = {
            "Name":names[i],"Months":months[i], "Years":years[i],
            "Max Sustained Winds": max_sustained_winds[i], "Areas Affected": areas_affected[i],
            "Deaths": deaths[i], "Damage": new_damages[i]}
    return hurricanes
    hurricanes = {name for name in names}
    for i in hurricanes:
        hurricanes[i].update(hurricanes_list)
    return hurricanes

hurricanes = hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, deaths, new_damages)
print(hurricanes)



# write your construct hurricane by year dictionary function here:

def hurricanes_year(hurricanes):
    hurricanes_by_year = {}
    for i in hurricanes:
        current_year = hurricanes[i]['Years']
        cur_hurricane = hurricanes[i]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = cur_hurricane
        else:
            hurricanes_by_year[current_year].append(cur_hurricane)
        return hurricanes_by_year

hurricanes_by_year = hurricanes_year(hurricanes)
print(hurricanes_by_year)

# write your count affected areas function here:
def cal_affected(hurricanes):
    affected_areas_num = {}
    for i in hurricanes:
        for area in hurricanes[i]['Areas Affected']:
            if area not in affected_areas_num:
                affected_areas_num[area] = 1
            else:
                affected_areas_num[area] += 1
    return affected_areas_num

counter = cal_affected(hurricanes)
print(counter)




# write your find most affected area function here:

def most_affected(counter):
    max = 'Florida'
    max_area = 0
    for i in counter:
        if counter[i] > max_area:
            max = i
            max_area = counter[i]
    return max, max_area

result = most_affected(counter)
print(result)


# write your greatest number of deaths function here:
def most_deaths(hurricanes):
    maximum = 'Cuba I'
    count = 0
    for i in hurricanes:
        if hurricanes[i]['Deaths'] > count:
            maximum = i
            count = hurricanes[i]['Deaths']
    return maximum, count

deadliest = most_deaths(hurricanes)
print(deadliest)





# write your catgeorize by mortality function here:

def mort_cat(hurricanes):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    scale = {0:[], 1:[], 2:[], 3:[], 4: []}
    for i in hurricanes:
        deaths = hurricanes[i]["Deaths"]
        if deaths == mortality_scale[0]:
            scale[0].append(hurricanes[i])
        elif deaths >mortality_scale[0] and deaths <= mortality_scale[1]:
            scale[1].append(hurricanes[i])
        elif deaths > mortality_scale[1] and deaths <= mortality_scale[2]:
            scale[2].append(hurricanes[i])
        elif deaths > mortality_scale[2] and deaths <= mortality_scale[3]:
            scale[3].append(hurricanes[i])
        else:
            scale[4].append(hurricanes[i])
    return scale

scales = mort_cat(hurricanes)
print(scales)





# write your greatest damage function here:

def most_dmg(hurricanes):
    maximum = 'Cuba I'
    count = 0
    for i in hurricanes:
        if hurricanes[i]['Damage'] == "Damages not recorded":
            pass
        elif hurricanes[i]['Damage'] > count:
            maximum = i
            count = hurricanes[i]['Damage']
    return maximum, count

damages = most_dmg(hurricanes)
print(damages)




# write your catgeorize by damage function here:

def scale_by_dmg(hurricanes):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    scale = {0: [], 1: [], 2: [], 3: [], 4: []}
    for i in hurricanes:
        damage = hurricanes[i]["Damage"]
        if damage == "Damages not recorded":
            scale[0].append(hurricanes[i])
        elif damage >damage_scale[0] and damage <= damage_scale[1]:
            scale[1].append(hurricanes[i])
        elif damage > damage_scale[1] and damage <= damage_scale[2]:
            scale[2].append(hurricanes[i])
        elif damage > damage_scale[2] and damage <= damage_scale[3]:
            scale[3].append(hurricanes[i])
        elif damage > damage_scale[3] and damage <= damage_scale[4]:
            scale[4].append(hurricanes[i])
    return scale

by_damage = scale_by_dmg(hurricanes)
print(by_damage)