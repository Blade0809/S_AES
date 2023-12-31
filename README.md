# S_AES
## Homework Report
### Level 1: basic test
GUI: 

**Since 16-bit binary is too long in sight, we use 4 character hexadecimal instead.**

<img width="928" alt="截屏2023-10-28 21 59 01" src="https://github.com/Blade0809/S_AES/assets/125954865/2d1a9113-a569-47a6-b4fe-05e70f7b2240">

1. Input the correct plaintext and key, we can encrypt and get the ciphertext.

<img width="928" alt="截屏2023-10-28 22 04 07" src="https://github.com/Blade0809/S_AES/assets/125954865/dcda0e73-72f3-4690-b2ac-80e89682f756">

2. Input the correct ciphertext and key, we can decrypt and get the plaintext.

<img width="928" alt="截屏2023-10-28 22 14 39" src="https://github.com/Blade0809/S_AES/assets/125954865/33fa14f4-e27f-4009-b2bc-2a67e5adfc74">

We can see that the plaintext we get through decrypt is the same as the original one, thus **the encrypt and the decrypt are inverse operations**.

3. If either the key or the plain/cipher is not correspond to the correct length, it will return an error.

<img width="928" alt="截屏2023-10-28 22 32 52" src="https://github.com/Blade0809/S_AES/assets/125954865/f42335e0-1d3f-48e3-864b-cc402092fcb6">

### Level 2: cross test

![WechatIMG108](https://github.com/Blade0809/S_AES/assets/125954865/7da45de4-e5e0-49b1-b3b9-13180b550486)

We transform binary to hexadecimal and find that it is correct.

### Level 3: ASCII

1. Input the correct plaintext and key, we can encrypt and get the ciphertext.

<img width="928" alt="截屏2023-10-28 22 11 01" src="https://github.com/Blade0809/S_AES/assets/125954865/3124f794-cce2-43b4-991e-e8de51e7ee84">

2. Input the correct ciphertext and key, we can decrypt and get the plaintext.

<img width="928" alt="截屏2023-10-28 22 13 57" src="https://github.com/Blade0809/S_AES/assets/125954865/0657a2e8-3508-4663-b51c-92208ee45477">

We can see that the plaintext we get through decrypt is the same as the original one, thus **the encrypt and the decrypt are inverse operations**.

### Level 4: Muti-encrypt

In S-AES (Simplified Advanced Encryption Standard), multiple encryption, also known as multi-round encryption, is a process where the data undergoes a series of encryption operations using the same or different keys. This technique enhances the security of the encrypted data by applying the encryption algorithm multiple times consecutively.

In each round of S-AES encryption, the data is subjected to a series of operations, including substitution, permutation, and mixing. These operations are performed on the data using a combination of key-dependent transformations. By repeating these rounds, the data undergoes a cascade of these operations, making it increasingly complex for an attacker to reverse-engineer or decrypt the original information.

The multiple encryption process in S-AES significantly increases the computational complexity required to break the encryption, thereby providing a higher level of security against various cryptographic attacks. It is a fundamental strategy to safeguard sensitive information in scenarios where strong encryption is imperative.

#### Double Encrypt

1. Input the correct plaintext and key, we can double encrypt and get the ciphertext.

<img width="928" alt="截屏2023-10-28 22 18 12" src="https://github.com/Blade0809/S_AES/assets/125954865/69c98f30-0a43-481b-bd65-5b4735f7dd40">

2. Input the correct ciphertext and key, we can double decrypt and get the plaintext.

<img width="928" alt="截屏2023-10-28 22 18 38" src="https://github.com/Blade0809/S_AES/assets/125954865/02248094-a020-46d8-b780-818f86be347e">

#### Attack the Middle

In the context of S-AES double encryption, the "Meet-in-the-Middle" attack is a cryptanalysis technique that exploits the vulnerability arising from encrypting a plaintext with two independent keys. Here's an explanation of the Meet-in-the-Middle attack in S-AES double encryption:

Double Encryption Process:

The plaintext is first encrypted with Key 1 to produce an intermediate ciphertext.
The intermediate ciphertext is then decrypted with Key 2 to produce the final ciphertext.
Meet-in-the-Middle Attack:

The attacker generates a list of all possible intermediate ciphertexts by encrypting the plaintext with all possible keys (2^16 in the case of 16-bit S-AES).

The attacker also generates a list of all possible results from decrypting the intermediate ciphertext with all possible keys (2^16 again).

Next, the attacker compares the lists to find a matching pair. This means they have found a combination where the encryption and decryption operations cancel each other out, resulting in the original intermediate ciphertext.

Finding Key Combinations:

Once a matching pair is found, the attacker has identified Key 1 and Key 2. This is because Key 1 was used to encrypt the plaintext, and Key 2 was used to decrypt the intermediate ciphertext.

The attacker can then use the identified Key 1 and Key 2 to decrypt the final ciphertext and recover the original plaintext.

Input the plain and the cipher, we can get the possible keys and the cracking time.

<img width="928" alt="截屏2023-10-29 10 49 37" src="https://github.com/Blade0809/S_AES/assets/125954865/19df3a19-5a11-4e0c-8c57-4e9b7e561e36">

#### Tribble Encrypt

We use 32-bit key(k1+k2) to tribble encrypt.

1. Input the correct plaintext and key, we can double encrypt and get the ciphertext.

<img width="928" alt="截屏2023-10-29 10 26 23" src="https://github.com/Blade0809/S_AES/assets/125954865/28007f32-801a-4033-8e3a-f6a348cb34a4">

2. Input the correct ciphertext and key, we can double decrypt and get the plaintext.

<img width="928" alt="截屏2023-10-29 10 26 47" src="https://github.com/Blade0809/S_AES/assets/125954865/8407ca9e-3958-48af-a8f9-bae2445a5153">

### Level 5: Working Mode

Cipher Block Chaining (CBC) is a widely used mode of operation for block ciphers, including in the context of the Simplified Advanced Encryption Standard (S-AES). Here's an explanation of how CBC encryption works in S-AES:

CBC mode involves the following steps:

Initialization Vector (IV) Selection: A random IV is generated. The IV is XORed with the first block of plaintext before encryption. This step ensures that even if the same plaintext is encrypted multiple times, the resulting ciphertext will be different due to the unique IV.

Dividing into Blocks: The plaintext message is divided into blocks of a fixed size (in S-AES, this is 16 bits or 2 bytes).

XOR with Previous Block: Each plaintext block (after the first one) is XORed with the ciphertext of the previous block.

Encryption: The XORed result is then encrypted using the S-AES algorithm. The encryption process in S-AES involves substitution, permutation, and mixing operations based on the key.

Ciphertext Output: The resulting ciphertext from each encryption operation becomes the input for the XOR operation in the next round.

Final Ciphertext: The final ciphertext is a series of blocks, each dependent on the encryption of the previous block. The IV, if used, is typically sent along with the ciphertext.

CBC mode ensures that even if identical blocks of plaintext are encrypted, the output will be different due to the XOR operation with the previous ciphertext block. This provides an additional layer of security.

1. Input the correct plaintext and key, we can double encrypt and get the ciphertext.

<img width="928" alt="截屏2023-10-29 10 28 06" src="https://github.com/Blade0809/S_AES/assets/125954865/e85a2173-8dd9-4acb-a8be-806b6c250234">

2. Input the correct ciphertext and key, we can double decrypt and get the plaintext.

<img width="928" alt="截屏2023-10-29 10 28 26" src="https://github.com/Blade0809/S_AES/assets/125954865/ac94bba2-862b-44f4-bceb-11d93893d46e">

3. If we change the order of the plain, for example the first 8 characters, we can see that the cipher is totally different, thus satisfies the CBC.

<img width="928" alt="截屏2023-10-29 10 42 07" src="https://github.com/Blade0809/S_AES/assets/125954865/cde4da7f-bd43-4fdb-b9a4-54ce5a42239c">

## Modules

We introduce some important modules in the algorithm.

### Encrypt

The Simplified Advanced Encryption Standard (S-AES) is a simplified version of the AES encryption algorithm. Here is an explanation of the encryption process in S-AES:

Key Expansion:

S-AES uses an 16-bit key. The first step is to expand this 16-bit key into a set of round keys. In this simplified version, the round keys are derived directly from the original key.

There some other functions such as sub_bytes, shift_rows and so on.

```python
def encrypt(plaintext, master_key):
    round_keys = generate_round_keys(master_key)
    cipher = ''
    for i in range(4):
        if plaintext[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
            return 'error, check the input!'
    if len(plaintext) != 4 or len(master_key) != 4:
        return 'error, check the input!'
    for i in range(int(len(plaintext) / 4)):
        tmp_cipher = ''
        tmp_plain = plaintext[4 * i:4 * i + 4]
        tmp_matrix = get_state_matrix(tmp_plain)
        tmp_matrix = add_round_key(tmp_matrix, round_keys[0])

        tmp_matrix = sub_bytes(tmp_matrix, s_box)
        tmp_matrix = shift_rows(tmp_matrix)
        tmp_matrix = mix_columns(tmp_matrix)
        tmp_matrix = add_round_key(tmp_matrix, round_keys[1])

        tmp_matrix = sub_bytes(tmp_matrix, s_box)
        tmp_matrix = shift_rows(tmp_matrix)
        tmp_matrix = add_round_key(tmp_matrix, round_keys[2])

        tmp_cipher += b_to_x(tmp_matrix[0])
        tmp_cipher += b_to_x(tmp_matrix[2])
        tmp_cipher += b_to_x(tmp_matrix[1])
        tmp_cipher += b_to_x(tmp_matrix[3])
        cipher += tmp_cipher
    return cipher
```

### Attack the Middle

We simplify the algorithm by using more space of list to save the time.

```python
def attack_the_middle(plain, cipher):
    start_time = time.time()
    keys = []
    mid_1 = {}
    mid_2 = {}
    for i in range(int(math.pow(2, 16))):
        key_1 = bin(i)[2:].zfill(16)
        p_1 = encrypt(plain, b_to_x(key_1))
        mid_1[p_1] = key_1
    for j in range(int(math.pow(2, 16))):
        key_2 = bin(j)[2:].zfill(16)
        p_2 = decrypt(cipher, b_to_x(key_2))
        mid_2[p_2] = key_2
    for mid in mid_1.keys():
        if mid in mid_2.keys():
            keys.append(b_to_x(mid_1[mid] + mid_2[mid]))
    end_time = time.time()
    running_time = end_time - start_time
    return keys
```

### Cipher Block Chaining

We set IV as static '1010101010101010'.

```python
def cipher_block_chaining_encrypt(long_plain_text, master_key, IV):
    cipher = ''
    for i in range(int(len(long_plain_text) / 4)):
        if i == 0:
            cipher += encrypt(b_to_x(binary_xor(IV, x_to_b(long_plain_text[:4]))), master_key)
        else:
            cipher += encrypt(
                b_to_x(binary_xor(x_to_b(cipher[4 * i - 4:4 * i]), x_to_b(long_plain_text[4 * i:4 * i + 4]))),
                master_key)
    return cipher
```

## Announcements

The Simplified Advanced Encryption Standard (S-AES) has a few notable drawbacks:

Reduced Security: Due to its simplified design, S-AES offers lower security compared to the full AES encryption algorithm. It uses smaller key sizes (8 bits) and operates on smaller data blocks, which makes it more vulnerable to brute-force attacks.

Limited Key Length: S-AES employs an 16-bit key, which provides only 65536 possible key combinations. This limited key space makes it susceptible to exhaustive search attacks where an adversary tries every possible key.

Less Resistance to Cryptanalysis: S-AES may be more susceptible to various cryptographic attacks compared to the full AES algorithm. For instance, it may be more vulnerable to differential and linear cryptanalysis due to its simplified substitution and permutation operations.

Not Suitable for High-Security Applications: S-AES is generally not recommended for applications requiring a high level of security, such as securing sensitive financial transactions or classified information. Its simplified structure makes it more suitable for educational purposes or scenarios where lightweight encryption is acceptable.

Not Standardized: S-AES is not an industry-standard encryption algorithm like AES. It may not be supported by widely used cryptographic libraries or hardware, limiting its practical applicability in real-world applications.

Overall, while S-AES serves as a valuable educational tool to understand the core concepts of AES, it is not intended for critical security applications and should be used with caution in scenarios where strong encryption is essential.




