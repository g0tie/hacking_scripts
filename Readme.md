# Hacking scripts for pentest
## Scripts I've made when playing on HackTheBox, TryHackMe 

### Python
- **ToJavaPayload.py**: Convert a string or command to java payload for SSTI on template engine like Thymeleaf
- **generateALphabet.py**: Generate alphabet lowercase or uppercase can use ">" bash operator to output on a document
- **testUserAgents.py**: Make request with custom user-agent based on a text list passed as argument to test server responses 
- **crackMD5bySalt.py**: Crack MD5 hash with known salt using a wordlist 

### Bash
- **lower_name_permutations.sh**: Script to generate a new wordlist of lowercase username permutations based on an existing username wordlist
- **ssrf_portscan.sh**: Script to make internal localhost portscan on webserver vulnerable to SSRF
