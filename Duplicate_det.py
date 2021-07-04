# Detects duplicate, specified, files on the basis of identical file size. and deletes (or) moves them to a specified directory

import os
import shutil
import time

direct = 'C:\\DIRECTORY_HERE'
ftype = '.FILE_TPYPE'



def mB(value):
    return round(value * (10**-6),3)

def tally():
    counter = 0
    for file in os.listdir(direct):
        if file.endswith(ftype):
            counter += 1
    return counter 


Ts = time.time()


deleted = []
duplicates = 0
acc = 0
itera=0
original = tally()

for file_1 in os.listdir(direct):
    
    if file_1 in deleted:
        pass
    else:
        if file_1.endswith(ftype):
            size_1 = os.path.getsize(direct+file_1)
##        else:
##            pass

            for file_2 in os.listdir(direct):
                if file_2.endswith(ftype):
                    size_2 = os.path.getsize(direct+file_2)
                    itera += 1

                    if file_1 != file_2:       
                        if size_1 == size_2:
                            duplicates += 1
                            if duplicates == 1:
                                print('FILE 1:\t\t\t[+]\tDUPLICATE:\n'+'-'*60)
                            else:
                                pass
                            #print('duplicate found')
                            print(file_1+'\t[+]\t'+file_2)

                            change = direct+file_2
                            acc += size_2

                            #DELETE
                            os.remove(change)
                            deleted.append(file_2)
                            #print(file_2,'deleted')

                            #MOVE
                            #shutil.move(change, target)
##                        else:
##                            pass
##                    else:
##                        pass
##                else:
##                    pass
                        

end = tally()
Te = time.time()
T = (Te-Ts)/60
                            
print('\nScan Complete:')
if duplicates == 0:
    print('No duplicates were found')
else:
    print('['+str(duplicates)+']\tDuplicates found')
    print('['+str(original)+']\tfiles before Scan')
    print('['+str(end)+']\tfiles after Scan')
    print('['+str(mB(acc))+']\tMB of duplicates deleted')
    print('Process took:',str(round(T,2))+'minutes to complete')
    print('Iterations completed:',str(itera))
    
                    
        
        

        
        
        
