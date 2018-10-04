"""This loader is designed to extract from a list of airfoils, that can be updated with your profiles data generated
through the program "Profili 2", which can be found at http://www.profili2.com , a couple of airfoils which maximise
Lift Coefficient (Cl) or the Efficiency (E) of the main wing, and return the highest Cl profile fot the flap.
Files generated are ready to be processed in a Multi profile Hess Smith solver written, nowadays in Matlab®

Author: Dott. Meazzo Mirco"""

"MAIN"



#%% Header

print('\n\n/------------------------------------------------------------------------------------------\ '
      '\n|############################## Starting Optimization Loader ##############################|'
      '\n\------------------------------------------------------------------------------------------/'
      '\n\n')
#%% Import section

import import_polar

import config;       table_f = config.table_f;      table_w = config.table_w;       path = config.path

import re

import sys

import numpy as np



#%% Mode selection


print('\nChoose which kind of analysis is required.\nType "e" to get maximum efficiency profile\n'
      'Type "cl" to get maximum lift coefficient profile\n'
      'Type "man" to select profiles manually \n\n'
      '(For the flap is always chosen the profile with the best Cl)')

chooser = input('\n\nMode selection: ')



#%%\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\OPTI WING////////////////////////////////////////////////////
# if sequence to perform analysis based on previous choice for WING ONLY

if chooser == 'cl':


	cl_list = (table_w[:, 2]).T                    # Extract just Cl row
	cl_list_w = []                                 # Create matrix used to store the float data

	for items in cl_list:                          # Convert all the elements inside cl_list in floating point values

		item = float(items)

		cl_list_w.append( item )

	index = ( cl_list_w ).index( max( cl_list_w )) # Index of the maximum value of cl_list (floating values)

	solution_w = table_w[index, :]

	# Find the name of the file, based on the entry 0 in "solution_w" and clean it

	file_name_w = solution_w[0]

	file_name_w.replace('_data.txt', ' ')

	file_name_w = re.sub('\_data.txt$', '', file_name_w)

	print('\nFor the WING the best Cl is achieved by {}, Cl_max= {}, alpha= {}'.format( file_name_w,
	                                                                                    solution_w[2], solution_w[1]))



elif chooser == 'e':


	e_list = table_w[:, 4]                         # Extract just E row
	e_list_w = []                                  # Create matrix used to store the float data

	for items in e_list:                           # Convert all the elements inside e_list in floating point values

		item = float(items)

		e_list_w.append( item )

	index = ( e_list_w ).index( max( e_list_w ))   # Index of the maximum value of cl_list (floating values)

	solution_w = table_w[index, :]

	# Find the name of the file, based on the entry 0 in "solution_w" and clean it

	file_name_w = solution_w[0]

	file_name_w.replace('_data.txt', ' ')

	file_name_w = re.sub('\_data.txt$', '', file_name_w)

	print('\nFor the WING the best E is achieved by {}, E_max= {}, alpha= {}'.format( file_name_w,	                                                                                  solution_w[4], solution_w[1]))



elif chooser == 'man':

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\MANUAL WING/////////////////////////////////////////////////

	file_name_w = input('Name of the airfoil in /Polar Data that you want to use as WING:')   # Profile name search

	path_airfoil_w = str( path +'/Polar Data/' + file_name_w + '_data.txt' )               # Path of the file as string

	print('Fetching profile data from:\n'+ path_airfoil_w)

	str_table_w = []                                                                       # Setup the container

	for i in range( len( table_w[ :,0 ] )):                         # i range from 0 to the number of rows of "table_w"

		str_table_w.append( str( table_w[ i, 0 ] ))                 # Translate from numpy.array to string the names of
																	# profiles, in order to compare them with airfoil_w

	index_w = str_table_w.index( file_name_w + '_data.txt' )        # Return the index of airfoil_w in strings table_w

	solution_w = table_w[index_w, :]

	print('\nThe selected WING have Cl_max= {}, alpha= {}'.format( solution_w[2], solution_w[1] ))



else:

	print('Wrong typing, exit from program...')

	sys.exit()



#%%\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\OPTI FLAP////////////////////////////////////////////////////

conditions = [ 'cl', 'e']                          # Cases for

if chooser in conditions :                              # Search Cl_max profile for the flap

	cl_list = (table_f[:, 2]).T                    # Extract just Cl row

	cl_list_f = []                                 # Create matrix used to store the float data

	for items in cl_list:                          # Convert all the elements inside cl_list in floating point values

		item = float(items)

		cl_list_f.append( item )

	index = ( cl_list_f ).index( max( cl_list_f )) # Index of the maximum value of cl_list (floating values)

	solution_f = table_f[index, :]

	# Find the name of the file, based on the entry 0 in "solution_f"

	file_name_f = solution_f[0]

	file_name_f.replace('_data.txt', ' ')

	file_name_f = re.sub('\_data.txt$', '', file_name_f)

	print('\nFor the FLAP the best Cl is achieved by {}, Cl_max= {}, alpha= {}'.format( file_name_f,
                                                                                    solution_f[2], solution_f[1]))


elif chooser == 'man':

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\MANUAL FLAP///////////////////////////////////////////////////

	file_name_f = input('Name of the airfoil in /Polar Data that you want to use as FLAP: ')

	path_airfoil_f = str( path +'/Polar Data/' + file_name_f + '_data.txt')                # Path of the file as string

	print('Fetching profile data from:\n'+path_airfoil_f)

	str_table_f = []                                                                       # Setup the container

	for j in range( len( table_f[ :,0 ] )):                         # i range from 0 to the number of rows of "table_f"

		str_table_f.append( str( table_f[ j, 0 ] ))                 # Translate from numpy.array to string the names of
																	# profiles, in order to compare them with airfoil_f

	index_f = str_table_f.index( file_name_f + '_data.txt' )        # Return the index of airfoil_f in strings table_f

	solution_f = table_f[index_f, :]

	print('\nThe selected FLAP have Cl_max= {}, alpha= {}'.format( solution_f[2], solution_f[1] ))



else:

	print('Wrong typing, exit from program...')

	sys.exit()


#%% Overwrite value in config file

config.solution_w = solution_w

config.solution_f = solution_f

config.file_name_w = file_name_w

config.file_name_f = file_name_f



#%% Save the AoA, updated in case of lower angles, inside Hess Smith script

control_path = str( path + '/Hess-Smith/nprofili/control.txt' )           # Path of the control.txt

with open( control_path, 'r+') as controller:

	text = controller.readlines()                                         # Read the entire text and split it in lines

	text[68] = str( solution_w[1] + '\n' )                                # Update the WING AoA

	text[69] = str( solution_f[1] + '\n' )                                # Update the FLAP AoA

	controller.seek(0)                                                    # Back to the head of the file

	controller.writelines( text )                                         # Write the file, with updated AoA



#%% Header generation for the file "results.txt"

header_path = str( path + '/Hess-Smith/nprofili/header_results.txt' )           # Path of the header_results.txt

with open( header_path, 'w') as header:

	header.write('RESULTS: wing {}, flap {},'.format( file_name_w, file_name_f ))  # Write the header of results with
																				   # correct profile names



#%% Profile points selection & export module

import export_coordinates


print('\n\nCoordinates files have been saved in the /Output directory.'
      '\n\n-------------------------> Launch MATLAB® to continue the analysis <-------------------------')



input('\n\n/------------------------------------ Program stopped -------------------------------------\ '
      '\n|################### Press "enter" to launch the post processing module ###################|'
      '\n\------------------------------------------------------------------------------------------/')

import postpro
