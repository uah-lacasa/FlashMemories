# File: 			combine.py
# Date: 			2020 May 24
# Description:	For the files listed under the list file_names
# 				.. this code combines all the files into the final file
# 				.. the output file will be named index.html
# Suggetions:		1. Make sure the name of files in the list appears in the order they are needed
# 				2. Make sure that head.html contains all the heading portions as well as the opening
# 				.. tag of body
# 				3. Body tag is close in file tail.html
# 				4. Any runnable script should be placed in the tail.html file
# 				5. The goal is to have a single html file that combines all the separate html files
# 				6. Make a list of all the filenames at the start of body section. This should link
# 				 .. to the respective section of the descrition later

# import necessary libraries
import os
import sys
import os.path

# MACROS
DEBUG = True

# the assumption is that head.html and tail.html are always named
# .. as such
# following list only lists the other files in between
file_names = [
				'nvm_introduction.html',
				'magnetic_disk.html',
				'sram.html',
				'dram.html',
				'fram.html',
				'rram.html',
				'flash.html',
				'mram.html',
				'pcm.html',
				'optane.html',
				'flash_security.html',
				'sram_dram_security.html',
				'flash_puf.html',
				'flash_sanitization_paper.html',
				'ssd_papers_study.html',
				'file_system_study.html',
				'other_study.html'
			]
# please make sure that following list contains the descriptive name of each
# .. of the files in above list
file_names_desc = [
				'NVM Introduction',
				'Magnetic Disks',
				'SRAM',
				'DRAM',
				'FRAM',
				'RRAM',
				'Flash Memory',
				'MRAM',
				'PCM',
				'Optane',
				'Security Primitives in Flash Memory',
				'Security Primitives in SRAM and DRAM',
				'Flash PUFs',
				'Sanitization of Flash Memory',
				'SSD papers',
				'Study of File Systems',
				'Others'
			]
# check the length of the two lists above
if len(file_names)!=len(file_names_desc):
	print("E: Please fix the lists \"file_names\" and list \"file_names_desc\"\n")
	print("E: .. both should have same length")
	sys.exit(-1)

# following is the name of header file
header_file = "head.html"
# following is the name of tail file
tail_file = "tail.html"
# following is the name of output file
outfile = "index.html"
# this will replace the file everytime
try:
	f_out = open(outfile,'w')
except Exception as e:
	print(f"E: Unable to open output file {outfile}. Program exits")
	print(f".. .. {str(e)}")
	sys.exit(-1)

###########################################################
############### Copy the header file section ##############
# let us first copy the contents from the header.html file
# .. test if the file exists
if os.path.exists(header_file):
	if DEBUG:
		print(f"M: file {header_file} found")
	try:
		f_in = open(header_file)

		# read entire content of header_file
		file_content = f_in.read()

		# dump the entire content to the outfile
		f_out.write(file_content)

		# close the header_file
		f_in.close()

	except Exception as e:
		print(f"E: Unable to open file {header_file}.")
		print(f".. .. {str(e)}")
		sys.exit(e)


	# now let us open the header_file and copy the content to the outfile
else:
	print(f"E: header file {header_file} not found. Program exists.")
	sys.exit(-1)


###########################################################
######## Write the name of title and name of author #######
# we should be inside the body section now
# .. so let us print the title of the write up
# .. and name of the author
# .. PLEASE CHANGE here
title_h1 = "Flash Research Comprehensive"
author = "Prawar Poudel"
contact = "prawar(dot)poudel(at)hotmail(dot)com"

# write the title
write_statement = f"\n<h1 align=\"center\">{title_h1}</h1>\n"
f_out.write(write_statement)
f_out.write("\n<hr>\n")
write_statement = f"\n<p align=\"center\">{author}</p>\n"
f_out.write(write_statement)
write_statement = f"\n<p align=\"center\">{contact}</p>\n"
f_out.write(write_statement)
f_out.write("\n<hr>\n")
f_out.write("\n<hr>\n")


###########################################################
################ Provide comprehensive info ###############
# write a button style thing that gives title
write_statement = f"\n<button type=\"button\" class=\"collapsible\"> About this document</button>\n"
f_out.write(write_statement)
write_statement = f"\n<p>\
This document contains short description about all the research items read by {author}\
during his/her course of research. The items studied can be categorized into following classes.\
</p>\n\
<p>\
Please follow the link below to jump to respective section:\
</p>\n"
f_out.write(write_statement)
# from all the file names in the list above create a navigation links for each of them
# the name of anchor should be name of file itself
f_out.write("\n<p>\n<ul>")
for idx,i in enumerate(file_names):
	f_out.write("<li>")
	anc_name = i.split(".")[0]
	f_out.write(f"<a href=\"#{anc_name}\">{file_names_desc[idx]}</a>")
	f_out.write("</li>")
f_out.write("\n</ul>\n</p>")
f_out.write("\n<hr>\n")
f_out.write("\n<hr>\n")


###########################################################
# Now create each section and copy the content from each files #
for idx,each_file in enumerate(file_names):
	# for each of the filenames we have above we will create a h2-header.
	anc_name = each_file.split(".")[0]
	f_out.write(f"\n<h2 align=\"center\"><a name=\"{anc_name}\">{file_names_desc[idx]}</a></h2>\n")
	f_out.write(f"\n<button type=\"button\" class=\"collapsible\"> <i>Please Click Here to Expand: {file_names_desc[idx]}</i></button>\n")
	# start div tag here
	f_out.write(f"\n<div class=\"content\">\n")
	
	# pull the contents from each of the files here
	if not os.path.exists(each_file):
		print(f"W: File {each_file} does not exist. Please check")
		
	else:
		if DEBUG:
			print(f"M: File {each_file} found.")
		try:
			f_in = open(each_file)
			file_content = f_in.read()

			f_out.write(file_content)

		except Exception as e:
			print(f"W: Error in opening file {each_file}.")
			print(f".. .. {str(e)}")
			

	# end div here
	f_out.write(f"\n</div>\n")
	# end with two horizontal rule line
	f_out.write("\n<hr>\n")
	f_out.write("\n<hr>\n")

###########################################################
############### Copy the tail file section ##############
# let us first copy the contents from the header.html file
# .. test if the file exists
if os.path.exists(tail_file):
	if DEBUG:
		print(f"M: file {tail_file} found")
	try:
		f_in = open(tail_file)

		# read entire content of header_file
		file_content = f_in.read()

		# dump the entire content to the outfile
		f_out.write(file_content)

		# close the tail_file
		f_in.close()

	except Exception as e:
		print(f"E: Unable to open file {tail_file}.")
		print(f".. .. {str(e)}")
		sys.exit(e)


	# now let us open the tail_file and copy the content to the outfile
else:
	print(f"E: tail file {tail_file} not found. Program exists.")
	sys.exit(-1)


# close the outfile here
f_out.close()