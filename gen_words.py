#/bin/sh python2.7
import math
import random
occupied_tones = 116
pilots_tones = 16
fft_length = 128     #longueur FFT
data1  = open('sync1.txt','wt') #la premiere sequence
data2  = open('sync2.txt','wt') #la deuxieme sequence
data3  = open('pilot_seqs.txt','wt') #la deuxieme sequence
zeros_on_left = int(math.ceil((fft_length - occupied_tones) / 2.0))

sfreq1 = [float(2*random.randint(0,1)-1)*float(1) for i in range(fft_length)][0:occupied_tones]
sfreq2 = [float(2*random.randint(0,1)-1)*math.sqrt(2) for i in range(fft_length)][0:occupied_tones]
sfreq3 = [float(2*random.randint(0,1)-1)*float(1) for i in range(fft_length)][0:piltos_tones]

for i in range(len(sfreq1)):
        if((zeros_on_left + i) & 1):
		sfreq1[i] = 0.0

preambles_1 = (sfreq1,)
preambles_2 = (sfreq2,)

padded_preambles_1 = list()
for pre in preambles_1:
        padded = fft_length*[0,]
        padded[zeros_on_left : zeros_on_left + occupied_tones] = pre
        padded_preambles_1.append(padded) 
data1.write(str((padded_preambles_1[0],)))      
data1.close() 

padded_preambles_2 = list()
for pre in preambles_2:
        padded = fft_length*[0,]
        padded[zeros_on_left : zeros_on_left + occupied_tones] = pre
        padded_preambles_2.append(padded)
data2.write(str((padded_preambles_2[0],))) 
data2.close()

data3.write(str(tuple(sfreq3)))


print("Done ...!")
