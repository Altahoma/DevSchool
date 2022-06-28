table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]

table_suites = [suit[-1] for suit in table_cards]
hand_suites = [suit[-1] for suit in hand_cards]

suites = table_suites + hand_suites

# flush = False
# for suite in 'CDHS':
#     if suites.count(suite) >= 5:
#         flush = True
#         break

flush = any([suites.count(suite) >= 5 for suite in 'CDHS'])

if flush:
    print('Flush!')
else:
    print('No Flush!')
