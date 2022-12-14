
data = [0, -100, 100, 67, -67, 67, 99, 15, 16, -15]

def sort_1(lst):
    result = sorted(lst, key = abs, reverse = True)
    #print(result)
    return result

def sort_2(lst):
    result_with_lambda = sorted(lst, key = lambda x: abs(x), reverse = True)
    return result_with_lambda

def main_s():
    result = sort_1(data)
    print (result)

    result_with_lambda = sort_2(data)
    print(result_with_lambda)

if __name__ == "__main__":
    main_s()
