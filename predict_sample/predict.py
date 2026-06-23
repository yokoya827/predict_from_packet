import numpy as np
import pickle


# 入力ファイル
path_data = "./data_processed/"

filename_test_list = ["20211128.csv", "20211129.csv", "20211130.csv"]
def predict(day, hour, min, pre_min=10):
    """

    :param day: 予測する時刻
    :param hour: 予測する時刻
    :param min: 予測する時刻
    :param pre_min: 何分後を予測するか
    :return: 予測したパケット数の配列
    """
    # データのロード
    data_test_list = [np.loadtxt(path_data + filename_test_list[i], delimiter=',', skiprows=1) for i in range(len(filename_test_list))]

    # データを一つの配列にまとめる
    data_test = np.concatenate(data_test_list)

    # 60分前からのデータを結合する
    data_predict = np.block([np.roll(data_test, shift, axis=0) for shift in range(60)])

    # 訓練したネットワークの読み込み
    with open('network.pickle', mode='rb') as f:
        network = pickle.load(f)

    # データの推定
    index_data = 3600*(day-28) + 60*(hour) + min
    pre_arr = network.predict(data_predict[index_data].reshape(1, 2340))

    return pre_arr[:, 2:].astype(int)

