# str1='Sofia Statsenko'
# def name(str1):
#     list1=str1.split(' ')
#     for i in list1:
#         if i=='':
#             print("Введите корректные данные")
#             quit()
#     list1.reverse()
#     str2=' '.join(list1)
#     a=str2
#     return a
# print(name(str1))
#
#
# a='sofia1981-s@mail.ru'
# if a.count('@')==1 and 1<=a.count('.')<=2 and a[-3:]=='.ru' or a[-4:]=='.com':
#     print(a)
# else:
#     print("False")
#
#
# list1=['мандаринки', 'лимоны', 'киви','апельсины']
# try:
#     index = int(input('Введите индекс '))
#     for i in range(len(list1)):
#         if index==i:
#             print(list1[i])
# except ValueError:
#     print('Это не число!')
# except IndexError:
#     print("ВВеден индекс за границей списка") - не выводит ошибку про индекс
#
# def dliny(a):
#     c=round(2*a,2)
#     b=round((c**2-a**2)**0.5,2)
#     return c,b
# print(dliny(2))


