import numpy as np
import statsmodels.api as sm
fn = input ("Please enter the filename: ")
f = open(fn, "r")

X = [
[1, 0],
[2, 0],
[4, 0],
[8, 0],
[1, 100],
[2, 100],
[4, 100],
[8, 100],
[1, 400],
[2, 400],
[4, 400],
[8, 400],
[1, 800],
[2, 800],
[4, 800],
[8, 800]
]

found = 0
f_first = 0
while found == 0:
    line = f.readline()
    if len(line.split()) > 0 and line.split()[0] == "Measurement:":
        found = 1
        if line.split()[1] == "tpdf":
            f_first = 1
f.readline()
tpdf = []
tpdr = []
for i in range (16):
    if f_first == 1:
        tpdf.append(float(f.readline().split()[1])*1e12)
    else:
        tpdr.append(float(f.readline().split()[1])*1e12)
f.readline()
f.readline()
f.readline()
for i in range (16):
    if f_first == 1:
        tpdr.append(float(f.readline().split()[1])*1e12)
    else:
        tpdf.append(float(f.readline().split()[1])*1e12)

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(np.array(X), np.array(tpdf))
print ("tpdf(ps) = ", reg.coef_[0], " x load(multiple of Cinv) + ", reg.coef_[1], " x slew (ps) + ", reg.intercept_)
reg2 = LinearRegression()
reg2.fit(np.array(X), np.array(tpdr))
print ("tpdr(ps) = ", reg2.coef_[0], " x load(multiple of Cinv) + ", reg2.coef_[1], " x slew(ps) + ", reg2.intercept_)
