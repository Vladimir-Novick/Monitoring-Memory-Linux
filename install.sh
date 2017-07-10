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
echo  " Purpose: set enable memory monitor service"
echo  ""
echo  " This is a simple and free tool for monitoring system memory."
echo  ""
echo  " Service provide periodical check max using memory and create log file"
echo  "                File: /var/monitor/memory.log"
echo  ""
echo -n "Do you want to install this service (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
sudo mkdir -p /var/monitor
sudo chmod g+s /var/monitor
sudo cp -rf memory_monitor.py /var/monitor/memory_monitor.py
sudo chmod a+x /var/monitor/memory_monitor.py
sudo cp -rf memory_monitor.service /lib/systemd/system/memory_monitor.service
sudo  systemctl enable /lib/systemd/system/memory_monitor.service
sudo service memory_monitor start
service memory_monitor status
fi
