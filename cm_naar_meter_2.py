# Script to rewrite the measurements in .csv files. Sometime's values are in centimeters instead of meters. This gives wrong results in Menyanthes.
# rewrite the code


import csv
import sys
import os
# def correct_measurement_files(source_files_dir, target_files_dir)

# source directory van# Script to rewrite the measurements in .csv files. Sometime's values are in centimeters instead of meters. This gives wrong results in Menyanthes.
# rewrite the code


import csv
import sys
import os
# def correct_measurement_files(source_files_dir, target_files_dir)



for root, dirs, files in os.walk('G:\projecten\WBN\python_scripts\cm_naar_meter\\backup_FTP_meetbestanden_okt_2018'):
    
    # loop over the .csv files in the files collection
    for measurement_file in files:
       
       # create a new .csv file to write the (corrected) rows for this measurement file.
       with open(measurement_file, 'w', newline='') as new_csvfile:
           
           # create the csv_file writer object #new_csvfile
           measurement_filewriter = csv.writer(new_csvfile, delimiter=';')
           # first insert the headers in the target file
           measurement_filewriter.writerow(["LOCATION", "DATE", "TIME", "VALUE", "TYPE"])
    
           # get the complete path of the source .csv fikle
           measurement_file_path = os.path.join(root, measurement_file)

           # open the source .csv file to check the contents.    
           with open(measurement_file_path, 'r') as csvfile:

            # open a reader on the source .csv file(todo: write exception code)
            measurements_reader = csv.reader(csvfile, delimiter=';', quotechar='|')

            # skip the headers
            next(measurements_reader, None)  
            
            # loop over the rows in the csv file and check the values found.
            for row in measurements_reader:
                
                # first test if it's a complete row with Comment or Value, otherwise skip this row and log the file.
                if row.count('Comment') == 1:
                    # it's a Comment not a value, keep it as is.
                    measurement_filewriter.writerow([row[0], row[1], row[2], row[3], row[4]])

                elif row.count('Value') == 1:
                                       
                    # get the measurement_value from 3th position
                    meetwaarde = row[3];

                    # get # of dots in meetwaarde value
                    dotcount_meetwaarde = meetwaarde.count(".")

                    # if there is no dot (.) in de string, its probably a centimeters value.
                    # --------------------
                    # Centimeter test
                    # --------------------
                    if dotcount_meetwaarde == 0:

                        # 3 possible situations: 1 position (do nothing), 2 positions or 3 positions (hopefully not more exceptions)
                        lengte_meetwaarde_str = len(meetwaarde)                       

                        if lengte_meetwaarde_str == 1:
                            # "1" ingevoerd, zal naar m. moeten
                            #
                            # do nothing, keep the meetwaarde. (in overleg met Ronnie)
                            meetwaarde = meetwaarde

                        elif lengte_meetwaarde_str == 2:
                            # "12" ingevoerd
                            meetwaarde = "0." + meetwaarde

                        elif lengte_meetwaarde_str == 3:
                            # "123" ingevoerd oid
                            meetwaarde = meetwaarde[0] + "." + meetwaarde[1:3]

                        else:
                            print("Waarde gevonden: * ", meetwaarde , " * Deze waarde heeft geen punt en valt niet in range 1-3. Voor row: ", row, " in measurement_file: ", measurement_file)
                        
                        # write the results to the new .csv file.
                        measurement_filewriter.writerow([row[0], row[1], row[2], meetwaarde, row[4]])
                        #
                        # Don't write a comment. Just log the value to the console.
                        # Too much comments will polute the database.
                        #
                        # measurement_filewriter.writerow([row[0], row[1], row[2], "Meetwaarde gecorrigeerd naar meters of andere afwijking gevonden.", "Comment"])

                            
                    elif dotcount_meetwaarde == 1:
                        # measurement is okay. Write line to new csv file and do nothing.
                        measurement_filewriter.writerow([row[0], row[1], row[2], row[3], row[4]])
                        
                    elif dotcount_meetwaarde > 1:
                        # extra check, write this in a logging file for later analyses.
                        print("Error found: ", meetwaarde, "in file: ", measurement_file)

                        # do nothing for time being, write it in the csv as is, will check this row later
                        measurement_filewriter.writerow([row[0], row[1], row[2], row[3], row[4]])
                    
                else:
                    # No Comment or value found in this row, print it to the console and continue
                    print("Hola, geen Comment of Value in deze row: ", row, "in measurement_file: ", measurement_file)
                    #measurement_filewriter.writerow([row[0], row[1], row[2], row[3], row[4]])


                
             
                







 de measurement_files
#source_measurement_files_dir = 'G:\projecten\WBN\python_scripts\cm_naar_meter\test_meetbestanden'

for root, dirs, files in os.walk('G:\projecten\WBN\python_scripts\genereer_measurements_csv\measurement_files_all'):

    # loop over the .csv files in the files collection
    for measurement_file in files:

       # always create a new .csv file to write the (corrected) rows for this measurement file.
       with open(measurement_file, 'w', newline='') as new_csvfile:
           
           # create the csv_file writer object
           measurement_filewriter = csv.writer(new_csvfile, delimiter=';', quoting=csv.QUOTE_ALL)

           # first insert the headers in the target file
           measurement_filewriter.writerow(["LOCATION", "DATE", "TIME", "VALUE", "TYPE"])
    
           # get the complete path of the source .csv fikle
           measurement_file_path = os.path.join(root, measurement_file)

           # open the source .csv file to check the contents.    
           with open(measurement_file_path, 'r') as csvfile:

            # open a reader on the source .csv file(todo: write exception code)
            measurements_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            
            # loop over the rows in the csv file and check the values found.
            for row in measurements_reader:
                
                if row[:4] == "Comment":
                    # it's a Comment not a value, keep it.
                    measurement_filewriter.writerow([row[0], row[1], row[2], row[3], row[4]])

                # test for Value' string in item[4], only then we are sure it is a measurement and not a Comment.
                if row[4] == 'Value':
                    
                    # get the measurement_value from 3th position
                    meetwaarde = row[3];

                    # get # of dots in meetwaarde value
                    dotcount_meetwaarde = meetwaarde.count(".")

                    # if there is no dot (.) in de string, its probably a centimeters value.
                    if dotcount_meetwaarde == 0:

                        # 3 possible situations: 1 position (do nothing), 2 positions or 3 positions (hopefully not more exceptions)
                        lengte_meetwaarde_str = len(meetwaarde)                       

                        if lengte_meetwaarde_str == 1:
                            # "1" ingevoerd, zal naar m. moeten
                            #
                            # do nothing, keep the meetwaarde. (in overleg met Ronnie)
                            meetwaarde = meetwaarde

                        elif lengte_meetwaarde_str == 2:
                            # "12" ingevoerd
                            meetwaarde = "0." + meetwaarde

                        elif lengte_meetwaarde_str == 3:
                            # "123" ingevoerd
                            meetwaarde = meetwaarde[0] + "." + meetwaarde[1:3]

                        else:
                            print("Waarde gevonden die geen punt heeft en niet in range 1-3 valt: ", meetwaarde)
                        
                        # write the results to the new .csv file.
                        measurement_filewriter.writerow([row[0], row[1], row[2], meetwaarde, row[4]])
                        measurement_filewriter.writerow([row[0], row[1], row[2], "Meetwaarde gecorrigeerd naar meters door script.", "Comment"])

                            
                    elif dotcount_meetwaarde == 1:
                        # measurement is okay. Write line to new csv file and do nothing.
                        measurement_filewriter.writerow([row[0], row[1], row[2], row[3], row[4]])
                        
                    elif dotcount_meetwaarde > 1:
                        # extra check, write this in a logging file for later analyses.
                        print("Error found: ", meetwaarde, "in file: ", measurement_file)

                        # do nothing for time being, write it in the csv as is, will check this row later
                        measurement_filewriter.writerow([row[0], row[1], row[2], row[3], row[4]])
                    
                
             
                







