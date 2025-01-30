import heapq
from collections import Counter, namedtuple

# Define a Huffman Node
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):  # Custom comparator for priority queue
        return self.freq < other.freq

def build_huffman_tree(text):
    """Builds the Huffman Tree from the input text."""
    if not text:
        return None
    
    # Step 1: Calculate frequency of each character
    frequency = Counter(text)

    # Step 2: Create a priority queue (min-heap) with leaf nodes
    heap = [Node(char, freq, None, None) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Step 3: Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)   # Smallest frequency node
        right = heapq.heappop(heap)  # Second smallest frequency node
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0]  # Root of the Huffman Tree

def generate_huffman_codes(node, prefix="", code_dict={}):
    """Generates Huffman Codes using DFS traversal of the tree."""
    if node is None:
        return
    
    if node.char is not None:  # Leaf node (has a character)
        code_dict[node.char] = prefix

    generate_huffman_codes(node.left, prefix + "0", code_dict)
    generate_huffman_codes(node.right, prefix + "1", code_dict)

    return code_dict

def encode_text(text, code_dict):
    """Encodes the input text using Huffman codes."""
    return "".join(code_dict[char] for char in text)

def decode_text(encoded_text, root):
    """Decodes the Huffman encoded text using the Huffman Tree."""
    decoded_text = []
    current = root

    for bit in encoded_text:
        current = current.left if bit == "0" else current.right

        if current.char is not None:  # Leaf node
            decoded_text.append(current.char)
            current = root  # Reset to root for next character

    return "".join(decoded_text)

# Example usage
if __name__ == "__main__":
    text = "huffman coding algorithm"
    print("Original Text:", text)

    huffman_tree = build_huffman_tree(text)
    huffman_codes = generate_huffman_codes(huffman_tree)

    print("\nHuffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

    encoded_text = encode_text(text, huffman_codes)
    print("\nEncoded Text:", encoded_text)

    decoded_text = decode_text(encoded_text, huffman_tree)
    print("\nDecoded Text:", decoded_text)
