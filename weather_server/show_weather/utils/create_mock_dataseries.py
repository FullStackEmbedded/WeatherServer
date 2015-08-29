import pandas as pd
import numpy as np

rng = pd.date_range('1/1/2014', '1/1/2015', freq='H')
frame = pd.DataFrame(index=rng)
frame_len=len(frame)
frame['t2m'] = np.random.uniform(295, 305, frame_len)
frame['pressure'] = np.random.randint(980, 1020, frame_len)
frame['relative_humidity'] = np.random.randint(30, 100, frame_len)
frame['precipitation'] = np.random.randint(0, 10, frame_len)
frame['wind_speed'] = np.random.uniform(0, 30, frame_len)
frame['wind_direction'] = np.random.randint(0, 359, frame_len)

frame.to_csv('data_series.csv')
