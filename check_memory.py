#!/usr/bin/env python3

# Author: Vladimir Novick , <vlad.novick@gmail.com>
#
#                          https://www.linkedin.com/in/vladimirnovick
#                      
# Date: 14.11.2016
# Purpose: check memory

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

def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
      retcode = p.poll() 
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


for line in runProcess('free -m'.split()):
    print(line)
    
print('Free size: ' + str(getFreeSize()) + ' MB')
print('\n')
    
output = subprocess.run("ps axo rss,comm,pid | sort -n | tail -n 30 | sort -rn", shell=True, stdout=subprocess.PIPE, 
                        universal_newlines=True)
print(output.stdout)



    
