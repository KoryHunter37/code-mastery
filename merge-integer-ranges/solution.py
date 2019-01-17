def merge_ranges(input_range_list):
    changes_found = True
    while changes_found:
        changes_found = False
        for i in range(0, len(input_range_list)):
            curr = input_range_list[i]
            for j in range(i + 1, len(input_range_list)):
                other = input_range_list[j]

                curr_range = [x for x in range(curr.lower_bound, curr.upper_bound + 1)]
                other_range = [y for y in range(other.lower_bound, other.upper_bound + 1)]
                new_range = list(set(curr_range + other_range))

                intersection = list(set(curr_range).intersection(set(other_range)))

                valid = False
                if len(intersection) > 0 and ((intersection[0] >= curr.lower_bound and intersection[-1] <= other.upper_bound) or (intersection[0] >= other.lower_bound and intersection[-1] <= curr.upper_bound)):
                    valid = True

                if valid:
                    new_range = Range(new_range[0], new_range[-1])
                    input_range_list[i] = new_range
                    input_range_list[j] = new_range
                    input_range_list = list(set(input_range_list))
                    changes_found = True
                    break
            if changes_found:
                break

    return input_range_list


