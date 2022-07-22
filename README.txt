This script is used to:

1. Group files to Year/Month folders
2. Check for duplicate files by checking the Last Modified Date (Delete duplicates)
 
INSTRUCTIONS:
1. Place the script on the same folder of images or images' folder



Plan:

1. Get modified time for each file
  - os.walk on each directory
  - createdir() on each file
2. Create directories for each Year and Months inside Year directories.
3. Move each files by Year and Month on their respective directories.
4. Delete files with the same modified date using the exact `hour:minute:second` from modified date.