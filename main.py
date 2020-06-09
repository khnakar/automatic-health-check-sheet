import pandas as pd
from datetime import datetime as dt, timedelta

from times import GetRandomTime
from body_temp import BodyTemp


def main(temp, dates):
    dates = range_date([dt.strptime(val, '%Y-%m-%d') for val in dates.values()])

    random_time = GetRandomTime(len(dates))
    body_temp = BodyTemp(temp['min'], temp['max'])

    df_temp = pd.DataFrame({'朝の体温(℃)': body_temp.get_random_body_temp(len(dates))}, columns=['朝の体温(℃)', ], index=dates)
    df_time = pd.DataFrame({'起床時刻': random_time.get_time(morning=True),
                            '就寝時刻': random_time.get_time(night=True)}, columns=['起床時刻', '就寝時刻'], index=dates)

    print(output:=pd.DataFrame.join(df_temp, df_time,))

    return output

def range_date(date_):

    return tuple(date_[0] + timedelta(days=i) for i in range((date_[1]-date_[0]).days + 1))

if __name__ == '__main__':
    body_temperature = {
        'min': 36.0,
        'max': 37.0}
    date = {
        "start": '2020-06-11',#format: 'YYYY-mm-dd'
        "end": '2020-06-24', #format: 'YYYY-mm-dd'
        }

    main(body_temperature, date)
