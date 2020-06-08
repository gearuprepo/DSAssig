# Huffman's Coding

The implementation is using minheap.

* huffman_encoding - O(n) = n^2 + 6n
> * Construct Frequency map -> O(n)=n
> * Construct priority queue for frequency map -> O(n)=n
> * Encode tree process -> O(n) = n^2 + 2n
> * form coding map O(n) = n
> * Code the input string O(n) = n

* huffman_decoding - O(n) = nlogn

Review Comment Fixes
--------------------
1. Boundary condition issues fixed
2. Review 2 - Added test cases for the rest of the conditions.