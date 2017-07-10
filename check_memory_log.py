#!/usr/bin/env python3


# Author: Vladimir Novick , <vlad.novick@gmail.com>
#
#                          https://www.linkedin.com/in/vladimirnovick
#                      
# Date: 14.11.2016
# Purpose: check memory and create log file

#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import subprocess
import sys
import datetime

logFile = "memory.log"

def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
      retcode = p.poll() #returns None while subprocess is running
      line = p.stdout.readline()
      line = line.decode("utf-8")
      yield line
      if(len(line) < 2):
        break      
      if(retcode is not None):
        break
        
        
        
    
def getFreeSize():
    p = subprocess.Popen('free -m'.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
    retcode = p.poll() #returns None while subprocess is running
    line = p.stdout.readline()
    line = p.stdout.readline().decode("utf-8") 
    r = line.split()
    return int(r[3].strip())

def writeLog(fileName):
    output = subprocess.run("ps axo rss,comm,pid | sort -n | tail -n 30 | sort -rn", shell=True, stdout=subprocess.PIPE, 
                        universal_newlines=True)
    with open(fileName, mode='a+') as out:
        all_lines =output.stdout
        records = all_lines.split('\n')
        l1 = 'Memory'.rjust(8)
        l2 = 'Task'.ljust(20)
        l3 = 'PID'.rjust(10)
        out.write(l1+ '  ' +l2+l3)
        out.write('\n')
        l1 = '------'.rjust(8)
        l2 = '----------------------'.ljust(20)
        l3 = '-----'.rjust(8)
        out.write(l1+ '  ' +l2+l3)
        out.write('\n')
        for index in range(len(records)):
           line = records[index]  
           if line != '':
              l = line.split()
              l1 = l[0].strip().rjust(8)
              l2 = l[1].strip().ljust(20)
              l3 = l[2].strip().rjust(10)
              out.write(l1+ '  ' +l2+l3)
              out.write('\n')
           else:
              break
    out.close()    
    
def writeMemoryLog(fileName):
    with open(fileName, mode='w+') as out:
        out.write(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y\n\n"))
        for line in runProcess('free -m'.split()):
           out.write(line)
           out.write('\n')
        out.close()


writeMemoryLog(logFile)
writeLog(logFile)

    
