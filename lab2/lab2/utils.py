import math
import time

s_box = [
    ['9', '4', 'a', 'b'],
    ['d', '1', '8', '5'],
    ['6', '2', '0', '3'],
    ['c', 'e', 'f', '7']
]

inverse_s_box = [
    ['a', '5', '9', 'b'],
    ['1', '7', '8', 'f'],
    ['6', '0', '2', '3'],
    ['c', '4', 'd', 'e']
]

mix_column_matrix = ['0', '4', '8', 'c', '3', '7', 'b', 'f', '6', '2', 'e', 'a', '5', '1', 'd', '9']

inverse_mix_column_matrix_2 = ['0', '2', '4', '6', '8', 'a', 'c', 'e', '3', '1', '7', '5', 'b', '9', 'f', 'd']

inverse_mix_column_matrix_9 = ['0', '9', '1', '8', '2', 'b', '3', 'a', '4', 'd', '5', 'c', '6', 'f', '7', 'e']


def x_to_b(x_num_strs):
    binary_num = ''
    for i in range(len(x_num_strs)):
        binary_num += bin(int(x_num_strs[i], 16))[2:].zfill(4)
    return binary_num


def b_to_x(b_num_strs):
    x_num = ''
    for i in range(int(len(b_num_strs) / 4)):
        x_num += hex(int(b_num_strs[4 * i:4 * i + 4], 2))[2:]
    return x_num


def b_to_int(b_num_str):
    number = 0
    for i in range(len(b_num_str)):
        if b_num_str[i] == '1':
            number += math.pow(2, len(b_num_str) - i - 1)
    return int(number)


def binary_xor(a, b):  # a, b both str
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result


def rot_nib(num):  # num should be str
    new_num = str(num[4:]) + str(num[:4])
    return new_num


def sub_nib(num):
    new_num = str(s_box[b_to_int(num[0:2])][b_to_int(num[2:4])]) + str(s_box[b_to_int(num[4:6])][b_to_int(num[6:8])])
    return new_num


# 轮密钥生成
def generate_round_keys(master_key):
    list_round_keys = []
    round_keys = x_to_b(master_key)
    w_0 = round_keys[:8]  # str
    w_1 = round_keys[8:]
    w_2 = binary_xor(binary_xor(w_0, '10000000'), x_to_b(sub_nib(rot_nib(w_1))[0]) +
                     x_to_b(sub_nib(rot_nib(w_1))[1]))
    w_3 = binary_xor(w_2, w_1)
    w_4 = binary_xor(binary_xor(w_2, '00110000'), x_to_b(sub_nib(rot_nib(w_3))[0]) +
                     x_to_b(sub_nib(rot_nib(w_3))[1]))
    w_5 = binary_xor(w_4, w_3)
    list_round_keys.append(w_0 + w_1)
    list_round_keys.append(w_2 + w_3)
    list_round_keys.append(w_4 + w_5)
    return list_round_keys


# 密钥加
def add_round_key(state, round_key):  # round key 16 bit long
    state[0] = binary_xor(state[0], round_key[0:4])
    state[1] = binary_xor(state[1], round_key[8:12])
    state[2] = binary_xor(state[2], round_key[4:8])
    state[3] = binary_xor(state[3], round_key[12:16])
    return state


# 半字节代替
def sub_bytes(state, s_box):
    new_state = []
    for i in range(4):
        row = b_to_int(state[i][:2])
        column = b_to_int(state[i][2:])
        new_state.append(x_to_b(s_box[row][column]))
    return new_state


def inverse_sub_bytes(state, inverse_s_box):
    new_state = []
    for i in range(4):
        row = b_to_int(state[i][:2])
        column = b_to_int(state[i][2:])
        new_state.append(x_to_b(inverse_s_box[row][column]))
    return new_state


# 行移位
def shift_rows(state):
    tmp = state[2]
    state[2] = state[3]
    state[3] = tmp
    return state


# 列混淆
def mix_columns(state):
    new_state = [binary_xor(state[0], x_to_b(mix_column_matrix[b_to_int(state[2])])),
                 binary_xor(state[1], x_to_b(mix_column_matrix[b_to_int(state[3])])),
                 binary_xor(state[2], x_to_b(mix_column_matrix[b_to_int(state[0])])),
                 binary_xor(state[3], x_to_b(mix_column_matrix[b_to_int(state[1])]))]
    return new_state


def inverse_mix_columns(state):
    new_state = [binary_xor(x_to_b(inverse_mix_column_matrix_9[b_to_int(state[0])]),
                            x_to_b(inverse_mix_column_matrix_2[b_to_int(state[2])])),
                 binary_xor(x_to_b(inverse_mix_column_matrix_9[b_to_int(state[1])]),
                            x_to_b(inverse_mix_column_matrix_2[b_to_int(state[3])])),
                 binary_xor(x_to_b(inverse_mix_column_matrix_9[b_to_int(state[2])]),
                            x_to_b(inverse_mix_column_matrix_2[b_to_int(state[0])])),
                 binary_xor(x_to_b(inverse_mix_column_matrix_9[b_to_int(state[3])]),
                            x_to_b(inverse_mix_column_matrix_2[b_to_int(state[1])]))]
    return new_state


def get_state_matrix(plain):  # plain should be 4 bit
    binary_plain = x_to_b(plain)
    matrix = []
    matrix.append(binary_plain[0:4])
    matrix.append(binary_plain[8:12])
    matrix.append(binary_plain[4:8])
    matrix.append(binary_plain[12:16])
    return matrix  # example ['0100', '1101', '0101', '0101']


# 加密函数
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


def ascii_encrypt(ascii_plain, master_key):
    cipher = ''
    chr_cipher = ''
    for i in range(int(len(ascii_plain) / 2)):
        tmp_ascii = ascii_plain[2 * i:2 * i + 2]
        tmp_bin = bin(ord(tmp_ascii[0]))[2:].zfill(8) + bin(ord(tmp_ascii[1]))[2:].zfill(8)
        x_string = b_to_x(tmp_bin)
        cipher_string = encrypt(x_string, master_key)
        cipher += cipher_string
    for i in range(int(len(cipher) / 2)):
        tmp_cipher = cipher[2 * i:2 * i + 2]
        tmp_int = b_to_int(x_to_b(tmp_cipher))
        chr_cipher += chr(tmp_int)
    return chr_cipher


def double_encrypt(plain_text, master_key_2):
    key_1 = master_key_2[:4]
    key_2 = master_key_2[4:]
    tmp_cipher = encrypt(plain_text, key_1)
    cipher = encrypt(tmp_cipher, key_2)
    return cipher


def tribble_encrypt(plain_text, master_key_3):
    key_1 = master_key_3[:4]
    key_2 = master_key_3[4:]
    tmp_cipher_1 = encrypt(plain_text, key_1)
    tmp_cipher_2 = encrypt(tmp_cipher_1, key_2)
    cipher = encrypt(tmp_cipher_2, key_1)
    return cipher


# 解密函数
def decrypt(ciphertext, master_key):
    round_keys = generate_round_keys(master_key)
    plain = ''
    for i in range(int(len(ciphertext) / 4)):
        tmp_plain = ''
        tmp_cipher = ciphertext[4 * i:4 * i + 4]
        tmp_matrix = get_state_matrix(tmp_cipher)
        tmp_matrix = add_round_key(tmp_matrix, round_keys[2])

        tmp_matrix = shift_rows(tmp_matrix)
        tmp_matrix = inverse_sub_bytes(tmp_matrix, inverse_s_box)
        tmp_matrix = add_round_key(tmp_matrix, round_keys[1])
        tmp_matrix = inverse_mix_columns(tmp_matrix)

        tmp_matrix = shift_rows(tmp_matrix)
        tmp_matrix = sub_bytes(tmp_matrix, inverse_s_box)
        tmp_matrix = add_round_key(tmp_matrix, round_keys[0])
        tmp_plain += b_to_x(tmp_matrix[0])
        tmp_plain += b_to_x(tmp_matrix[2])
        tmp_plain += b_to_x(tmp_matrix[1])
        tmp_plain += b_to_x(tmp_matrix[3])
        plain += tmp_plain
    return plain


def ascii_decrypt(ascii_cipher, master_key):
    plain = ''
    chr_plain = ''
    for i in range(int(len(ascii_cipher) / 2)):
        tmp_ascii = ascii_cipher[2 * i:2 * i + 2]
        tmp_bin = bin(ord(tmp_ascii[0]))[2:].zfill(8) + bin(ord(tmp_ascii[1]))[2:].zfill(8)
        x_string = b_to_x(tmp_bin)
        plain_string = decrypt(x_string, master_key)
        plain += plain_string
    for i in range(int(len(plain) / 2)):
        tmp_plain = plain[2 * i:2 * i + 2]
        tmp_int = b_to_int(x_to_b(tmp_plain))
        chr_plain += chr(tmp_int)
    return chr_plain


def double_decrypt(cipher_text, master_key_2):
    key_1 = master_key_2[:4]
    key_2 = master_key_2[4:]
    tmp_plain = decrypt(cipher_text, key_2)
    plain = decrypt(tmp_plain, key_1)
    return plain


def tribble_decrypt(cipher_text, master_key_3):
    key_1 = master_key_3[:4]
    key_2 = master_key_3[4:]
    tmp_plain_1 = decrypt(cipher_text, key_1)
    tmp_plain_2 = decrypt(tmp_plain_1, key_2)
    plain = decrypt(tmp_plain_2, key_1)
    return plain


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


def cipher_block_chaining_decrypt(long_cipher_text, master_key, IV):
    plain = ''
    for i in range(int(len(long_cipher_text) / 4)):
        if i == 0:
            plain += b_to_x(binary_xor(IV, x_to_b(decrypt(long_cipher_text[:4], master_key))))
        else:
            plain += b_to_x(
                binary_xor(x_to_b(long_cipher_text[4 * i - 4:4 * i]), x_to_b(decrypt(long_cipher_text[4 * i:4 * i + 4],
                                                                                     master_key))))
    return plain


# test
master_key = '2d55'
# master_key_2 = '2d553e44'
# IV = '1010101010101010'

plaintext = '3ad4'
ciphertext = encrypt(plaintext, master_key)
# print(f"加密后的密文：{ciphertext}")  # 01ec

# decrypted_text = tribble_decrypt(ciphertext, master_key_2)
# print(f"解密后的明文：{decrypted_text}")

# cipher = cipher_block_chaining_encrypt('3469163621637caadc63', master_key, IV)
# print(cipher)
# plain = cipher_block_chaining_decrypt('53cc645441a3aea14bf4', master_key, IV)
# print(plain)
# print(b_to_x(binary_xor(x_to_b(decrypt('6454', master_key)), x_to_b('53cc'))))  # 1636
# print(b_to_x(binary_xor(IV, x_to_b('3469'))))
# key = attack_the_middle('3ad4', '01ec')
# print(key)
