V=3
import os
import socket
import urllib.request
import urllib.parse
from urllib.parse import quote
try:
    import retrying
except Exception:
    print("retrying module not installed. Installing now...")
    os.system('pip install retrying')
try:
    import retrying
except Exception:
    os.system("wget https://github.com/rholder/retrying/archive/refs/tags/v1.3.3.tar.gz")
    os.system("tar -zxvf v1.3.3.tar.gz")
    os.chdir("retrying-1.3.3")
    os.system("python setup.py install")
from retrying import retry
from requests.exceptions import ConnectionError

try:
    from icmplib import ping as pinging
except Exception:
    os.system('pip install icmplib')
    from icmplib import ping as pinging


import  sys
try:
    import rich
except Exception:
    print("Rich module not installed. Installing now...")
    os.system('pip install rich')
from rich.console import Console
from rich.prompt import Prompt
from rich import print as rprint
from rich.table import Table
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed



try:
    import requests
except ImportError:
    print("Requests module not installed. Installing now...")
    os.system('pip install requests')
try:
    import requests
except ModuleNotFoundError:
    os.system('wget https://github.com/psf/requests/releases/download/v2.32.2/requests-2.32.2.tar.gz')
    os.system('tar -xzvf requests-2.32.2.tar.gz')
    os.chdir('requests-2.32.2')
    os.system('python setup.py install')
try:
    import requests
except ModuleNotFoundError:
    os.system('curl -L -o requests-2.32.2.tar.gz https://github.com/psf/requests/releases/download/v2.32.2/requests-2.32.2.tar.gz')
    os.system('tar -xzvf requests-2.32.2.tar.gz')
    os.chdir('requests-2.32.2')
    os.system('python setup.py install')
    import requests
    
results=[]
console=Console()
save_result=[]

if not os.path.exists('/storage/emulated/0/cfrange.txt'):
    	os.system('termux-setup-storage')
    	with open('/storage/emulated/0/cfrange.txt', 'w') as f:
    		f.write('#162.159.245.0:162.159.245.255\n Delete this enter an ip range you want to scan from cfexport.txt')
    		print()
    		rprint('[bold red]\n cfrange.txt  created in /storage/emulated/0/cfrange.txt !\n enter an ip range you want to scan from cfexport.txt[/bold red]')
    		exit()
def check_internet_connection():
    try:
        response = requests.get('http://www.google.com/', timeout=5)
        return True
    except requests.ConnectionError:
        return False
        
def get_ip_details(ip_address):
    ip_address=ip_address[0]
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
    	    	try:
    	    		response = requests.get(f'http://ip-api.com/json/{ip_address}',timeout=10)
    	    	except Exception:
    	    		return {'countryCode':'Non'}
    	    	return response.json()
    	    
    data = file_o()
    
    data=data['countryCode']
    
    return data
    
def info():
    console.clear()
    
    table = Table(show_header=True,title="Info", header_style="bold blue")
    table.add_column("Creator", width=15)
    
    table.add_column("contact", justify="right")
    table.add_row("arshiacomplus","1 - Telegram")
    table.add_row("arshiacomplus","2 - github")
    console.print(table)
    
    print('\nEnter a Number\n')
    options2={"1" : "open Telegram Channel", "2" : "open github ", "0":"Exit"}
    for key, value in options2.items():
    	rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    whats2 = Prompt.ask("Choose an option", choices=list(options2.keys()), default="1")
    
    if whats2=='0':
    	os.execv(sys.executable, ['python'] + sys.argv)
    elif whats2=='1':
    	os.system("termux-open-url 'https://t.me/arshia_mod_fun'")
    elif whats2=='2'   :
    	os.system("termux-open-url 'https://github.com/arshiacomplus/'")
def start_menu():
   
    options = {
        "1": "Scan ip",
        "2": "Short cut",
        '3': 'download cfexport.txt',
        '00' : 'info',
        
        "0" : "Exit"
    }
    
    if check_internet_connection()==True:
    	rprint('[bold green]Internet is available[/bold green]\n')
    else:
    	rprint('[bold red]Internet is unavailable[/bold red]\n')
    
    
    rprint("[bold red]by Telegram= @arshiacomplus[/bold red]\n")
    for key, value in options.items():
        rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    what = Prompt.ask("Choose an option", choices=list(options.keys()), default="0")
    
    return what
    
def input_p(pt ,options):
    
    os.system('clear')
    options.update({"0" : "Exit"})
    print(pt)
    for key, value in options.items():
    	rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    whats = Prompt.ask("Choose an option", choices=list(options.keys()), default="1")
    if whats=='0':
    	os.execv(sys.executable, ['python'] + sys.argv)
    return whats
    
def create_ip_range(start_ip, end_ip):
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))
    temp = start[:]
    ip_range = []

    while temp != end:
        ip_range.append('.'.join(map(str, temp)))
        temp[3] += 1
        for i2 in (3, 2, 1):
            if temp[i2] == 256:
                temp[i2] = 0
                temp[i2-1] += 1
    ip_range.append(end_ip)
    return ip_range
    
def scan_ip_port(ip ,results,loc):
    
    
    icmp=pinging(ip, count=4, interval=1, timeout=5,privileged=False)
    
    
    
    results.append((ip,loc, float(icmp.avg_rtt), icmp.packet_loss, icmp.jitter))
def main():
    global save_result
    
    os.system('clear')
    
    
    rprint('[bold green]please wait scan ip ...[/bold green]')
    range_start=[]
    range_end=[]
    if rand_or_uset=='2':
    	tc=0
    	f3=open('/storage/emulated/0/cfrange.txt', 'r')
    	b2=f3.readlines()
    	f3.close()
    	while True:
    	   
    	   
    	    
    	    
    	    
    	    try:
    	     
    	        
    
    	        for i in b2:
    	         if i !='\n':
    	     	   
    	     	    range_start.append(i[:i.index(':')])
    	     	    
    	     	    range_end.append(i[i.index(':')+1:i.index('\n')])
    	        
    	    except Exception:

    	     	
    	     	    
    	     
    	     	
    	     	rprint('[bold red]please Wait fix cfrange.txt [/bold red]')
    	     	
    	     	time.sleep(2)
    	     	
    	     	os.system('clear')
    	     	
    	     	with open('/storage/emulated/0/cfrange.txt', 'a') as ff:
    	     		ff.write('\n')
    	     	range_end=[]
    	     	range_start=[]
    	     	with open('/storage/emulated/0/cfrange.txt', 'r') as ff:
    	     		b3=ff.readlines()
    	     	try:
    	     	    for i in b3:
    	     	
    	              if i !='\n':
    	     	   
    	     	         range_start.append(i[:i.index(':')])
    	     	    
    	     	         range_end.append(i[i.index(':')+1:i.index('\n')])
    	     	except Exception:
    	     	 	rprint('[bold red]something went wrong in cfrange.txt [/bold red]')
    	     	 	exit()
    	     	rprint('[bold green]please wait scan ip...[/bold green]')
    	     	#rprint(' [bold red]Try agian [/bold red]')
#    	     	rprint(' [bold red]If not work again check cfrange.txt[/bold red]')
    	    break
    
    	     		

    	  
    		
    else:
    	range_start=['198.41.128.0','173.245.48.0','103.21.244.0','199.212.90.0','185.146.172.0','154.85.99.0','170.114.46.0','185.238.228.0','195.85.23.0','185.176.26.0','185.18.250.0']
    	range_end=['198.41.128.255','173.245.48.255','103.21.244.255','199.212.90.255','185.146.172.255','154.85.99.255','170.114.46.255','185.238.228.255','195.85.23.255','185.176.26.255','185.18.250.255']
    start_ips = range_start
    end_ips = range_end
    
   

    for start_ip, end_ip in zip(start_ips, end_ips):
        loc=get_ip_details(start_ips)
        ip_range = create_ip_range(start_ip, end_ip)
        executor=ThreadPoolExecutor(max_workers=500)
        
        try :
                
                for ip in ip_range:
                	
                	executor.submit(scan_ip_port, ip,results,loc)
                
                	
                
        except Exception as E:
        	print("Error :","E")
        finally:
        	executor.shutdown(wait=True)

    
    extended_results = []
    
    for result in results:
        ip,loc, ping ,loss_rate,jitter= result
        if ping ==0.0:
        	ping=1000
        if float(jitter)==0.0:
        	jitter=1000
        if loss_rate ==1.0 :
        	loss_rate=1000
        	
        loss_rate=loss_rate*100
        	
        combined_score = 0.5 * ping + 0.3 * loss_rate + 0.2 * jitter

        extended_results.append((ip,loc,ping, loss_rate,jitter, combined_score))
       

    sorted_results = sorted(extended_results, key=lambda x: x[5])
    
    for ip,loc, ping, loss_rate,jitter, combined_score in sorted_results:
            if Wh_save=='3':
                if int(ping) <=  int(ping_range):
                    save_result.append(ip+' | '+'ping: '+str(ping)+' packet_lose: '+str(loss_rate)+' jitter: '+str(jitter)+'\n')
            elif Wh_save=='2':
            	if int(ping) <=  int(ping_range):
            	    save_result.append(ip+'\n')
            elif Wh_save=='1':
            	if int(ping) <=  int(ping_range):
            	    save_result.append(ip+',')
    
    
    console.clear()
    table = Table(show_header=True,title="IP Scan Results", header_style="bold blue")
    table.add_column("IP", style="dim", width=15)
    table.add_column("Loc", style="dim", width=3)
    table.add_column("Ping (ms)", justify="right")
    table.add_column("Packet Loss (%)", justify="right")
    table.add_column("Jitter (ms)", justify="right")
    table.add_column("Score", justify="right")

    for ip,  loc,ping, loss_rate,jitter, combined_score in sorted_results[:10]:
        table.add_row(ip,loc,  f"{ping:.2f}" if ping else "None", f"{loss_rate:.2f}%",f"{jitter}", f"{combined_score:.2f}")

    console.print(table)

    best_result = sorted_results[0] if sorted_results else None
    if best_result and best_result[0] != "No IP":
        ip, loc,ping, loss_rate,jitter, combined_score = best_result
        try:
            console.print(f"The best IP: {ip} ,location : {loc} ,ping: {ping:.2f} ms, packet loss: {loss_rate:.2f}%, {jitter:.2f} ms ,score: {combined_score:.2f}", style="green")
        except TypeError:
            console.print(f"The best IP: {ip} ,location : {loc}  ,ping: None, packet loss: {loss_rate:.2f}% ,{jitter:.2f} ms ,  score: {combined_score:.2f}", style="green")
        ()
        best_result=[f"{ip}"]
    else:
        console.print("Try agian if something went wrong in cfrange.txt", style="red")
    if Which == '1':
        t=False
        if do_you_save=='1':
            if Wh_save =="1":
                 with open('/storage/emulated/0/result.csv' , "w") as f:
                      for j in save_result[1:]:
                          if j != "\n":
                              f.write(j)
                              t=False
                          else:
                          	
                          	    if t==False:
                          	    	 f.write(",")
                          	    t=True
                 with open('/storage/emulated/0/result.csv' , "r") as f:
                          	   b=f.readline()
                          	   with open('/storage/emulated/0/result.csv' , "w") as ff:
                          	   	ff.write(b[:len(b)-2])
                          	   	
                          	   
            elif Wh_save=='2':
                 with open('/storage/emulated/0/result.csv' , "w") as f:
                      for j in save_result:
                          f.write(j)
            elif Wh_save=='3':
                       with open('/storage/emulated/0/result.csv' , "w") as f:
                       	for i in save_result:
                       	
                       		f.write(str(i))
            print('\n saved in /storage/emulated/0/result.csv !')
if __name__ == "__main__":
    os.system('clear')
    Which=start_menu()
    if Which=='3':
    	os.system('termux-setup-storage')
    	os.system('curl -fsSL -o cfexport.txt https://raw.githubusercontent.com/arshiacomplus/Cf-Scanner-Pre/main/cfexport.txt')
    	os.system('cp cfexport.txt /storage/emulated/0/')
    	print('\n saved in /storage/emulated/0/cfexport.txt')
    	exit()
    if Which =='0':
    	exit()

    if Which=='00':
    	info()
    	exit()
    
    if Which=='2':
    

    	if os.path.exists('/data/data/com.termux/files/usr/etc/bash.bashrc_cf.bak'):
    		
    		Delete=input_p('Do you want to Delete short cut',{"1" : "Yes", "2" : "No"})
    		if Delete=='1':
    			os.system('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
    			os.rename('/data/data/com.termux/files/usr/etc/bash.bashrc_cf.bak', '/data/data/com.termux/files/usr/etc/bash.bashrc')
    			console.print("[bold red]Shortcut Deleted,  successful[/bold red]", style="red")
    
    
    		exit()
    	while True:
    		name = input("\nEnter a shortcut name : ")
    		if not name.isdigit():
    			break
    			
    		
    		else:
    			console.print("\n[bold red]Please enter a name![/bold red]", style="red")
    			
    	with open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'r') as f2:
    		txt= f2.read()
    		with open('/data/data/com.termux/files/usr/etc/bash.bashrc_cf.bak', 'w') as f:
    			f.write(txt)
    	text=f'''
{name}() {{
bash <(curl -fsSL https://raw.githubusercontent.com/arshiacomplus/Cf-Scanner-Pre/main/install.sh)
}}\n'''
    	with open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'r+') as f:
    	   	content = f.read()
    	   	f.seek(0, 0)
    	   	f.write(text.rstrip('\r\n') + '\n' + content)
    	rprint(f"\n[bold green]Please Restart your  termux and Enter [bold red]{name}[/bold red] to run script[/bold green]")
    	exit()
    if Which=='1':
    	do_you_save=input_p("Do you want to Save\n", {'1':'Yes','2':'No'})
    Wh_save=''
    if do_you_save=='2':
    	Wh_save=''
    if do_you_save=='1':
    		
    		
    		
    		os.system('termux-setup-storage')
    		Wh_save=input_p('Which type\n', {'1':'For bpb(with comma) ' ,'2' : 'For vahid pannel(with Enter)', '3' : 'with score', '4':'clean'})
    		if Wh_save=='4':
    			Wh_save=input_p('Which type\n', {'1':'For bpb(with comma) ' ,'2' : 'For vahid pannel(with Enter)'})
    			
    			
    			with open('/storage/emulated/0/result.csv', 'r') as f:
        		    b=f.readlines()
        		    with open('/storage/emulated/0/clean_result.csv', 'w') as ff:
        		        for j in b:
        		             	if Wh_save =='1':
        		             		ff.write(j[:j.index('|')-1])
        		             		if j != b[len(b)-1]:
        		             		     ff.write(',')
        		             	else:
        		             		ff.write(j[:j.index('|')-1])
        		             		ff.write('\n')
        		       	     	
    			print(' saved in /storage/emulated/0/clean_result.csv !')
    			exit()
    if Wh_save!='4':
    			ping_range=input('\nEnter Range ping (from Zero to What ?[defualt 300] : ')
    			if ping_range=='':
    			    ping_range='300'
    port=input('\nEnter a port for check IPs[defualt 443]: ')
    if port =='':
    	port='443'
    else:
    	while not port.isdigit():
    		port=input('\nEnter a port for check IPs[defualt 443]: ')
    port =int(port)
    rand_or_uset=input_p('Choose ',{'1' :'default', '2':'user/cfrange'})
    
    main()
    
