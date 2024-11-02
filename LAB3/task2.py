# TODO Напишите функцию find_common_participants
def find_common_participants(c,d,divider =","):
    a=set(c.split(divider))
    b=set(d.split(divider))
    common_list=list(set(a).intersection(b))
    common_list.sort
    return common_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
output=find_common_participants(participants_first_group,participants_second_group,"|")
print(output)