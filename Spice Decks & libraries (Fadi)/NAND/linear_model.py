import numpy as np
import statsmodels.api as sm
fn = input ("Please enter the filename: ")
f = open(fn, "r")
output = open("output.txt", "w")

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
output.write ("tpdf(ps): \n")
# output.write ("slw\\ld\t")
# for i in [1, 2, 4, 8]:
#     output.write (str(i))
#     output.write("\t")
# output.write("\n")
delays = [0, 100, 400, 800]
for i in range(4):
    # output.write(str(delays[i]))
    # output.write("\t")
    for j in range(4):
        output.write(str(tpdf[4*i+j]))
        output.write("\t")
    output.write("\n")
output.write("\n")
print("tpdf(ps) = ", reg.coef_[0], " x load(Cinv) + ", reg.coef_[1], " x slew (ps) + ", reg.intercept_)

output.write ("tpdr(ps): \n")
# output.write ("slw\\ld\t")
# for i in [1, 2, 4, 8]:
#     output.write (str(i))
#     output.write("\t")
output.write("\n")
for i in range(4):
    # output.write(str(delays[i]))
    # output.write("\t")
    for j in range(4):
        output.write(str(tpdr[4*i+j]))
        output.write("\t")
    output.write("\n")
output.write("\n")
reg2 = LinearRegression()
reg2.fit(np.array(X), np.array(tpdr))
print ("tpdr(ps) = ", reg2.coef_[0], " x load(Cinv) + ", reg2.coef_[1], " x slew(ps) + ", reg2.intercept_)
print ("Delay tables written to file output.txt")
