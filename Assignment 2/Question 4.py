test_list = [(5, 6), (2, 4), (5, 7), (2, 5)]
print("The original list is : " + str(test_list))
sub_list = [7, 2, 4, 6]
res = [sub + tuple(sub_list) for sub in test_list]
print("The modified list : " + str(res))
