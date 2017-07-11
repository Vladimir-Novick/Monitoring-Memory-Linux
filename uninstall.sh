#!/bin/bash
#
# Author: Vladimir Novick , <vlad.novick@gmail.com>
#
#                          https://www.linkedin.com/in/vladimirnovick
#                      
# Date: 11.07.2017
# Purpose: check max using memory and create log file
#
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
echo  ""
echo  "            MEMORY MONITOR SERVICE"
echo  ""
echo  " This is a simple and free tool for monitoring system memory."
echo  ""
echo  " Service provide periodical check max using memory and create log file"
echo  "                "
echo  ""
echo -n "Do you want to REMOVE this service (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
sudo systemctl disable memory_monitor.service
sudo systemctl daemon-reload
sleep 5
sudo service memory_monitor stop
sudo rm -rf /var/monitor/memory_monitor.py
sudo rm -rf /var/monitor/memory.log
sudo rm -rf /lib/systemd/system/memory_monitor.service

fi
