from decrypt import app
from flask import render_template

# the URL which triggers our function
@app.route('/api/<raw_code>/')

def decrypt(raw_code): 
    dec_code = ''
    for char in raw_code: 
        # transfer the char to its ascii
        char_ascii = ord(char)

        # decrypt each char and transfer the ascii to char
        if (char >= 'X' and char <= 'Z') or (char >= 'x' and char <= 'z'): 
           dec_char = chr(char_ascii + 3 - 26)
        else: 
           dec_char = chr(char_ascii + 3)

        dec_code += dec_char
    
    # check whether the decrypted code exists
    dec_code_flag, dec_code_time = check_dec_code(dec_code)
    
    # call the template to show the decrypted code
    return render_template('show_dec.html', dec_code = dec_code, dec_code_flag = dec_code_flag, 
        dec_code_time = dec_code_time)

def check_dec_code(dec_code): 
    import models
    from decrypt import db
    import datetime

    # get all the tables in DB
    codes = models.Code.query.all()

    # store the codes into a list
    code_list = []
    for i in range(len(codes)): 
        code_list.append(codes[i].code)

    # decrypted code already exists in DB
    if dec_code in code_list: 
        dec_code_flag = True
        # get the decrypted code's index
        dec_code_idx = code_list.index(dec_code)

        dec_code_time = codes[dec_code_idx].timestamp
    else:
        dec_code_flag = False
        dec_code_time = datetime.datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S')

        # store the decrypted code into DB
        add_code = models.Code(code = dec_code, timestamp = dec_code_time)
        db.session.add(add_code)
        db.session.commit()
    
    return dec_code_flag, dec_code_time