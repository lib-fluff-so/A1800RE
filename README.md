# A1800RE
Here is my progress in reverse engineering. A1800 aka SACM-A1800 aka SACM-DVR1800 is audio codec that used in Furbies from 2012 to 2016 years. Here you can find scripts, roms, A1800 files and WAVs, which are converted A1800 ones.

# Header
A1800 file has 6-byte header. First four bytes are length of the audio. The next 2 bytes are "Ђ>". Interesting that in hex it's "80 3E" which is 16000 in decimal. The A1800 also uses 16000 sample rate, so this header may indicate the sample rate of the audio.

# Scripts
All scripts are on the python. **Ensure you have 32 bit python**, because the A1800.dll is 32 bit, and python script runs it. To run "**split.py**", ensure that you have "rom_dump.bin" in "rom_dumps" folder and you have "splitted" folder. To run "**toA1800.py**" ensure that you have "A1800.dll", "wavs" folder and there's data to convert in "splitted" folder. If there's no data to convert in "splitted" folder, just run "split.py".
