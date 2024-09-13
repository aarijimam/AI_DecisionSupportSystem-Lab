import numpy as np

def fibonacci(n):
    series = [0,1]
    for i in range(n)[1:]:
        series.append(series[i-1] + series[i])
    return series


if __name__ == '__main__':
    print(fibonacci(10))
