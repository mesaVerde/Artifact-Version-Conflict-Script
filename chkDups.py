#!/usr/bin/env python

import os, re, subprocess, optparse

parser = optparse.OptionParser(description='Process version conflicts.')
parser.add_option('-t','--test', action='store_true', help=optparse.SUPPRESS_HELP)
parser.add_option('-d','--direction', action='store',
         help='Specify whether to increment or decrement the version.   Default is increment', choices=['increment', 'decrement'])
parser.add_option('-c','--compare', action='store',
         help='Specify the version depth to begin comparing.  Default is major (i.e. non-gems)', choices=['major', 'minor'])
parser.add_option('-w','--workdir', action='store',
         help='Specify the directory to resolve conflicts.  Default is /web/docs/', 
         choices=['/web/docs/', '/web/config/'])
parser.disable_interspersed_args()
parser.set_defaults(workdir='/web/docs/', compare='major', direction='increment')
(options,args) = parser.parse_args()
workdir=options.workdir
test=options.test
compare=options.compare
direction=options.direction

if __name__ == '__main__' :    
    newList = []
    alreadyRemoved=[]
    myDict = {}
    cmpDict = {}
    myList=os.listdir(workdir)
    
    def append_func():
         newList.append(myString)
    
    def removeFunc(version,cmpversion,workdir,name_and_ver):
     if (direction == 'increment'):
        rmFile=str(name_and_ver[cmpversion].keys()) ; rmFile=re.sub('[\[\]\']','',rmFile) ; workdir +=rmFile ; name_and_ver[cmpversion].keys().pop()
     elif (direction == 'decrement'):
        rmFile=str(name_and_ver[version].keys()) ; rmFile=re.sub('[\[\]\']','',rmFile) ; workdir +=rmFile ; name_and_ver[version].keys().pop()

     if workdir not in alreadyRemoved:
      #print("versions found:",versionCount)
      if test:
         #print('TEST-MODE rm -Rf ' + workdir)
         alreadyRemoved.append(workdir)
      elif not test:
         print('--> REMOVING ' + workdir)
         try:
          CMD=subprocess.check_call('rm -Rf ' + workdir,shell=True)
          alreadyRemoved.append(workdir)
         except subprocess.CalledProcessError: print('Failed to remove conflicting artifacts.') ; exit(1)

    for myString in myList:
      if myString.endswith('ear'):
       append_func()
      elif myString.endswith('jar'):
       append_func()
      elif myString.endswith('war'):
       append_func()

    del myList

    for myString in newList:
      origString=str(myString)
      myString=myString.replace('v','') 
      myString=myString.replace('-','.') 
      #The GDL59 line below will only be necessary if GDL59.war is ever versioned.
      myString=myString.replace('GDL59','GDL')
      myString=myString.replace('SNAPSHOT','')
      version=re.findall('[0-9]+\.',myString)
      verlen=len(version)
      myString=myString.replace('.','') 
      myString=myString.upper()
      myString=myString.rstrip('[EJW]AR')
      myString=re.sub('[0-9]','',myString) 
      myString=myString.replace('MONITORINGJBOSS','MONITORING')
      myString=myString.replace('MONITORINGTOMCAT','MONITORING')
      #print(myString,origString,version) ; continue
      for short in range(9-verlen):
       version.append(0)
      if myString in myDict:
       myDict[myString].append({origString:version})

      elif myString not in myDict:
       myDict[myString]=[]
       myDict[myString].append({origString:version})

    del newList

    for key, value in myDict.items():
     cmpDict[key]=value

    for cmpName,name_and_ver in myDict.items() :

     versionCount=(len(name_and_ver))
    
     if (versionCount <= 1):
      #print("skipping", cmpName)
      pass #Only 1 version of the file exists or file is non-versioned, therefore no further action required.
     elif (versionCount > 1):
      for version in range(versionCount) :
       try:
         #print(cmpName,name_and_ver[version])
         #print(name_and_ver[version].keys(),name_and_ver[version].values())
         myNums1=list(name_and_ver[version].values()).pop(0) 
         A0=myNums1[0]
         A1=myNums1[1]
         A2=myNums1[2]
         A3=myNums1[3]
         A4=myNums1[4]
         A5=myNums1[5]
         A6=myNums1[6]
         A7=myNums1[7]
         A8=myNums1[8]
       except IndexError: print("IndexError-1!!!!"); exit(1) #This exception should never occur.

       for baseName,base_name_and_ver in cmpDict.items() :
        if cmpName != baseName: continue #Artifacts are not the same, so don't try to compare them--continue with next iteration.
        cmpversionCount=(len(base_name_and_ver))
        if (cmpversionCount <= 1):
        #print("skipping", baseName)
         pass #Only 1 version of the file exists or file is non-versioned, therefore no further action required.
        elif (cmpversionCount > 1):
         for cmpversion in range(cmpversionCount) :
          try:
            #print(baseName,base_name_and_ver[cmpversion])
            #print(base_name_and_ver[cmpversion].keys(),name_and_ver[cmpversion].values())
            myNums2=list(base_name_and_ver[cmpversion].values()).pop(0)
            B0=myNums2[0]
            B1=myNums2[1]
            B2=myNums2[2]
            B3=myNums2[3]
            B4=myNums2[4]
            B5=myNums2[5]
            B6=myNums2[6]
            B7=myNums2[7]
            B8=myNums2[8]
          except IndexError: print("IndexError-2!!!!"); exit(1) #This exception should never occur.

          if (compare == 'major'):
           if float(A0) > float(B0):
            removeFunc(version,cmpversion,workdir,name_and_ver)
           elif float(A0) < float(B0):
            pass
           elif float(A1) > float(B1):
            removeFunc(version,cmpversion,workdir,name_and_ver)
           elif float(A1) < float(B1):
            pass
           elif float(A2) > float(B2):
            removeFunc(version,cmpversion,workdir,name_and_ver)
           elif float(A2) < float(B2):
            pass
           elif float(A3) > float(B3):
            removeFunc(version,cmpversion,workdir,name_and_ver)
           elif float(A3) < float(B3):
            pass
           elif float(A4) > float(B4):
            removeFunc(version,cmpversion,workdir,name_and_ver)
           elif float(A4) < float(B4):
            pass
           elif float(A5) > float(B5):
            removeFunc(version,cmpversion,workdir,name_and_ver)
           elif float(A5) < float(B5):
            pass
           elif float(A6) > float(B6):
            removeFunc(version,cmpversion,workdir,name_and_ver)
           elif float(A6) < float(B6):
            pass
           elif float(A7) > float(B7):
            removeFunc(version,cmpversion,workdir,name_and_ver)
           elif float(A7) < float(B7):
            pass
           elif float(A8) > float(B8):
            removeFunc(version,cmpversion,workdir,name_and_ver)
           elif float(A8) < float(B8):
            pass

          if (compare == 'minor'): #USED FOR APPLICATIONS THAT ALLOW MULTIPLE SERVICE VERSIONS
           if float(A0) > float(B0):
            if cmpName == 'MONITORING' : removeFunc(version,cmpversion,workdir,name_and_ver)
            else: pass #MULTIPLE MAJOR VERSIONS ALLOWED
           elif float(A0) < float(B0): pass
           elif float(A0) == float(B0):
            if float(A1) > float(B1):
             if cmpName == 'MONITORING' : removeFunc(version,cmpversion,workdir,name_and_ver)
             else: pass #MULTIPLE MINOR VERSIONS ALLOWED
            if float(A1) < float(B1): pass
            elif float(A1) == float(B1):
              if float(A2) > float(B2):
               removeFunc(version,cmpversion,workdir,name_and_ver)
              elif float(A2) < float(B2): pass
              elif float(A3) > float(B3):
               removeFunc(version,cmpversion,workdir,name_and_ver)
              elif float(A3) < float(B3): pass
              elif float(A4) > float(B4):
               removeFunc(version,cmpversion,workdir,name_and_ver)
              elif float(A4) < float(B4): pass
              elif float(A5) > float(B5):
               removeFunc(version,cmpversion,workdir,name_and_ver)
              elif float(A5) < float(B5): pass
              elif float(A6) > float(B6):
               removeFunc(version,cmpversion,workdir,name_and_ver)
              elif float(A6) < float(B6): pass
              elif float(A7) > float(B7):
               removeFunc(version,cmpversion,workdir,name_and_ver)
              elif float(A7) < float(B7): pass
              elif float(A8) > float(B8):
               removeFunc(version,cmpversion,workdir,name_and_ver)
              elif float(A8) < float(B8): pass

          if test: 
           if float(A0) > float(B0):
             print(A0 , " > ", B0)
           elif float(A0) < float(B0):
            print(A0 , " < ", B0)
           elif float(A1) > float(B1):
            print(A1 , " > ", B1)
           elif float(A1) < float(B1):
            print(A1 , " < ", B1)
           elif float(A2) > float(B2):
            print(A2 ," > ", B2)
           elif float(A2) < float(B2):
            print(A2 ," < ", B2)
           elif float(A3) > float(B3):
            print(A3 ," > ", B3)
           elif float(A3) < float(B3):
            print(A3 ," < ", B3)
           elif float(A4) > float(B4):
            print(A4 ," > ", B4)
           elif float(A4) < float(B4):
            print(A4 ," < ", B4)
           elif float(A5) > float(B5):
            print(A5 ," > ",B5)
           elif float(A5) < float(B5):
            print(A5 ," < ",B5)
           elif float(A6) > float(B6):
            print(A6 ," > ",B6)
           elif float(A6) < float(B6):
            print(A6 ," < ",B6)
           elif float(A7) > float(B7):
            print(A7 ," > ",B7)
           elif float(A7) < float(B7):
            print(A7 ," < ",B7)
           elif float(A8) > float(B8):
            print(A8 ," > ",B8)
           elif float(A8) < float(B8):
            print(A8 ," < ",B8)

