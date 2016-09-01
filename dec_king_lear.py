# coding: utf-8
import urllib2
import re
import httplib

def main(): 
    # read webpage "http://shakespeare.mit.edu/lear/full.html"
    #page = urllib2.urlopen('http://shakespeare.mit.edu/lear/full.html', timeout = 20)
    page = urllib2.urlopen('https://www.python.org/', timeout = 20)
    page_html = page.read()
    
    page_cont = sanitize_page(page_html)
    # decode the str with utf-8
    page_cont = page_cont.decode('utf-8')
    
    code_list = page_cont.lower().split(' ')
    # open txt file to write decrypted info into it
    fh = open('dec_code.txt', 'w')
    total_code = ""
    
    for code in code_list: 
        # if the last char is not a letter, drop it from the code 
        if not (code[-1] >= 'a' and code[-1] <= 'z' or code[-1] >= 'A' and code[-1] <= 'Z'): 
            code = code[:-1]
    
        # decrypt it if the code only contains letters
        if code and (not re.search(r'[^a-z^A-Z]', code)): 
            get_code = '/api/' + code + '/'
            # send the request to web server and receive the response
            conn = httplib.HTTPConnection("127.0.0.1:5000")
            conn.request('get', get_code)
            resp = conn.getresponse().read()

            # sanitize the html response
            resp_cont = sanitize_page(resp)

            # get the decrypted code or the printed time message
            if re.search(r'The decrypted code is: .*', resp_cont): 
                dec_code = resp_cont.split(': ')[-1]
            else: 
                dec_code = resp_cont.split(' ')[-1]
    
            total_code += dec_code + '\n'
    
    # write all the codes into txt file
    fh.write(total_code)
    fh.close()

# remove the HTML tags and '\n'
def sanitize_page(page_html): 
    page_cont = re.sub(r'<[^>]*>', '', page_html)
    page_cont = re.sub(r'\n', '', page_cont)
    page_cont = re.sub(r'\s+', ' ', page_cont)
    page_cont = page_cont.strip()

    return page_cont

if __name__ == '__main__': 
    main()
