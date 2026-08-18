# def predict(x, w, b):
#     y = (w*x) + b
#     return y


# # y = wx + b
# x = 10 # input
# w = 4 # weights
# b = -3 # bias 
# predict(x , w , b) # 7


# def find_weight(x, y, b):
#     # y = wx + b <===> (y-b)/x = w 
#     w = (y - b) / x
#     # return w

# x = 3
# y = 4
# b = 1
# w = find_weight(x , y , b)


# def find_bias(x, y, w):
#     b = y - w*x
#     return b
#     # y = (wx) + b
#     # 7 = (3*2) + b
#     # 7 = 6 + b
#     # 7 - 6 = b 
#     # b = 1
#     # return b

# b = find_bias(4 , 13 , 3)
# print(b)

# x = 5
# w = 2
# b = 0
# aY = 10
# def prediction_error(x, w, b, actualY):
#     # y = wx+b
#     y = w*x + b
#     # error = y - actualY
#     error = y - actualY
#     return error

# error = prediction_error(x , w , b , aY)

# def mean_squared_error(predictions, actual):
#     MSE = 0 
#     N = len(predictions)
#     for i in range(N):
#         actualY = actual[i]
#         predictionY = predictions[i]
#         error = (predictionY - actualY) ** 2
#         MSE += error 
#     return MSE / N 

# mean = mean_squared_error(
#     [10, 20],
#     [5, 10]
# )

# → 1.6666666667

x = [1, 2, 3, 4, 5]
actual = [3, 5, 7, 9, 11]

def find_best_parameters(xArray, actual):
    # your algorithm
    startW = -10 # 10
    endW = 10 # 10
    startB = -10 # 10
    endB = 10 # 10
    best_error = 9999999
    best_w = 0
    best_b = 0
    # keys = {}

    # for number in actual:
        # keys[number] = {'w': [] , 'b': []}

    for w in range(startW , endW + 1):
        for b in range(startB , endB + 1):
            total_error = 0
            for k in range(len(xArray)):
                x = xArray[k]
                actualY = actual[k]
                y = w*x + b
                error = (y - actualY) ** 2
                total_error += error
            mse = total_error / len(xArray) 
            if mse < best_error : 
                best_error = mse
                best_w = w
                best_b = b

                # if sum == 0:
                #     # keys[actualY]['w'].append(w)
                #     # keys[actualY]['b'].append(b)
                #     print("found something" , y , w , x , b)

    w = best_w 
    b = best_b
    # countWeights = {}
    # countBiases = {}



#     for key in keys : 
#         object = keys[key]
#         weights = object['w']
#         biases = object['b']

#         for j in range(len(weights)):
#             countWeights[weights[j]] = 0

#         for j in range(len(biases)):
#             countBiases[biases[j]] = 0



#     for key in keys : 
#         object = keys[key]
#         weights = object['w']
#         biases = object['b']

#         for j in range(len(weights)):
#             weight = weights[j]
#             countWeights[weight]+=1

#         for j in range(len(biases)):
#             bias = biases[j]
#             countBiases[bias]+=1

#     maxW = -9999999
#     w = 0
#     for key in countWeights:
#         weight = key
#         count  = countWeights[key]
#         if count > maxW : 
#             w = weight 
#             maxW = count


#     maxB = -99999999
#     b = 0
#     for key in countBiases:
#         bias = key
#         count = countBiases[key]
#         if count > maxB : 
#             b = bias
#             maxB = count
#         # print(countBiases[key])


    return w,b

w , b = find_best_parameters(x, actual)

print("w =", w)
print("b =", b)