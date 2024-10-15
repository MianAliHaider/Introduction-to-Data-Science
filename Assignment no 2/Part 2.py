def count_uniq(trans):
    uniq = set()
    for i in trans:
        uniq.add(i[1])
    return len(uniq)

def trans_high_amount(trans):
    high_trans = trans[0]
    for i in trans:
        if i[2] > high_trans[2]:
            high_trans = i
    return high_trans


def id(trans):
    trans_id = []
    user_id = []
    for i in trans:
        trans_id.append(i[0])
        user_id.append(i[1])
    return trans_id, user_id

transactions = [
    (101, 1, 250.0, '2024-10-12 10:00'),
    (102, 2, 150.0, '2024-10-12 11:00'),
    (103, 3, 300.0, '2024-10-12 12:00'),
    (104, 1, 400.0, '2024-10-12 13:00'),
    (105, 2, 100.0, '2024-10-12 14:00'),
]


unique_users_count = count_uniq(transactions)
highest_transaction = trans_high_amount(transactions)
transaction_ids, user_ids = id(transactions)


print("Total unique users:", unique_users_count)
print("Transaction with the highest amount:", highest_transaction)
print("Transaction IDs:", transaction_ids)
print("User IDs:", user_ids)
