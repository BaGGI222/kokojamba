# def strcounter(s):
#     sym_dict = {}
#     for sym in s:
#         count = 0
#         for sub_sym in s:
#             sym_dict[sym] = 1 + sym_dict.get(sym, 0)
#         print(f'{sym} - {count}') 


def strcounter(s):
    sym_dict = {}
    for sym in s:
        sym_dict[sym] = 1 + sym_dict.get(sym, 0)

    for sym, count in sym_dict.items():
        print(f'{sym} - {count}')

strcounter('asdadddd')
