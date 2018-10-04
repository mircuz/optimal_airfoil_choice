"""Module used to import the polar data"""
#%% Import section

import numpy as np

import glob

import config;      path = config.path

import os



#%% Select project path & overwrite in config file

path = os.getcwd()

config.path = path                                         # Overwrite in config file

path_P = str(path +'/Polar Data/*.txt')                        # Format needed by glob.glob



#%% istruction needed by module glob

data = glob.glob( path_P )



#%% Vector setup

Cl_max = []

E_max = []

a_Cl = []

a_E = []

profile = []



Cl_max_f = []

a_Cl_f = []

profile_f = []



#%% Set maximum AoA_input for the main wing

AoA_input = (float(input('Set maximum angle of attack for the main wing. Only integers and integers+0.5 supported: ')))

AoA = AoA_input

#%% Data import & subdivision in vectors

for name in data:

		# vector creation, starting from row number 2

		current_data = str( name )

		a,Cl,Cd,E,Cm = np.loadtxt( current_data, skiprows= 2, unpack=True )


		a_f, Cl_f, Cd_f, E_f, Cm_f = np.loadtxt(current_data, skiprows=2, unpack=True)



		# Lower the angle of attack in case of profile doesn't have the requested one

		index_tuple = np.where(a == AoA)



		val = config.index_tuple_check( index_tuple[0] , AoA, path, name, a )

		index = int( val ) + 1           # Extract from the tuple the index which identifies the AoA



		# Select the maximum bounded between 0 and index for the wing

		E_max.append( float(max( E[:index] )) )                              # E[:index] ensure values bounded

		a_E.append( float(a[ list( E[:index] ).index( max( E[:index] ) )]))

		profile.append( str( name[ (path.count('') + 11) :] ))          # "path.count('')+11" used as index to catch
																		# the correct profile name, independently from
																		# path in which files are located

		Cl_max.append( float(max( Cl[:index] )))

		a_Cl.append( float(a[ list( Cl[:index] ).index( max( Cl[:index] ))]))

		AoA= AoA_input                                                       # Needed to erase the previous value





		# vectors of the maximum for the flap

		Cl_max_f.append(float(max(Cl)))

		a_Cl_f.append(float(a[list(Cl).index(max(Cl))]))

		profile_f.append(str(name[(path.count('') + 11):]))              # "path.count('')+11" used as index to catch
														                 # the correct profile name, independently from
														                 # path in which files are located

#%% Table creation, readable from the main, which have all the necessary values

table_w = [ profile, a_Cl, Cl_max, a_E, E_max ]

table_f = [ profile_f, a_Cl_f, Cl_max_f ]



# ndarray, T used to Transpose

table_w = np.array(table_w).T

table_f = np.array(table_f).T



#%% Overwrite value in config file

config.table_w = table_w

config.table_f = table_f

config.AoA = AoA



#%% Want you to show your database?

chooser = input('Type "y" to show the available profile list, else press "enter": ')


if chooser == 'y':

	print('\n\nReasume table with the best features for the wing \n [profile,    alpha_Cl,   Cl,     alpha_E,    E\n')

	print(table_w, ' \n\n')

	print('\n\nReasume table with the best features for the flap \n [profile_f,    alpha_Cl_f,   Cl_f\n')

	print(table_f, ' \n\n')

else:

	print('Profile data not shown')

