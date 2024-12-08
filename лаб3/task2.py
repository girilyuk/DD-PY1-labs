# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=","):
    group1 = group1.split(delimiter)
    group2 = group2.split(delimiter)
    common_participants = \
        list(set(group1).intersection(group2))
    common_participants.sort()

    return common_participants


# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
participants_intersection =\
    find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(participants_intersection)