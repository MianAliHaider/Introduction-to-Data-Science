def filter(data):
    filtered_names = []
    for i in data:
        if i[2] > 30 and i[3] in ('USA','Canada'):
            filtered_names.append(i[1])
    return filtered_names

def age(data):
    return data[2]

def top_oldest(data):
    sort_age = sorted(data,key=age,reverse=True)
    return sort_age[:100]

def duplicate(data):
    name = []
    duplicate = []
    for i in data:
        if i[1] in name and i[1] not in duplicate:
            duplicate.append(i[1])
        name.append(i[1])
    return duplicate

def main():
    users = [
    (1, 'Alice', 32, 'USA'),
    (2, 'Bob', 29, 'Canada'),
    (3, 'Charlie', 35, 'USA'),
    (4, 'David', 22, 'UK'),
    (5, 'Eve', 40, 'USA'),
    (6, 'Frank', 28, 'Canada'),
    (7, 'Grace', 33, 'Canada'),
    (8, 'Heidi', 25, 'Germany'),
    (9, 'Ivan', 31, 'USA'),
    (10, 'Judy', 40, 'Canada'),
    (11, 'Eve', 40, 'Canada'),
    (12, 'Alice', 32, 'USA'),
    (13, 'Bob', 29, 'Canada'),
    (14, 'Charlie', 35, 'USA'),
    (15, 'David', 22, 'UK'),
    (16, 'Eve', 40, 'USA'),
    (17, 'Frank', 28, 'Canada'),
    (18, 'Grace', 33, 'Canada'),
    (19, 'Heidi', 25, 'Germany'),
    (20, 'Ivan', 31, 'USA'),
    (21, 'Judy', 40, 'Canada'),
    (22, 'Eve', 40, 'Canada'),
    (23, 'Charlie', 35, 'USA'),
    (24, 'David', 22, 'UK'),
    (25, 'Eve', 40, 'USA'),
    (26, 'Frank', 28, 'Canada'),
    (27, 'Grace', 33, 'Canada'),
    (28, 'Heidi', 25, 'Germany'),
    (29, 'Ivan', 31, 'USA'),
    (30, 'Judy', 40, 'Canada'),
    (31, 'Eve', 40, 'Canada') 
]

    filtered = filter(users)
    oldest = top_oldest(users)
    duplicates = duplicate(users)

    print("Filtered names:", filtered)
    print("Top 10 oldest:", oldest)
    print("Duplicate names:", duplicates)

if __name__ == "__main__":
    main()
