import ctypes
from ctypes.wintypes import LPCSTR, UINT
import os

dll = ctypes.WinDLL(os.getcwd()+"\\"+"a1800.dll")
decproto = ctypes.WINFUNCTYPE(ctypes.c_uint, LPCSTR, LPCSTR, ctypes.POINTER(UINT), UINT, UINT)
decparamflags = ((1, 'infile'), (1, 'outfile'), (2, 'fp'), (1, 'unk1', 16000), (1, 'unk2', 0))
decfunc = decproto(('dec', dll), decparamflags)

files = os.listdir('splitted')

for f in files:
    fname = 'splitted/' + f
    outfile = 'wavs/' + f + '.wav'
    print("Converting "+f+" to WAVs")
    decfunc(infile=LPCSTR(fname.encode('ascii')), outfile=LPCSTR(outfile.encode('ascii')))

print("Converted succesfully!")
