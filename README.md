# vetty

Application details:
1. Application have single GET route.
2. On call to this route application need to read content of given file (see file1.txt.. file4.txt) 
and render properly it in HTML page. Any markup should be preserved.
(files are in English, file 4 contains some Chinese)
3. Endpoint accept target file name as optional variable part of URL and default to 
file1.txt.
4. Endpoint accept optional URL query parameters to specify start line number and 
end line number. If those parameters present – return only part of file between specified line 
numbers. If parameters absent – return all lines.
5. All most likely exceptions in application logic should be handled gracefully. When 
exception happens error page should be displayed with exception details.
