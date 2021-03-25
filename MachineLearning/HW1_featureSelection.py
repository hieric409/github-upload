import numpy as np
import pandas as pd
data = pd.read_csv("D:/Download/train.csv")
data.corr(method = 'spearman').to_csv('D:/Download/result.csv')