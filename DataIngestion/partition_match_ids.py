def get_all_matches():
    all_match_ids = []

    with open('match_ids.txt', 'r') as f:
        all_match_ids = [x.strip() for x in f.readlines()] 

    print(f"Read {len(all_match_ids)} players")

    return all_match_ids


def write_to_file(match_ids, partition_id):
    # write to disk
    with open(f'match_ids_partition_{partition_id}.txt', 'w+') as f:
        for match_id in match_ids:
            f.write("{}\n".format(match_id))


if __name__ == "__main__":
    all_match_ids = get_all_matches()
    total_count = len(all_match_ids)

    parition_count = 10
    for idx in range(0, 10): # 0 - 9
        if idx == 9:
            # print(f"{total_count // 10 * idx}:end")
            write_to_file(
                all_match_ids[
                    total_count // 10 * idx
                    :
                ],
                idx + 1
            )

            continue

        if idx == 0:
            # print(f"0:{total_count // 10}")
            write_to_file(
                all_match_ids[
                    :
                    total_count // 10
                ],
                idx + 1
            )

            continue

        # print(f"{total_count // 10 * idx}:{total_count // 10 * idx + (total_count // 10)}")
        write_to_file(
            all_match_ids[
                total_count // 10 * idx:
                total_count // 10 * idx + (total_count // 10)
            ],
            idx + 1
        )

