def reverse(to_rev):

    # convert string to a list
    split_x = to_rev.split(" ")
    # store reversed words
    reverse_x = []
    # itarate each world in split_x list, and append to reverse_x list
    for i in split_x:
        reverse_x.append(i[::-1])

        # convert individual word in reverse_x list to a string

    x_reverse=" ".join(reverse_x)
    return x_reverse

print(reverse("The quick brown fox"))

# advanced way >>> list comprehension

# y=" ".join([i[::-1] for i in x.split(" ")])




