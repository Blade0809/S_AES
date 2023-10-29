# aes_app/views.py
from django.shortcuts import render
from .utils import (encrypt, decrypt, ascii_encrypt, ascii_decrypt, double_encrypt, double_decrypt, tribble_encrypt,
                    tribble_decrypt, attack_the_middle, cipher_block_chaining_encrypt, cipher_block_chaining_decrypt)


def aes_view(request):
    result = None
    if request.method == 'POST':
        text = request.POST.get('text')
        password = request.POST.get('password')
        operation = request.POST.get('operation')

        if operation == 'encrypt':
            result = encrypt(text, password)
        elif operation == 'decrypt':
            result = decrypt(text, password)
        elif operation == 'ascii_encrypt':
            result = ascii_encrypt(text, password)
        elif operation == 'ascii_decrypt':
            result = ascii_decrypt(text, password)
        elif operation == 'double_encrypt':
            result = double_encrypt(text, password)
        elif operation == 'double_decrypt':
            result = double_decrypt(text, password)
        elif operation == 'tribble_encrypt':
            result = tribble_encrypt(text, password)
        elif operation == 'tribble_decrypt':
            result = tribble_decrypt(text, password)
        elif operation == 'cipher_block_chaining_encrypt':
            result = cipher_block_chaining_encrypt(text, password, '1010101010101010')
        elif operation == 'cipher_block_chaining_decrypt':
            result = cipher_block_chaining_decrypt(text, password, '1010101010101010')

        return render(request, 'aes.html', {'result': result})

    return render(request, 'aes.html')


