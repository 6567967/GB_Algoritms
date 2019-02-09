import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_code(s: str) -> dict:
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = dict()
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(encoded: str, code: dict) -> str:
    decode = dict()
    for char, enc in code.items():
        decode[enc] = char

    spam = ''
    decoded_string = ''
    for i in encoded:
        spam = f'{spam}{i}'
        if decode.get(spam) is not None:
            decoded_string = f"{decoded_string}{decode[spam]}"
            spam = ''

    return decoded_string


def huffman_encode(encoded_string: str, code: dict) -> str:
    return "".join(code[ch] for ch in encoded_string)


def main():
    s = input('Input string for encoding: ')
    code: dict = huffman_code(s)
    print(f'Huffman code: {code}')
    encoded: str = huffman_encode(s, code)
    print(f'{len(code)} symbols ({list(code.keys())} coded by '
          f'{len(encoded)} bits:')
    print(encoded)
    # print(huffman_decode(encoded, code))


def test():
    import random, string
    for i in range(100):
        eggs = ''.join(random.choices(string.ascii_lowercase,
                                      k=random.randint(0, 100)))
        code = huffman_code(eggs)
        assert huffman_decode(huffman_encode(eggs, code), code) == eggs
        print(f'test {i + 1} for {eggs} OK')


if __name__ == "__main__":
    main()
    # test()
