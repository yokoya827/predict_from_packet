import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from predict_func.predict import predict
import datetime
import plotly.figure_factory as ff

df = pd.read_json("higashiyama_meta.json")
#dt_now = datetime.datetime.now()
df1 = pd.read_csv("20211128.csv")

def elephant_population(x):
    y = int((x[4]+x[5]+x[33])/3)
    return y

def monkey_population(x):
    y = int((x[16]+x[22])/2)
    return y

def tower_population(x):
    y = int((x[31]+x[32]+x[14])/3)
    return y

def child_zoo_population(x):
    y = int((x[21]+x[23])/2)
    return y

def plant_population(x):
    y = int((x[30]+x[29]+x[24]+x[34])/4)
    return y

    


def make_a_list():
    dt_now = datetime.datetime.now()
    pupulation = [[], [], [], [], [], [], [], [], [], [], [], [], []]

    pupulation[0].append('ズーボーゲート')
    pupulation[1].append('休憩室')
    pupulation[2].append('象エリア')
    pupulation[3].append('子供動物園')
    pupulation[4].append('ライオン')
    pupulation[5].append('ズー・デ・ガッテン')
    pupulation[6].append('海洋エリア')
    pupulation[7].append('猿エリア')
    pupulation[8].append('遊園地')
    pupulation[9].append('アメリカゾーン')
    pupulation[10].append('スカイタワー')
    pupulation[11].append('ボート乗り場')
    pupulation[12].append('植物園')
    print(pupulation[0])

    #dt_now = datetime.datetime.now()
    pre_arr = [0]*37

    for est_min in [0, 10, 30, 60]:
           
        if(est_min == 0):
            tmp = 60*dt_now.hour + dt_now.minute
            for column in range(37):
                pre_arr[column] = df1.iat[tmp, column + 2]
            
        else:            
            pre_arr = predict(28, dt_now.hour, dt_now.minute, est_min)
            index = 0
            for item in pre_arr:
                if item < 0:
                    pre_arr[index] = 0
                index += 1    
            
        pupulation[0].append(str(pre_arr[35]))
        pupulation[1].append(str(pre_arr[3]))
        pupulation[2].append(str(elephant_population(pre_arr)))
        pupulation[3].append(str(child_zoo_population(pre_arr)))
        pupulation[4].append(str(pre_arr[6]))
        pupulation[5].append(str(pre_arr[34]))
        pupulation[6].append(str(pre_arr[18]))
        pupulation[7].append(str(monkey_population(pre_arr)))
        pupulation[8].append(str(pre_arr[20]))
        pupulation[9].append(str(pre_arr[12]))
        pupulation[10].append(str(tower_population(pre_arr)))
        pupulation[11].append(str(pre_arr[27]))
        pupulation[12].append(str(plant_population(pre_arr)))
    return pupulation


def make_map(day, hour, min, pre_min):
    global df
    df = df.dropna(subset=['latitude', 'longitude'])
    #データフレームの読み込み
    if(pre_min == 0):
        tmp = 60*hour + min
        df['Population'] = [df1.at[tmp, 'HZ001'], df1.at[tmp, 'HZ002'], df1.at[tmp, 'HZ003'], df1.at[tmp, 'HZ004'], df1.at[tmp, 'HZ005'], df1.at[tmp, 'HZ006'], df1.at[tmp, 'HZ007'], df1.at[tmp, 'HZ008'], df1.at[tmp, 'HZ009'], df1.at[tmp, 'HZ010'], df1.at[tmp, 'HZ011'], df1.at[tmp, 'HZ012'], df1.at[tmp, 'HZ013'], df1.at[tmp, 'HZ014'], df1.at[tmp, 'HZ015'], df1.at[tmp, 'HZ016'], df1.at[tmp, 'HZ017'], df1.at[tmp, 'HZ018'], df1.at[tmp, 'HZ019'], df1.at[tmp, 'HZ020'], df1.at[tmp, 'HZ021'], df1.at[tmp, 'HZ022'], df1.at[tmp, 'HZ023'], df1.at[tmp, 'HZ024'], df1.at[tmp, 'HZ026'], df1.at[tmp, 'HZ027'], df1.at[tmp, 'HZ029'], df1.at[tmp, 'HZ030'], df1.at[tmp, 'HZ031'], df1.at[tmp, 'HZ032'], df1.at[tmp, 'HZ033'], df1.at[tmp, 'HZ034'], df1.at[tmp, 'HZ035'], df1.at[tmp, 'HZ036'], df1.at[tmp, 'HZ037'], df1.at[tmp, 'HZ038'], df1.at[tmp, 'HZ039']]

    else:
        pre_arr = predict(day, hour, min, pre_min)
        index = 0
        for item in pre_arr:
            if item < 0:
                pre_arr[index] = 0
            index += 1    
        df['Population'] = [pre_arr[0], pre_arr[1], pre_arr[2], pre_arr[3], pre_arr[4], pre_arr[5], pre_arr[6], pre_arr[7], pre_arr[8], pre_arr[9], pre_arr[10], pre_arr[11], pre_arr[12], pre_arr[13], pre_arr[14], pre_arr[15], pre_arr[16], pre_arr[17], pre_arr[18], pre_arr[19], pre_arr[20], pre_arr[21], pre_arr[22], pre_arr[23], pre_arr[24], pre_arr[25], pre_arr[26], pre_arr[27], pre_arr[28], pre_arr[29], pre_arr[30], pre_arr[31], pre_arr[32], pre_arr[33], pre_arr[34], pre_arr[35], pre_arr[36]]
    
    fig = px.scatter_mapbox(
    # データフレームおよび緯度・経度の設定
    data_frame=df,
    lat="latitude",
    lon="longitude",
    hover_data=["name"],
    color="Population",
    size="Population",
    size_max=70,
    opacity=0.5,
    range_color= [0,800],
    color_continuous_scale = 'Jet',
    zoom=15,
    height=700,
    width=1200)
    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

def make_table():
    pupulation = make_a_list()

    df_population = pd.DataFrame(
        columns=['場所', '現在時刻', '10分後', '30分後', '1時間後']
    )

    for tmp in range(13):
        df_population.loc[tmp] = pupulation[tmp]

    fig = ff.create_table(df_population)
    return fig



#グラフを作る
def make_graph():
    dt_now = datetime.datetime.now()
    go.Figure(make_table()).write_html('./templates/table.html')
    go.Figure(make_map(28, dt_now.hour, dt_now.minute, 60)).write_html('./templates/hour.html')
    go.Figure(make_map(28, dt_now.hour, dt_now.minute, 30)).write_html('./templates/bo.html')
    go.Figure(make_map(28, dt_now.hour, dt_now.minute, 10)).write_html('./templates/oresen.html')
    go.Figure(make_map(28, dt_now.hour, dt_now.minute, 0)).write_html('./templates/en.html')


if __name__ == '__main__':
    a = make_a_list()
    make_graph()