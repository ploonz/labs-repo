# TODO Напишите функцию для поиска индекса товара
def func(find_item,items_list):
 for i, item in enumerate(items_list):
     if item == find_item:
       return i
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = func(find_item,items_list)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
