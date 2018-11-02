from datetime import datetime
from typing import List

import pandas as pd
from luminol import anomaly_detector
from luminol.modules.anomaly import Anomaly

sold_items = 'data/sold-items-de-summer-2018.csv'
pd.read_csv(sold_items)

detector = anomaly_detector.AnomalyDetector(time_series=sold_items)
anomalies: List[Anomaly] = detector.get_anomalies()
for a in anomalies:
    dd = datetime.utcfromtimestamp(a.exact_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    print(f'{dd}: {a.anomaly_score}')
