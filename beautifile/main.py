import os, shutil
from termcolor import colored as clr
from beautifile.extensions import *

def organize_files(files):
	for file in files:
		extension = file.split('.')[-1]
		folder = ''
		
		if extension in font_extensions: folder = 'Fonts'
		elif extension in image_extensions: folder = 'Images'
		elif extension in audio_extensions: folder = 'Audios'
		elif extension in video_extensions: folder = 'Videos'
		elif extension in archive_extensions: folder = 'Archives'
		elif extension in document_extensions: folder = 'Documents'
		elif extension in application_extensions: folder = 'Applications'
		elif extension in code_extensions: folder = 'Codes'
		
		os.makedirs(folder, exist_ok=True)
		print(clr(f'Moving {file} to {folder}', 'yellow'))
		shutil.move(file, folder)
	print(clr('Directory organized!', 'green'))
	
def main():
	all_files = os.listdir()
	filtered_files = [file for file in all_files if file.split('.')[-1] in all_extensions]
	organize_files(filtered_files)
	
if __name__ == '__main__':
	main()