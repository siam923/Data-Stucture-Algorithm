import sys

def frequency(word):
    freqs = {}
    for char in word:
        freqs[char] = freqs.get(char, 0) + 1
    return freqs

def sortFreq(freqs):
    letters = freqs.keys()
    tuples = []
    for l in letters:
        tuples.append((freqs[l], l))
    tuples.sort()
    return tuples

def get_key(lst): # Used as key in sorted function
    return lst[0]

def build_trees(tuples):
    while len(tuples) > 1:
        least_two = tuples[0:2]
        rest = tuples[2:]
        freq_sum = least_two[0][0] + least_two[1][0]
        tuples = rest + [(freq_sum, least_two)]
        sorted(tuples, key=get_key)
    return tuples[0]

def trim_tree (tree) :
     # Trim the freq counters off, leaving just the letters
    p = tree[1]    # ignore freq count in [0]
    if type(p) == str :
        return p     # if just a leaf, return it
    else :
        return (trim_tree(p[0]), trim_tree(p[1]))# trim left then right and recombine

def assignCodes (node, pat='') :
    global codes
    if type(node) == type("") :
        codes[node] = pat                # A leaf. set its code
    else  :
        assignCodes(node[0], pat+"0")    # Branch point. Do the left branch
        assignCodes(node[1], pat+"1")    # then do the right branch.

def encode (word) :
    global codes
    binary_output = ""
    for ch in word:
        binary_output += codes[ch]
    return binary_output


def decode (tree, str) :
    output = ""
    p = tree
    for bit in str :
        if bit == '0' :
            p = p[0]     # Head up the left branch
        else:
            p = p[1]     # or up the right branch
        if type(p) == type("") :
            output += p     # found a character. Add to output
            p = tree        # and restart for next character
    return output

def huffman_encoding(data):
    if len(data) < 1:
        raise Exception('data is empty')
        return

    global codes
    freqs = frequency(data)
    tuples = sortFreq(freqs)
    tree = build_trees(tuples)
    trim = trim_tree(tree)
    if type(tree[1]) == str:
        codes[tree[1]] = '0'
    else:
        assignCodes(trim)
    return encode(data), trim

def huffman_decoding(data,tree):
    return decode(tree, data)

def huffman_decoding(data,tree):
    return decode(tree, data)


def build_test_case(a_great_sentence, test_no=1):
    print("Test Case: ", test_no)

    data_size = sys.getsizeof(a_great_sentence)

    print("The size of the data is: {}".format(data_size))
    print("The content of the data is: {}".format(a_great_sentence))

    try:
        encoded_data, tree = huffman_encoding(a_great_sentence)
    except Exception as e:
        print(str(e))
        return
    encoded_data_size = sys.getsizeof(int(encoded_data, base=2))

    print("The size of the encoded data is: {}".format(encoded_data_size))
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    decoded_data_size = sys.getsizeof(decoded_data)

    print ("The size of the decoded data is: {}".format(decoded_data_size))
    print ("The content of the decoded data is: {}".format(decoded_data))
    if (data_size == decoded_data_size) and \
            (a_great_sentence == decoded_data):
        print('pass\n')
    else:
        print('fail\n')

if __name__ == '__main__':

    codes = {}
    build_test_case("The bird is the word", 1)
    #pass
    build_test_case("a", 2)
    #pass 
    build_test_case("", 3)
    #data is empty
    build_test_case("aaaa", 4)
    #pass
