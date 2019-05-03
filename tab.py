"""
Usage:
Expected .txt file format:
##[caption]
#[colum1]\t[colum2]…
[[data]]

Expected location:
content/[label]tab.txt

"""
import numpy as np
import re
import sys

data = np.genfromtxt(str(sys.argv[1]), unpack=True, dtype="str", autostrip=True)

def columnsettings(a):
	vz = ""
	lenvk = 1
	lennk = 0
	lenexp = 0
	lenunc = 0

	for i in a:
		if re.search("-", i):
			vz = "-"
		x = re.search("\d+(?=\.)", i)
		if x:
			if len(x.group()) > lenvk:
				lenvk = len(x.group())
		else:
			x = re.search("\d+", i)
			if x:
				if len(x.group()) > lenvk:
					lenvk = len(x.group())
		x = re.search("(?<=\.)\d+", i)
		if x:
			if len(x.group()) > lennk:
				lennk = len(x.group())
		x = re.search("(?<=e)\d+", i)
		if x:
			if len(x.group()) > lenexp:
				lenexp = len(X.group())
		x = re.search(r"(?<=[\\pm, ±])\d+", i)
		if x:
			if len(x.group)+1 > lenunc:
				lenunc = len(x.group)+1
			
	if lenunc == 0:
		return "S[table-format=" + vz + str(lenvk) + "." + str(lennk) + "e" + str(lenexp) + "]"
	else:
		return "S[table-format=" + vz + str(lenvk) + "." + str(lennk) + "e" + str(lenexp) + str(lenunc) +"]"

file = open(str(sys.argv[1]), "r")
caption = file.readline()
kopfzeile = file.readline()
file.close()

out = open("build/" + str(sys.argv[1])[8:-7] + ".tex", "w")
out.write("\\begin{table}[H]\n")
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

#
#~~~ strings manuell auf gleiche Länge bringen -> 0…0 ergänzen, evtl .0…0
#

out.write("}\n")
out.write("\t\t\\toprule\n")
if(kopfzeile[0] == "#"):
    kopfzeile = [x.strip() for x in kopfzeile[1:].split("\t")]
#   for i in range(len(kopfzeile) -1):
    for i in range(min(len(kopfzeile), int(data.size/data[0].size)) - 1):
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
        out.write(data[i][j] + "\t& ")
    out.write(data[-1][j] + "\t\\\\\n")

out.write("\t\t\\bottomrule\n")
out.write("\t\\end{tabular}\n")
out.write("\\end{table}\n")
out.write("\\noindent\n")
