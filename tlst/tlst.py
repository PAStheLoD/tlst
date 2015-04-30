#!/usr/bin/env python3

import re
import click
from OpenSSL import crypto


def get_chunk(path):
    buf = ""
    begin = False
    end = False
    with open(path) as f:
        while True:
            last_read = f.read(100)
            buf += last_read
            r = re.search("\s*-+BEGIN CERTIFICATE-+ *", buf)
            if r:
                begin = r.start()
            else:
                print(" --------- notfound: {} \n\n\n ---- \n".format(buf))

            r = re.search(" *-+END CERTIFICATE-----", buf)
            if r:
                if begin is not False:
                    end = r.end()
                    yield buf[begin:end]
                buf = buf[end:]

            if len(last_read) < 100:
                break

@click.command()
@click.argument('infile', type=click.Path(exists=True))
@click.option('--noout', is_flag=True)
@click.option('--verify', is_flag=True)
def main(infile, noout, verify):

    cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(infile).read())

    certs = []

    for c in get_chunk(infile):
        if not noout:
            print(c)
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, c)
        print(cert.get_subject())
        if verify:
            certs.append(cert)

    if verify:
        pass
        #  ah 

if __name__  ==  '__main__':
    main()
