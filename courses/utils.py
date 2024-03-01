def redistribute_groups(groups, total_users, users_per_group):
    for group in groups:
        current_users = group.students.count()
        if current_users < users_per_group:
            while current_users < users_per_group and total_users > 0:
                other_group = find_group_with_most_users(groups)
                move_user_to_group(other_group, group)
                current_users += 1
                total_users -= 1
        elif current_users > users_per_group:
            remove_excess_users(group, current_users - users_per_group)


def find_group_with_most_users(groups):
    return max(groups, key=lambda group: group.students.count())


def move_user_to_group(from_group, to_group):
    user_to_move = from_group.students.first()
    from_group.students.remove(user_to_move)
    to_group.students.add(user_to_move)


def remove_excess_users(group, excess):
    users_to_remove = group.students.all()[:excess]
    for user in users_to_remove:
        group.students.remove(user)
