# A1800RE
Here is my progress in reverse engineering. A1800 aka SACM-A1800 aka SACM-DVR1800 is audio codec that used in Furbies from 2012 to 2016 years. Here you can find scripts, roms, A1800 files and WAVs, which are converted A1800 ones. The audio and rom dump is ripped from Furby 2012.

# Header
A1800 file has 6-byte header. First four bytes are length of the audio. The next 2 bytes are "Ђ>". Interesting that in hex it's "80 3E" which is 16000 in decimal. The A1800 also uses 16000 sample rate, so this header may indicate the sample rate of the audio.

# Scripts
**Run scripts only if you want to do this on your own, with your own files!**
**You should have 32-bit version of python!**

***How To Run***

Put your own rom_dump into **"rom"** folder. It must have the **"rom_dump.bin"** name. Then delete everything from **"splitted"** and **"wavs"**. Then run **"split.py"** to split rom into small .a18 files. Then run **"convert.py"** to convert .a18 files to the WAVs.
