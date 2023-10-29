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

#### Trible Encrypt

### Level 5: Working Mode


