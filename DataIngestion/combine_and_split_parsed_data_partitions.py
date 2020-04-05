Desert_Main = "Desert_Main"
DihorOtok_Main = "DihorOtok_Main"
Erangel_Main = "Erangel_Main"
Baltic_Main = "Baltic_Main"
Range_Main = "Range_Main"
Savage_Main = "Savage_Main"
Summerland_Main = "Summerland_Main"


def read_partition_data(partition_number):
    res = []

    with open(f"data_partitions/parsed_data_partition_{partition_number}.txt", "r") as f:
        res = [x.strip().split(",") for x in f.readlines()]

    print(f"Read {len(res)} matches")

    return res

def write_to_file(match_data, map_name):
    with open(f"parsed_data/{map_name}_data.txt", "a+") as f:
        for match in match_data:
            f.write(f"{','.join(match)}\n")

def write_all(match_data):
    with open(f"parsed_data/combined.txt", "a+") as f:
        for match in match_data:
            f.write(f"{','.join(match)}\n")

def main():
    partition_numbers = range(1, 11)
    desert = []
    dihor = []
    erangel = []
    baltic = []
    range_ = []
    savage = []
    summerland = []
    all_kills = []

    for partition_number in partition_numbers:
        print(f"Currently on partition {partition_number}")
        parsed_content = read_partition_data(partition_number)
        desert.clear()
        dihor.clear()
        erangel.clear()
        baltic.clear()
        range_.clear()
        savage.clear()
        summerland.clear()
        all_kills.clear()
        count = 0

        for kill in parsed_content:
            map_name = kill[1]
            all_kills.append(kill)

            if map_name == Desert_Main:
                desert.append(kill)
            elif map_name == DihorOtok_Main:
                dihor.append(kill)
            elif map_name == Erangel_Main:
                erangel.append(kill)
            elif map_name == Baltic_Main:
                baltic.append(kill)
            elif map_name == Range_Main:
                range_.append(kill)
            elif map_name == Savage_Main:
                savage.append(kill)
            elif map_name == Summerland_Main:
                summerland.append(kill)
            else:
                print(f"map not found {map_name} on line {count}")
                print(kill)

            count += 1

        # Write to file
        write_to_file(desert, Desert_Main)
        write_to_file(dihor, DihorOtok_Main)
        write_to_file(erangel, Erangel_Main)
        write_to_file(baltic, Baltic_Main)
        write_to_file(range_, Range_Main)
        write_to_file(savage, Savage_Main)
        write_to_file(summerland, Summerland_Main)
        write_all(all_kills)
            
if __name__ == "__main__":
    main()
