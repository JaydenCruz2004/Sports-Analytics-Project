import pandas as pd
import numpy as np
from scipy import stats

# Load and filter data
df = pd.read_csv('badminton_wrld_tour.csv')
df = df[df['matches_played'] >= 3].copy()
df['is_singles'] = (df['discipline'] == 'Singles').astype(int)

# Define predictors and response
X = df[['shot_pct', 'pt_differential_per_match', 'is_singles', 'matches_played']].values
y = df['win_pct'].values
n = len(y)

# Add intercept column
X_mat = np.column_stack([np.ones(n), X])
col_names = ['Intercept', 'shot_pct', 'pt_diff/match', 'is_singles', 'matches_played']

# OLS via normal equations
beta = np.linalg.lstsq(X_mat, y, rcond=None)[0]
y_hat = X_mat @ beta
residuals = y - y_hat
p = X_mat.shape[1]

# Model fit statistics
SS_res = np.sum(residuals**2)
SS_tot = np.sum((y - y.mean())**2)
R2     = 1 - SS_res / SS_tot
R2_adj = 1 - (1 - R2) * (n - 1) / (n - p)
RMSE   = np.sqrt(SS_res / n)
MSE    = SS_res / (n - p)

# Standard errors, t-stats, p-values
se     = np.sqrt(MSE * np.diag(np.linalg.inv(X_mat.T @ X_mat)))
t_stat = beta / se
p_vals = [2 * (1 - stats.t.cdf(abs(t), df=n-p)) for t in t_stat]

# F-statistic
F   = (R2 / (p - 1)) / ((1 - R2) / (n - p))
F_p = 1 - stats.f.cdf(F, p - 1, n - p)

# Print results
print("OLS REGRESSION RESULTS")
print("Variable               Coef      SE        t         p      Sig")
print("-" * 65)
for i, name in enumerate(col_names):
    sig = "***" if p_vals[i] < 0.001 else "**" if p_vals[i] < 0.01 else "*" if p_vals[i] < 0.05 else ""
    print(name.ljust(22), round(beta[i], 4), str(round(se[i], 4)).rjust(8),
          str(round(t_stat[i], 4)).rjust(8), str(round(p_vals[i], 4)).rjust(8), sig.rjust(4))
print("-" * 65)
print("")
print("R2          =", round(R2, 4))
print("Adjusted R2 =", round(R2_adj, 4))
print("RMSE        =", round(RMSE, 4))
print("F-statistic =", round(F, 2), " (p =", "{:.2e}".format(F_p), ")")
print("n           =", n)
print("")
print("Sig. codes: *** p<0.001  ** p<0.01  * p<0.05")