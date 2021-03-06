from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.formula.api as an
from statsmodels.stats.anova import anova_lm



a = pd.DataFrame({"X1": [0,0,10,10,20,20], "X2": [0,0,100,100,400,400], "Y": [5,7,15,17,9,11]})
result = an.ols(formula="Y ~ X1 + X2", data=a).fit()
print result.params
print(anova_lm(result))
print(result.summary())

fig = plt.figure()
axis = fig.add_subplot(111, projection='3d')
axis.scatter(a['X1'], a['X2'], a['Y'], c='r', marker='o')
xx, yy = np.meshgrid(a['X1'],a['X2'])
exog = pd.core.frame.DataFrame({'X1':xx.ravel(),'X2':yy.ravel()})
out = result.predict(exog=exog)
axis.plot_surface(xx, yy, out.values.reshape(xx.shape), rstride=1, cstride=1, alpha='0.2', color='None')
axis.set_xlabel("X1")
axis.set_ylabel("X2")
axis.set_zlabel("Y")
plt.show()

