def oxford_comma(items : list):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        copy = items
        popped_item = copy.pop()
        return f"{', '.join(copy)}, and {popped_item}"

oxford_comma(['poo', 'pee', 'penis'])