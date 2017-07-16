#!/usr/bin/env python3


# Author: Vladimir Novick , <vlad.novick@gmail.com>
#
#                     https://www.linkedin.com/in/vladimirnovick
#
#                  https://github.com/Vladimir-Novick/Monitoring-Memory-Usage
#                      
#                      
# Date: 09.07.2017
# Purpose: check max using memory and create log file

#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys

print("")
print("                 MEMORY MONITOR SERVICE")
print("                 ----------------------")
print("                 memory_monitor.service")
print("")
print(" Service provide periodical check max using memory and create log file")
print("                File: /var/monitor/memory.log")
print(" ______________________________________________________________________")
print(" ")

with open('/var/monitor/memory.log', 'r') as fin:
    print(fin.read())
