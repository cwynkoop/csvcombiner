import chunk
import sys
import pandas as pd


def main():
    script = sys.argv[0]
    #allows as many csv to combine as possible
    for filename in sys.argv[1:]:
        #create iterator so that I know when I have first chunk in each file
        i = 1
        #create context manager to allocate resources to prevent memory limit
        with pd.read_csv(filename, chunksize = 10000) as reader:
            for chunk in reader:
                #convert filename to string and cut it to the part after last /
                name = str(filename)
                chunk['filename']=name[name.rindex('/')+1:]
                #keep header if first file otherwise do not keep header
                if filename == sys.argv[1] and i == 1:
                    chunk.to_csv(sys.stdout,index=False, mode='a',line_terminator='\n',header=True)
                else:
                    chunk.to_csv(sys.stdout,index=False, mode='a',line_terminator='\n',header=False)
                i = i+1

if __name__ == '__main__':
   main()