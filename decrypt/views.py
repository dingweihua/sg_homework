# -*- coding: utf-8 -*-

from decrypt import app, code
from flask import render_template

# the URL which triggers our function
@app.route('/api/<raw_code>/')
def decrypt(raw_code):
    # decrypt code
    dec_code = code.decrypt_code(raw_code)
    # check whether the decrypted code exists
    dec_code_flag, dec_code_time = code.check_dec_code(dec_code)
    # call the template to show the decrypted code
    return render_template('show_dec.html', dec_code=dec_code,
        dec_code_flag=dec_code_flag, dec_code_time=dec_code_time)