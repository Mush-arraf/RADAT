#Passing right ascension and declination for targets for the FIRST website.
def get_first(RA, DEC, NAME,):

    data = {
        'RA': RA,
        'Dec': DEC,
        'Equinox': 'J2000',
        'ImageSize': '4.5',
        'ImageType': 'FITS File',
        'MaxInt': 30,
        'Epochs': '',
        'Fieldname': '',
        '.submit': 'Extract the Cutout ',
        '.cgifields': 'ImageType',
    }
    url = 'https://third.ucllnl.org/cgi-bin/firstcutout'
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
