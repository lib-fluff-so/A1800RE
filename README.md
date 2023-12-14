# A1800RE
Here is my progress in reverse engineering. A1800 aka SACM-A1800 aka SACM-DVR1800 is audio codec that used in Furbies from 2012 to 2016 years. Here you can find scripts, roms, A1800 files and WAVs, which are converted A1800 ones.

#Header
A1800 file has 6-byte header. First four bytes are length of the audio. The next 2 bytes is "Ђ>". Interesting that in hex it's "80 3E" which is 16000 in decimal. The A1800 also uses 16000 sample rate, so this header may indicate the sample rate of the audio.
*This is all the header*
