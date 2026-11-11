# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 11Bonus
# Date:         10 November 2026


def is_valid(passport):
    pairs = passport.split()
    my_dict = {}

    for pair in pairs:
        parts = pair.split(":")
        if len(parts) == 2:
            my_dict[parts[0]] = parts[1]

    # all required fields present (ecl is optional)
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "pid", "cid"]
    for r in required:
        if r not in my_dict:
            return False

    # byr
    byr = my_dict["byr"]
    if not (len(byr) == 4 and byr.isdigit()):
        return False
    if not (1920 <= int(byr) <= 2007):
        return False

    # iyr
    iyr = my_dict["iyr"]
    if not (len(iyr) == 4 and iyr.isdigit()):
        return False
    if not (2013 <= int(iyr) <= 2023):
        return False

    # eyr
    eyr = my_dict["eyr"]
    if not (len(eyr) == 4 and eyr.isdigit()):
        return False
    if not (2023 <= int(eyr) <= 2033):
        return False

    # hgt
    hgt_num = my_dict["hgt"][:-2]
    units = my_dict["hgt"][-2:]
    if not hgt_num.isdigit():
        return False
    hgt = int(hgt_num)
    if units == "cm":
        if not (150 <= hgt <= 193):
            return False
    elif units == "in":
        if not (59 <= hgt <= 76):
            return False
    else:
        return False

    # hcl
    hcl = my_dict["hcl"]
    if not (len(hcl) == 7 and hcl[0] == "#"):
        return False
    characters = "0123456789abcdef"
    for j in range(1, 7):
        if hcl[j] not in characters:
            return False

    # pid
    pid = my_dict["pid"]
    if not (len(pid) == 9 and pid.isdigit()):
        return False

    # cid
    cid = my_dict["cid"]
    if not (len(cid) == 3 and cid.isdigit() and cid[0] != "0"):
        return False

    return True


file_name = input("Enter the name of the file: ")
count = 0
outfile = open("valid_passports2.txt", "w")

with open(file_name, "r") as file:
    data = file.read()
    passports = data.strip().split("\n\n")

    for i in range(len(passports)):
        if is_valid(passports[i]):
            if count > 0:
                outfile.write("\n\n")
            count += 1
            outfile.write(passports[i])

print("There are", count, "valid passports")
outfile.close()
