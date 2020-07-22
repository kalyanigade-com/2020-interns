

# Name-Kalyani Gade
# //Emailid-kalyanigade98@gmail.com
# //college Name-Trinity college of engineering and research pune
# //mob no-8551937350

# //[T-1] programme

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_json('new_data.json')
df.head()

inr_values = []
for json_data in df.rates:
    inr_values.append(json_data['INR'])

    plt.plot(inr_values)
plt.show()