# Script to import the measurement for ObsWell B54F0099. 
#Measurements where missing due to missing metadata.

# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:32:41 2019

@author: mcari
"""

#import csv
import sys
import os
import logging
import pandas
import glob



def test_start_measurement_import_for_NITGCode_FilterNo(nitgcode_filterno):

    """Start the search for NITGCode: nitgcode_filterno.
    param is a STRING and should be in format: B54F0099_1"""
    
    # logging
    logging.basicConfig(filename="messages.log",
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        filemode = "w",
                        datefmt='%d/%m/%Y %I:%M:%S')
    
   
    
    try:
        
         #print("Start search:")
         logging.warning('Start search for: ' + str(nitgcode_filterno))
         
     
     
         #use panda
         path = 'G:\projecten\WBN\python_scripts\meetstanden_inlezen_B54F0099\\backup_FTP_meetbestanden_okt_2018'
         all_files = glob.glob(path + "/*.csv")

         li = []

         for filename in all_files:
             df = pandas.read_csv(filename, sep='delimiter', header=0)
             li.append(df)

         d_frame = pandas.concat(li, axis=0, ignore_index=True)
         
         print("------d_frame--------")
         print(d_frame)
         
         # select only the nitgcode_filterno
         #df_filtered = d_frame.query('location == "B54F0099_1"')
         df_filtered = d_frame.loc[d_frame['LOCATION'] == 'B54F0099_1']
         
         print("-----df_filtered----")
         print(df_filtered)
#        # tod: change the path to the latest production files.
#        for root, dirs, files in os.walk('G:\projecten\WBN\python_scripts\meetstanden_inlezen_B54F0099\\backup_FTP_meetbestanden_okt_2018'):
#    
#               # loop over the .csv files in the files collection
#              for measurement_file in files:
#       
#                      # get the complete path of the source .csv file
#                      measurement_file_path = os.path.join(root, measurement_file)
#                      print("measurement_file_path: ", measurement_file_path)    
#                      
#                      # open the source .csv file to check the contents.    
#                      with open(measurement_file_path, 'r') as csvfile:
#
#                          # open a reader on the source .csv file(todo: write exception code)
#                          measurements_reader = csv.reader(csvfile, delimiter=';')
#
#                          # skip the headers
#                          next(measurements_reader, None)  
#            
#                          # loop over the rows in the csv file and check the values found.
#                          for row in measurements_reader:
#                
#                                nitgcode = row[0]
#                
#                                if nitgcode == 'B54F0099_1':
#                                    #write it to the destination file.
#                                    measurement_filewriter.writerow([row[0], row[1], row[2], row[3], row[4]])
#                                    
#                                    # report the action
#                                    report_str = 'Gevonden: ', str(nitgcode), ' met gemeten stand: ', str(row[3]), ' op datum: ', str(row[1])
#                                    print(report_str)
#                                    logging.warning(report_str)
#            
            
            
    except (Exception) as error:
            print(error)
            print("Hola, something went wrong")
            logging.warning('Er iets iets foutgegaan')
            
    finally:
            print('Search finished. Results are written to file.')
                
            # close logging
            logging.shutdown()



               
               