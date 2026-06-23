import numpy as np
import tensorflow as tf
import os


# 入力ファイル
path_data = os.path.join(os.path.dirname(__file__), "data_processed" )
path_pickle = os.path.join(os.path.dirname(__file__), "pickle_file")

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
    data_test_list = [np.loadtxt(os.path.join(path_data, filename_test_list[i]), delimiter=',', skiprows=1) for i in range(len(filename_test_list))]

    # データのカット(6時台から１８時台まで)
    # data_test_list = [data[480: 1140] for data in data_test_list]

    # データを一つの配列にまとめる
    data_test = np.concatenate(data_test_list)


    # 60分前からのデータを結合する
    data_predict = np.block([np.roll(data_test, shift, axis=0) for shift in range(60)])

    # 訓練したパラメータの読み込み
    network = tf.keras.models.load_model(
        os.path.join(path_pickle, f'network_{pre_min}.h5'),
        compile=False
    )

    # データの推定
    index_data = 3600*(day-28) + 60*(hour) + min + pre_min
    pre_arr = network.predict(data_predict[index_data].reshape(1, 2340))

    return pre_arr[0].astype(int)

