## Description:
The reset_swapfile program creates or recreates the swapfile.

## Running the program:
python3 reset_swapfile.py 2048

"2048" - is the default size of the generated swapfile. You specify your file size.

### If a swap partition was created earlier, then you need in the console:
    1. Open the fstab file for editing:
         sudo nano /etc/fstab
    2. Comment out the swap section.
         At the beginning of the swap section line, write the # symbol
    3. Add a line:
         /swapfile none swap sw 0 0
    4. Save changes to the file:
         <Ctrl+O>
    5. Exit the editor:
         <Ctrl+X>
    6. Start the program.
