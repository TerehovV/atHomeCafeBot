def convert_basket(dct, tabs=0):
    res = []
    pref = ' ' * 2 * tabs
    for k, v in dct.items():
        res += [pref + str(k) + ' - ' + str(v) + ' шт']
    return '\n'.join(res)