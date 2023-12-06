#!/usr/bin/env pypy3

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
seeds = list(seeds)

for i in range(0, len(seeds), 2):
    print(f"=== Seed {i} of {len(seeds)} ===")
    for seed in range(seeds[i], seeds[i + 1] + seeds[i]):
        test = seeds[i]
        for k in m:
            for v in m[k]:
                if v["source"] <= test < v["source"] + v["range"]:
                    test += v["offset"]
                    break
                mmin = min(mmin, test)
print(mmin)
