#Passing right ascension and declination for targets for the NVSS Postage Stamp.
def get_first(RA, DEC, NAME,):

    data = {
        'Equinox': 'J2000',
        'PolType': 'I',
        'ObjName': '',
        'RA': RA,
        'Dec': DEC,
        'Size': '0.25 0.25',
        'Cells': '15.0 15.0',
        'MAPROJ': 'SIN',
        'rotate': '0.0',
        'Type': 'image/x-fit',
    }
    url = 'https://www.cv.nrao.edu/cgi-bin/postage.pl'
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.post(url, data=data, stream=False, verify=False)
    if response.text.startswith('<PRE>'):
        print("File not found")
        return

    print(NAME)
    filename = str(NAME)+".fits"
    return astropy.io.fits.open(io.BytesIO(response.content)).writeto(filename)
  #Returned file is in FITS format
