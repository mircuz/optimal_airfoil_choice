"""Export module"""
#%% Import module

import config;      solution_w = config.solution_w;       solution_f = config.solution_f;

path = config.path; file_name_w = config.file_name_w;     file_name_f = config.file_name_f

import os



#%%                                         WING
# Set path of Coordinates and code to search by itself the file based on main output

print('\n\nSearching for the coordinates of',file_name_w, 'in')

path_C_w = str( path + '/Coordinates/' + file_name_w + '.txt' )

print( path_C_w )



#%% Operation on txt of the WING

with open(path_C_w) as p_points_text:



	# Print that file has been found

	print(file_name_w, 'coordinates has been found!!')



	# Reading file

	p_points_read_w = p_points_text.read()



	# Separate upper profile points from lower profile points

	p_points_up_w, p_points_dw_w = p_points_read_w.rsplit( sep='Lower X \tLower Y' , maxsplit= 3)



	# Generate a container in which I can put my upper files, so that I can READ them LINE by LINE

	path_T_w = str(path + '/Temp/Wing/temp.txt')

	temp_w = open(path_T_w, 'w')

	temp_w.write(p_points_up_w)
	temp_w.close()



	# Read the container LINE by LINE

	temp_txt_w = open(path_T_w)

	data_list_w = temp_txt_w.readlines()



	# Delete the header

	del data_list_w[0:3]



#%%                                         FLAP
# Set path of Coordinates and code to search by itself the file based on main output

print('\n\nSearching for the coordinates of',file_name_f, 'in')

path_C_f = str( path + '/Coordinates/' + file_name_f + '.txt' )

print( path_C_f )



#%% Operation on txt of the FLAP

with open(path_C_f) as p_points_text_f:



	# Print that file has been found

	print(file_name_f, 'coordinates has been found!!')



	# Reading file

	p_points_read_f = p_points_text_f.read()



	# Separate upper profile points from lower profile points

	p_points_up_f, p_points_dw_f = p_points_read_f.rsplit( sep='Lower X \tLower Y' , maxsplit= 3)



	# Generate a container in which I can put my upper files, so that I can READ them LINE by LINE

	path_T_f = str(path + '/Temp/Flap/temp.txt')

	temp_f = open(path_T_f, 'w')

	temp_f.write( p_points_up_f )
	temp_f.close()



	# Read the container LINE by LINE

	temp_txt_f = open( path_T_f )

	data_list_f = temp_txt_f.readlines()



	# Delete the header

	del data_list_f[0:3]



#%%  Write on txt & Export files

path_O = str( path + '/Hess-Smith/nprofili/')

txt_dw_w = open( path_O + 'points_dw_w.txt', 'w' )

txt_dw_w.write( p_points_dw_w )

txt_dw_w.close()

txt_up_w = open( path_O + 'points_up_w.txt', 'w' )

txt_up_w.writelines( data_list_w )

txt_up_w.close()



txt_dw_f = open( path_O + 'points_dw_f.txt', 'w' )

txt_dw_f.write( p_points_dw_f )

txt_dw_f.close()

txt_up_f = open( path_O + 'points_up_f.txt', 'w' )

txt_up_f.writelines( data_list_f )

txt_up_f.close()


#%% Remove temporary data

os.remove( path_T_w )

os.remove( path_T_f )

