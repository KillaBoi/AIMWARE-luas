import os,sys
folder = ('DIR')
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.nav', '.dat')
       output = os.rename(infilename, newname)
