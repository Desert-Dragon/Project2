"""

"""

from itertools import combinations_with_replacement

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}


HOTEL_BUDGET = int(850)


def averageperweek(dictkey, nameofdict):
    d = []
    y = []
    Temps = {}
    o = nameofdict
    for p in dictkey:
        t = o[p]
        y.append(max(t))
        b = (sum(y)/len(y))
        Temps[b] = p
    for keys in Temps:
        d.append(keys)
    d.sort(reverse= True)
    foo = sum(y)/len(y)
    return d, Temps, foo
def costdict(combs, referencedict):
    fres = {}
    uss = []
    for i in combs:
        bdg = []
        for tt in i:
            gg = referencedict[tt]
            bdg.append(gg)
        uss.append(sum(bdg))
        fres[i] = uss[-1]
    return fres
def finalbudget(dictkeys, refdict):
    global HOTEL_BUDGET
    jk = []
    for i in dictkeys:
        jk.append(i)
    min_cost = HOTEL_BUDGET
    for k in jk:
        cost = int(refdict[k])
        if (HOTEL_BUDGET - cost) < min_cost and HOTEL_BUDGET >= cost:
            min_cost = HOTEL_BUDGET - cost
            best_option = k
    return k
# For whatever reason the commented out code below refused to work for me, thus the above code is borrowed from the combinatorics lecture we had right before break.
#    ttt = min(jk, key=lambda o: HOTEL_BUDGET - jk[o] if HOTEL_BUDGET >= jk[o] else HOTEL_BUDGET)
#    return ttt
x = []
z = {}
if __name__ == "__main__":
    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())
    tmp, dict, maxes = averageperweek(cities,city_temps)
    for e in tmp:
        x.append(dict[e])
    w = list(combinations_with_replacement(hotels, len(cities)))
    z = costdict(w, hotel_rates)
    zt = list(z.keys())
    zz = finalbudget(zt, z)
    #print(tmp)
    #print(dict)
    print(f'Here is your best route: {x} the average of the daily max temp. is {maxes}F')
    # ..
    print(f'To max out your hotel budget, stay at these hotels: {zz}, totaling ${z[zz]}')


### This is the borrowed code block for the finalbudget function, I will however look into the cause of why my code was not working.

# #  if we didn't have the builtin min function .. we could do this
# #
# min_cost = BUDGET
# best_option = []
# for c in combs:
#     cost = cost_func(c)
#     if (BUDGET - cost) < min_cost and BUDGET >= cost:
#         min_cost = BUDGET - cost
#         best_option = c
#
# print(cost_func(best_option), best_option)