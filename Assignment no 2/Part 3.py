def visit_both(page_a,page_b):
    return page_a.intersection(page_b)

def visit_not_both(page_a,page_c):
    return page_a.symmetric_difference(page_c)

def update_page_a(page_a,new_id):
    page_a.update(new_id)

def remove_from_page_b(page_b,user_id_to_remove):
    page_b.difference_update(user_id_to_remove)

page_a_users = {1, 2, 3, 4}
page_b_users = {3, 4, 5, 6}
page_c_users = {4, 5, 7, 8}

both_visitors = visit_both(page_a_users, page_b_users)
print("Users who visited both Page A and Page B:", both_visitors)

either_not_both_visitors = visit_not_both(page_a_users, page_c_users)
print("Users who visited either Page A or Page C, but not both:", either_not_both_visitors)

new_user_ids = {5, 6}
update_page_a(page_a_users, new_user_ids)
print("Updated Page A users:", page_a_users)

user_ids_to_remove = [3, 5]
remove_from_page_b(page_b_users, user_ids_to_remove)
print("Updated Page B users:", page_b_users)
