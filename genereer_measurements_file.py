# quick and dirty code, to generate a measurements.csv file for uploading to the FTP server: hydromonitor.nl.
# The measurements file makes all historical measurements available in the FieldLoggerApp. 


import csv
import sys
import os
# def create_measurements(measurement_files_dir, target_file_dir)

# bron directory van de measurement_files
measurement_files_dir = 'G:\projecten\WBN\python_scripts\genereer_measurements_csv\measurements'

# doel file van de measurement_files (het file dat je op de FTP server gaat zetten)
target_measurement_file = 'G:\projecten\WBN\python_scripts\genereer_measurements_csv\\measurements.csv'

# open het doel file and loop over all measurements files.
with open (target_measurement_file, 'w', newline='') as target_file:

    # open a csv writer to create 1 measurement file
    measurements_writer = csv.writer(target_file, delimiter=';')

    # first insert tghe headers in the target file
    measurements_writer.writerow(["LOCATION; DATE; TIME; VALUE; TYPE"])

    # Loop over alle measurements bestanden in de directory: .. en zet deze in het juiste formaat in de measurements_writer.
    for subdir, dirs, files in os.walk(measurement_files_dir):

        for measurement_file in files:

           measurement_file = os.path.join(subdir, measurement_file)

           with open(measurement_file, 'r') as csvfile:

                #measurements_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                measurements_reader = csv.reader(csvfile)

                # skip the headers
                next(measurements_reader, None)  

                for row in measurements_reader:
                    print(''.join(row))
                    measurements_writer.writerow(row)



### when done upload the measurements file to the FTP server:
##from ftplib import FTP
##
### connect to the FTP
##ftp = FTP_TLS('hydromonitor.nl')
##ftp.login(user='provincie_zeeland', passwd='29uyq87ml1')
##ftp.cwd('FieldLoggerData/Imported/')
##
### store the file
##filename = 'exampleFile.txt'
##ftp.storbinary('STOR '+filename, open(filename, 'rb'))
##ftp.quit()


