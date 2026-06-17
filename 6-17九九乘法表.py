# for i in range(1,10):
#     for n in range(1,10):
#         if i>=n:
#           print(f"{n}*{i}={i * n}", end="   ")
#
#     print("")

for i in range(1,10):
    for n in range(1, i + 1):
        print(f"{n}*{i}={i * n}", end="   ")

    print("")