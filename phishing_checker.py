from urllib.parse import urlparse

def inspect url(raw_url):

***Check URL text for selected phishing warning signs.**

url raw_url.strip()

findings = []

return ["No URL entered."]

if not url:

candidate url if "://" in url else "http://" url

try: parsed urlparse(candidate) host (parsed.hostname or "").lower() except ValueError:

return ["This text is not valid URL format."]

if not host:

return ["Could not identify a hostname."]

findings.append("Contains an @ symbol; inspect carefully.")

if "@" in candidate:

findings.append("Unusually long URL (over 100 characters).")

if len(url) > 100:

if re.fullmatch(r" (?:\d(1,3)\.) (3)\d(1,3)", host): findings.append("Uses an IP address instead of a familiar domain.")

labels [part for part in host.split(".") if part]

if len(labels)> 5: findings.append("Contains many hostname segments/subdomains.")

if "xn-- in host:

findings.append("Contains a punycode-style hostname.")

if parsed.scheme.lower() "http":

findings.append("Uses HTTP, HTTPS alone does not prove trust.")

if not findings: findings.append(

"No listed warning signs found. This does NOT prove safety."


)

return findings

def main(): print("Text checks only this program does not open URLs.")

print("EWB Phishing URL Awareness Checker")

raw url input("\\nEnter a sample URL (or type q to quit): ")

while True:

if raw url.strip().lower() in ("q", "quit", "exit"): print("Goodbye! Stay alert online.") break

findings inspect_url(raw_url)

print("\\nResult:") for item in findings: print("- item)

warning prefixes ( "Contains an @",

"Unusually long URL", "Uses an IP address", "Contains many hostname", "Contains a punycode" "Uses HTTP."

warning count sum( 1 for item in findings. if item.startswith(warning prefixes)

if warning count:

print( \\nREVIEW CAREFULLY: (warning count) warning sign(s) found."

print("Never enter passwords from unexpected links.")

if_name_ main() "main":
