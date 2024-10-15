def filter_high_ratings(feedback):
    high_rated_users = {}
    for user_id, details in feedback.items():
        if details['rating'] >= 4:
            high_rated_users[user_id] = details['rating']
    return high_rated_users

def top_5_users_by_rating(feedback):
    def get_rating(item):
        return item[1]['rating']
    
    sorted_feedback = sorted(feedback.items(), key=get_rating, reverse=True)
    return dict(sorted_feedback[:5])

def combine_feedback(*feedback_dicts):
    combined_feedback = {}
    for feedback in feedback_dicts:
        for user_id, details in feedback.items():
            if user_id not in combined_feedback:
                combined_feedback[user_id] = {'rating': details['rating'], 'comments': details['comments']}
            else:
                combined_feedback[user_id]['rating'] = max(combined_feedback[user_id]['rating'], details['rating'])
                combined_feedback[user_id]['comments'] += f" {details['comments']}"
    return combined_feedback

def ratings_greater_than_three(feedback):
    result = {}
    for user_id, details in feedback.items():
        if details['rating'] > 3:
            result[user_id] = details['rating']
    return result


# Example feedback data
feedback1 = {
    1: {'rating': 5, 'comments': 'Excellent service!'},
    2: {'rating': 3, 'comments': 'Average experience.'},
    3: {'rating': 4, 'comments': 'Good quality.'},
}

feedback2 = {
    2: {'rating': 4, 'comments': 'Improved from last time.'},
    3: {'rating': 2, 'comments': 'Not satisfied.'},
    4: {'rating': 5, 'comments': 'Loved it!'},
}

# Filtering users with ratings of 4 or higher
high_rated_users = filter_high_ratings(feedback1)
print("Users who rated 4 or higher:", high_rated_users)

# Getting the top 5 users by rating
top_users = top_5_users_by_rating(feedback1)
print("Top 5 users by rating:", top_users)

# Combining feedback from multiple dictionaries
combined_feedback = combine_feedback(feedback1, feedback2)
print("Combined feedback:", combined_feedback)

# Dictionary comprehension for ratings greater than 3
high_ratings = ratings_greater_than_three(combined_feedback)
print("Users with ratings greater than 3:", high_ratings)
