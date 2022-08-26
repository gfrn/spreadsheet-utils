import pylightxl

b = list(pylightxl.readxl("a.xlsx").ws("PVs MBTemp").rows)
a = list(pylightxl.readxl("b.xlsx").ws("PVs MBTemp").rows)

ips = {}
current_ips = []

for row in a:
    ips[f"{row[1]} - {row[3]}"] = row[6:]

for row in b:
    name = f"{row[1]} - {row[3]}"
    current_ips.append(name)
    if name in ips:
        if row[6:] != ips[name]:
            diff_new = ""
            diff_old = ""
            for i, cell in enumerate(row[6:]):
                if cell != ips[name][i]:
                    try:
                        pad_new = (
                            " " * (len(ips[name][i]) - len(cell))
                            if len(ips[name][i]) - len(cell) > 0
                            else ""
                        )
                        pad_old = (
                            " " * (len(cell) - len(ips[name][i]))
                            if len(ips[name][i]) - len(cell) < 0
                            else ""
                        )

                        diff_new += f"\033[33m{cell + pad_new}\033[39m "
                        diff_old += f"\033[35m{ips[name][i] + pad_old}\033[39m "
                    except TypeError:
                        pass
                else:
                    diff_new += f"{cell} "
                    diff_old += f"{ips[name][i]} "

            print(f"{name}: {diff_new}")
            print(f"Original{(len(name)-8)*' '}: {diff_old}")
            print("----------------------------------------")
    else:
        try:
            print(f"\033[32m{name}: {' '.join(row[6:])}\033[39m")
            print("--------------------------------------------")
        except TypeError:

            print(row[6:])

for ip in ips.keys():
    if ip not in current_ips:
        try:
            print(f"\033[31m{ip}: {' '.join(ips[ip])}\033[39m")
            print("------------------------------------------")
        except TypeError:
            pass
