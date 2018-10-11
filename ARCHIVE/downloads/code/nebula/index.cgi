#!/usr/bin/perl

use CGI qw{param};

print "Content-type: text/html\n\n";

sub ping {
	$host = $_[0];

	print("<html><head><title>Ping results</title></head><body><pre>");

	@output = `ping -c 3 $host 2>&1`;
	foreach $line (@output) { print "$line"; } 

	print("</pre></body></html>");
	
}

# check if Host set. if not, display normal page, etc

ping(param("Host"));

