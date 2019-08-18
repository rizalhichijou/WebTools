from requests import Session

nmap = "https://api.hackertarget.com/nmap?q="
whois = "https://api.hackertarget.com/whois?q="
grab = "https://api.hackertarget.com/pagelinks?q="
dns = "https://api.hackertarget.com/dnslookup?q="
r = Session()

ba = "[*] Author : Kuina Natsukawa"
ba += "\n[*] Version : 0.1\n"
ba += "[*] Thanks for using this tool\n"
print ba

banner = """
[ * ] Command List
[1] TCP Port Scan
[2] Whois
[3] Extract Page Links
[4] DNS Lookup

[ * ] :3
"""
print banner

def main():
 global target

 try:
  type = raw_input("Command_> ")
  if type == "1":
   input()
   re = r.get(nmap+str(target))
   print re.text
   main()
  elif type == "2":
   input()
   re = r.get(whois+str(target))
   print re.text
   main()
  elif type == "3":
   input()
   re = r.get(grab+str(target))
   print re.text
   main()
  elif type == "4":
   input()
   re = r.get(dns+str(target))
   print re.text
   main()
  elif type == "help" or type == "Error":
   print banner
   main()
  
  else:
   print "[ ? ] : "+type+" : Not found"
   main()

 except:
  print "Error."
  exit()

def input():
 global target
 try:
  target = raw_input("Target_> ")

  
 except:
  print "Something went wrong"
  exit()
 

if __name__ == "__main__":
 main()