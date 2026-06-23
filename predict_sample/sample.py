from predict import predict


if __name__ == '__main__':
    day = 28
    hour = 12
    min = 50
    pre_min = 10
    pre_arr = predict(day, hour, min, pre_min)
    print(f"=== 11/{day} {hour}:{min} -> {pre_min}===")
    print(pre_arr)

    exit(1)