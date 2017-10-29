'''
Please use lowercase for dictionary keys in the future // Rachel

# default probability in Security mode is prob_a: 0, prob_b: 100

# positive -> sec_1bl_1ch;
# negative -> sec_2bl_1ch;
# independent -> sec_1bl_2ch;
# single -> sec_ownrisk

'''

data = [
    {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    {'mode': 'sec_1bl_2ch', 'm': 100, 'p_x': 2, 'p_y': 1, 'prob_a': 50},
    {'mode': 'sec_1bl_1ch'   , 'm': 100, 'p_x': 1, 'p_y': 3, 'prob_a': 50},
    {'mode': 'sec_1bl_1ch'   , 'm': 100, 'p_x': 1, 'p_y': 3, 'prob_a': 50},
    {'mode': 'sec_2bl_1ch'   , 'm': 100, 'p_x': 1, 'p_y': 3, 'prob_a': 50},
    {'mode': 'sec_ownrisk'   , 'm': 100, 'p_x': 2, 'p_y': 3, 'prob_a': 50},
    {'mode': 'sec_ownrisk_fixedother'   , 'm': 100, 'p_x': 2, 'p_y': 3, 'prob_a': 50, 'partner_a': 20},
    {'mode': 'sec_otherrisk_ownfixed'   , 'm': 100, 'p_x': 2, 'p_y': 3, 'prob_a': 50, 'you_a': 30}
]

def checkValidity():
    for period in data:
        if 'prob_a' in period:
            if period['prob_a'] < 0 or period['prob_a'] > 100:
                print('ERROR: invalid prob_a in round', data.index(period), ': prob_a is: ',
                    period['prob_a'], ' but must be a number between 0 and 100')
                return 0
    return 1

def numberOfPeriod():
    return len(data)

def getDynamicValues():
    if checkValidity() == 0:
        return 0
    return data


# old config data
# data = [
#     {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
#     {'mode': 'independent', 'm': 100, 'p_x': 2, 'p_y': 1, 'prob_a': 50},
#     {'mode': 'positive'   , 'm': 100, 'p_x': 1, 'p_y': 3, 'prob_a': 50},
#     {'mode': 'negative'   , 'm': 100, 'p_x': 1, 'p_y': 3, 'prob_a': 50},
#     {'mode': 'single'   , 'm': 100, 'p_x': 2, 'p_y': 3, 'prob_a': 50}
# ]
