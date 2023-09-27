# RADAT :satellite:	:desktop_computer:	
Radio Astronomy Data Acquisition Tool (RADAT) is a group of functions designed for the acquisition of radio astronomy data from several sources. RADAT uses HTTP requests through Python and Astropy library to convert raw data into FITS images/files. This method has  few advantages over the traditional way of collecting data through FTP. One such advantage is HTTP requests are not bound by the FTP connection limitations. Currently, RADAT supports only two sources. Faint Images of the Radio Sky at Twenty-Centimeters (FIRST) image cutouts and NRAO/VLA Sky Survey (NVSS) post stamp.

Both the available functions in this repository require just the right ascension (RA) and declination (DEC) of the required sources. The returns from the respective functions are FITS format Images/files. 


