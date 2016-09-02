# -*- coding: utf-8 -*-

import datetime

from decrypt import models, db

def decrypt_code(raw_code):
    dec_code = ''
    for char in raw_code:
        # transfer the char to its ascii
        char_ascii = ord(char)
        # decrypt each char and transfer the ascii to char
        if char.lower() >= 'x' and char.lower() <= 'z': 
           dec_char = chr(char_ascii + 3 - 26)
        else: 
           dec_char = chr(char_ascii + 3)
        dec_code += dec_char
    return dec_code

def check_dec_code(dec_code):
    code_inst = models.Code.query.filter_by(code=dec_code).first()
    if code_inst:
        dec_code_flag = True
        dec_code_time = code_inst.timestamp
    else:
        dec_code_flag = False
        dec_code_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        # store the decrypted code into DB
        add_code = models.Code(code=dec_code, timestamp=dec_code_time)
        db.session.add(add_code)
        db.session.commit()
    return dec_code_flag, dec_code_time