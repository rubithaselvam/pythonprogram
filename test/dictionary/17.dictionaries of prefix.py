def group_by_prefix(dict):
    result = {}
    for key, value in dict.items():
        result.setdefault(key.split('_')[0], []).append(value)
    return result

# Example dictionary
dict = {"cs_1": 10, "cs_2": 15, "tfd_1": 20, "tfd_2": 25, "biotech_1": 30}

# Grouping values
print(group_by_prefix(dict))
