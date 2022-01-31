import csv
import sys


def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py CSV file and TXT file required")
    # dictionary to store database
    data = []

    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        # if using databse/small
        if sys.argv[1] == "databases/small.csv":
            for row in reader:
                row["AGATC"] = int(row["AGATC"])
                row["AATG"] = int(row["AATG"])
                row["TATC"] = int(row["TATC"])
                data.append(row)
        # else large database
        else:
            for row in reader:
                row["AGATC"] = int(row["AGATC"])
                row["TTTTTTCT"] = int(row["TTTTTTCT"])
                row["AATG"] = int(row["AATG"])
                row["TCTAG"] = int(row["TCTAG"])
                row["GATA"] = int(row["GATA"])
                row["TATC"] = int(row["TATC"])
                row["GAAA"] = int(row["GAAA"])
                row["TCTG"] = int(row["TCTG"])
                data.append(row)
    # string to store sequences
    DNA = ""
    with open(sys.argv[2], "r") as file:
        for row in file:
            DNA = row
    # when returning no match
    result = ""
    # check which database were in
    if sys.argv[1] == "databases/small.csv":
        AGATC = count_STR("AGATC", DNA)
        AATG = count_STR("AATG", DNA)
        TATC = count_STR("TATC", DNA)
        for name in data:
            if AGATC == name["AGATC"] and AATG == name["AATG"] and TATC == name["TATC"]:
                return print(name["name"])
            else:
                result = "No match"
        print(result)
    else:
        AGATC = count_STR("AGATC", DNA)
        AATG = count_STR("AATG", DNA)
        TATC = count_STR("TATC", DNA)
        TTTTTTCT = count_STR("TTTTTTCT", DNA)
        TCTAG = count_STR("TCTAG", DNA)
        GATA = count_STR("GATA", DNA)
        GAAA = count_STR("GAAA", DNA)
        TCTG = count_STR("TCTG", DNA)
        for name in data:
            if (AGATC == name["AGATC"] and AATG == name["AATG"] and TATC == name["TATC"] and TTTTTTCT == name["TTTTTTCT"] and
                    TCTAG == name["TCTAG"] and GATA == name["GATA"] and GAAA == name["GAAA"] and TCTG == name["TCTG"]):
                return print(name["name"])
            else:
                result = "No match"
        print(result)


# count the times STR repeats in a given string
def count_STR(string, DNA):
    s = string
    count = 0
    while s in DNA:
        count += 1
        s += string
    return count

main()

