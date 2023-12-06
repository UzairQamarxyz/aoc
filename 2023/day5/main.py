#!/usr/bin/env python3

input_file = "input"

seeds, *blocks = open(input_file).read().strip().split("\n\n")
seeds = map(int, seeds.split(": ")[1].split(" "))

m = {}

for block in blocks:
    category_name, *dsr_list = block.split("\n")
    category_name = category_name.replace(" map:", "")
    m[category_name] = []
    for i, dsr in enumerate(dsr_list):
        dsr_destination, dsr_source, dsr_range = map(int, dsr.split(" "))
        m[category_name].append(
            {
                "destination": dsr_destination,
                "source": dsr_source,
                "range": dsr_range,
                "offset": dsr_destination - dsr_source,
            }
        )

mmin = 9999999999999999
test_list = []
for seed in seeds:
    test = seed
    for k in m:
        print(f"\n=== Seed No. {seed} | {k} ===")
        for v in m[k]:
            print(v)
            if v["source"] <= test < v["source"] + v["range"]:
                test += v["offset"]
                print(test)
                break
    mmin = min(mmin, test)
print(mmin)
