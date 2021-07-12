endpt=$(curl -X GET https://brianna-portfolio.duckdns.org)
if [[endpt -eq 200]] ; then
   exit 1
else
   exit 0

endpt=$(curl -X GET https://brianna-portfolio.duckdns.org/health)
if [[endpt -eq 200]] ; then
   exit 1
else
   exit 0

endpt=$(curl -X GET https://brianna-portfolio.duckdns.org/login)
if [[endpt -eq 200]] ; then
   exit 1
else
   exit 0

endpt=$(curl -X GET https://brianna-portfolio.duckdns.org/register)
if [[endpt -eq 200]] ; then
   exit 1
else
   exit 0