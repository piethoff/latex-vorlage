import numpy as np
import re
import sys

data = np.genfromtxt(str(sys.argv[1]), unpack=True)

def columnsettings(a):

	vz = ""
	lenvk = 0
	lennk = 0
	lenunc = 0

	for i in a:
		if i < 0:
			vz = "-"
		if len(str(int(i))) > lenvk:
			lenvk = len(str(int(i)))
		if len(str(i).split(".")[1]) > lennk:
			lennk = len(str(i).split(".")[1])

	return "S[table-format=" + vz + str(lenvk) + "." + str(lennk) + "]"


file = open(str(sys.argv[1]), "r")
caption = file.readline()
kopfzeile = file.readline()
file.close()

out = open("build/" + str(sys.argv[1])[8:-4] + ".tex", "w")
out.write("\\begin{table}\n")
out.write("\t\\caption{")
if (caption[0] == "#") and (caption[1] == "#"):
	out.write(caption[2:-1])
else:
	kopfzeile = caption

out.write(".}\n")
out.write("\t\\label{tab:" + str(sys.argv[1])[8:-7] + "}\n")
out.write("\t\\centering\n")
out.write("\t\\begin{tabular}{")
if data.ndim == 1:
	out.write(columnsettings(data))
else:
	for i in range(int(data.size/data[0].size)):
		out.write(columnsettings(data[i]) + " ")

out.write("}\n")
out.write("\t\t\\toprule\n")
if(kopfzeile[0] == "#"):
    kopfzeile = [x.strip() for x in kopfzeile[1:].split("\t")]
#   for i in range(len(kopfzeile) -1):
    for i in range(min(len(kopfzeile), int(data.size/data[0].size))):
        out.write("\t\t{" + str(kopfzeile[i]) + "} & \n")
    out.write("\t\t{" + str(kopfzeile[-1]) + "} \\\\\n")
else:
    for i in range(int(data.size/data[0].size)-1):
        out.write("\t\t{$$} &")
    out.write("\t{$$} \\\\\n")

out.write("\t\t\\midrule\n")

for j in range(data[0].size):
    out.write("\t\t")
    for i in range(int(round(data.size/data[0].size)) -1):
        out.write(str(data[i][j]) + "\t& ")
    out.write(str(data[-1][j]) + "\t\\\\\n")

out.write("\t\t\\bottomrule\n")
out.write("\t\\end{tabular}\n")
out.write("\\end{table}\n")
