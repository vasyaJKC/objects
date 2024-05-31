# 1
# def family(name):
#     Family = {
#         "Darth Vader": "father",
#         "Leia": "sister",
#         "Han": "brother in law",
#         "R2D2": "droid"
#     }
#
#     if name in Family:
#         return f"Luke, I am your {Family[name]}. "
#     else:
#         return "Error"
#
#
# print(family("Darth Vader"))  # ---> "Luke, I am your father."
# print(family("Leia"))
# print(family("Han"))
#
#
# # 2
# def get_budgets(l):
#     tot = 0
#     for x in l:
#         tot += x['budget']
#     return tot
#
#
# print(get_budgets([
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }
# ]))  # --->65700
#
# print(get_budgets([
#   { "name": "John",  "age": 21, "budget": 29000 },
#   { "name": "Steve",  "age": 32, "budget": 32000 },
#   { "name": "Martin",  "age": 16, "budget": 1600 }
# ]))  #----->62600
#
#
#
# # 3
# def get_students_names(vv):
#     lst = []
#     for x in vv:
#         lst.append(x)
#     return sorted(vv.values())
#
# print(get_students_names({
#   "Student 1": "Steve",
#   "Student 2": "Becky",
#   "Student 3": "John"
# }))  # ---->["Becky", "John", "Steve"]
#
# # 4
# def maximum_score(vvv):
#     lst = []
#     for x in vvv:
#         lst.append(x['score'])
#     return sum(lst)
#
#
#
# print(maximum_score([
# { "tile": "N", "score": 1 },
# { "tile": "K", "score": 5 }, { "tile": "Z", "score": 10 },
# { "tile": "X", "score": 8 }, { "tile": "D", "score": 2 },
# { "tile": "A", "score": 1 }, { "tile": "E", "score": 1 } ]))  #--->28
#
# print(maximum_score([{ "tile": "B", "score": 2 },{ "tile": "V", "score": 4 },
# {"tile": "F", "score": 4 }, { "tile": "U", "score": 1 },
# {"tile": "D", "score": 2 }, { "tile": "O", "score": 1 },
# { "tile": "U", "score": 1 } ]))  #---->15
#
#
#
# # 5
# def mapping(str):
#     ss = {}
#
#     for s in str:
#         if type(s) == set:
#             pass
#
#         else:
#             ss[s] = s.upper()
#     return ss
#
#
#
# print(mapping(["p", "s"]))   #--->{'p': 'P', 's': 'S'}
# print(mapping(["a", "b", "c"]))
# print(mapping(["a", "v", "y", "z"]))
#
#
# # 6
# def count_all(sss):
#     result = {"LETTERS": 0, "DIGITS": 0}
#
#     for x in sss:
#         if x.isalpha():
#             result["LETTERS"] += 1
#         elif x.isdigit():
#             result["DIGITS"] += 1
#
#     return result
#
#
# # Examples
# print(count_all("Hello World"))  # ➞ { "LETTERS": 10, "DIGITS": 0 }
# print(count_all("H3ll0 Wor1d"))
# print(count_all("149990"))
#
#
# # 7
# def calc_diff(set1, set2):
#     s = 0
#     for x in set1:
#         if x in set2:
#             s += min(set1[x] - set2[x], set2[x] + set1[x])
#         else:
#             s += set1[x]
#     return s
#
#
# print(calc_diff({ "baseball bat": 20 }, { "baseball bat": 5 })) # ---->15
# print(calc_diff({"skate": 10, "painting": 20 }, {"skate": 19}))
# print(calc_diff({"skate": 200, "painting": 200, "shoes": 1 }, {"skate": 400}))


# 8
# def get_distance(x,y):
#     return ((x['x'] ,y['x']) + (x['y'] y['y']) * 1/2)
#
# print(get_distance({"x": -2, "y": 1}, {"x": 4, "y": 3}))
# print(get_distance({"x": 0, "y": 0}, {"x": 1, "y": 1}))
# print(get_distance({"x": 10, "y": -5}, {"x": 8, "y": 16}))



# 9
# def dict_to_list(www):
#     lis = []
#     lst = list(www.items())
#     lis.append(lst[1])
#     lis.append(lst[-1])
#     lis.append(lst[0])
#     return lis
#
#
# print(dict_to_list({
#   "D": 1,            #---> [("B", 2), ("C", 3), ("D", 1)]
#   "B": 2,
#   "C": 3
# }))
# print(dict_to_list({
#   "likes": 2,
#   "dislikes": 3,
#   "followers": 10
# }))



# 10
# def oldest(w):
#     for x,y in w.items():
#         if type(y) == int:
#             if y >= y:
#                 return x
#
# print(oldest({
#   "Emma": 71,
#   "Jack": 45,
#   "Amy": 15,
#   "Ben": 29
# }))
# print(oldest({
#   "Max": 9,
#   "Josh": 13,
#   "Sam": 48,
#   "Anne": 33
# }))


# 11
# def top_note(ww):
#     for x,y in ww.items():
#         if x == 'notes':
#             for _ in y:
#                 ww.update({'notes':max(y)})
#     return ww
#
#
# print(top_note({"name": "John", "notes": [3, 5, 4]}))  #---->{ "name": "John", "top_note": 5 }
# print(top_note({"name": "Max", "notes": [1, 4, 6]}))
# print(top_note({"name": "Zygmund", "notes": [1, 2, 3]}))



# 12
# def profit(fun):
#     res = 0
#     for x,k in fun.items():
#         if type(k) == int or float:
#             res += k
#     return res
#
#
# print(profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }))---->14796
# print(profit({
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "inventory": 100
# }))
# print(profit({
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# }))


