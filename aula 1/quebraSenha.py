from collections import Counter

inicioDoAlfabeto = ord(' ')
tamanhoDoAlfabeto = ord('z')-inicioDoAlfabeto+1
#suposicao do ' ' ser mais frequente
caractereMaisComum = ord(' ') - inicioDoAlfabeto

#32->122

#texto = input()
texto = "mV:f3b1q9\\5!*V4p8b;j:b)n+[O!)V6t+J<f:\\:!'K1q/Z+j4NCf2P</A*:b9b8s+[1v3b-s5ZCr;P;!,L=h/H<!,H+j2P;j9pCT;Z8f4K1t9LCg8P6h/S4bAZ+f2L:j9X=fAK7m5YCj4b)d)\\5t'UQ!nH-d+U)tAK7m5YCb8J=-AL/f9[)tAJ7n3V,pAQ=t:VCo+JO!8\\<s;TCd;Y;v9b;b6P-oObqv2S)nAL/f9[)tAL4j:b5f:\\;-A]-o+U)u/ZCf2L5f4[=nAH=h;LCe/N6j9Z1nAZ-eObloAZ1uAH5f:b6f7\\-!)V6h;LO!:P6d/K=o:b6j9PCo5UO!9V,b2L;!'U<fObvf*b6f)b.f2P;!+\\Cq;Y=tAV:o'Y-!'S1r;L</A5=m2H5!;S<s/J-tMb<v8W1tA\\<!<L0j)\\4bAJ7o9L9v'[O!3PCm/N=m'b=m2H5d5Y8f8b,v/nCbA[-n6V:!*V4p8b;f3b1eAL4j:pCE5U-dAZ-n6L:!'U<fAL=j9T7eAH:d;b4b)P6j'nCw/[)fAM-s3L6u;TCo/Z4!2V*p8[1tObxuAX=j9b)d)\\5t'UCe;PO!4V6!3H<u/ZCv8U)/A<<!0\\;u5b,j'TO!9L5q+YCo+JCq2H+f8H<!+N-uMb=m:Y1d/L;!+N-uAZ-nObfs'ZCn'S-t;H,bAU=m2HCw/[)fAV,j5b+p3T7e5b8m'J-s'[Q!r\\1t7\\-!)V6h;LCv:b6f7\\-!'b8m'J-s'[Q!o\\6dAW=m<P6b8b4j(L:pAZ1uAH5f:b4b)P6j'b<f3W=tObdf4L)oAH4j7\\-uAS)p8L-uAZ)q/L6!<P<b+b<j4J1e;U</A-=t)LCbA[:j9[1r;LCu5Y<p8nCb)b<s/Z<j7\\-!'\\/v+pCV:b)dAZ)q/L6!(S)o*P<-AW=m<P6b8b,p2V:!4L+-A\\4u8P+f9b4j(L:pObiv9J-!/U<f8K=nAP8t;TCbAH=d:V:!-Y)w/K)/A=-t:P*v2\\5!'U<fAP8t;TCq8P5j9b1oAM)v)P*v9b7s)PCm;J<v9b-uA\\4u8P+f9b8p9\\-s+b+v(P4j'bfv8H-<A:-eAV:o'Y-!2L+u;ZCo/Z4-AL<!6L4m+U<f9X=fAP8t;TCf,M1d/[=sAP6/A<<!<L;u/I=m;TCr;P;!2P*f8VCt/[Cb3L<!<L;u/I=m;TQ!qY)f9L6uAL/f9[)tAT7m2P;!6V:u'pCG;Z+fA[7s:V:!0\\;u5nCt5S4j)P<v*P6!9L,!3H;t'b-uMb.f;N1b:b<j4J1e;U<!7\\)nObpb;Y1tAU7oA[:j9[1r;LCm+VO!9L,!)V6h;LCn+[=tObqb3b-uAK1d:\\5!4P;mMb-uAW4b)L:b:b5b9Z)/A7:b+Z-o:b-h+Z<b9b9v'TCv:b>p2\\<q'[Ce/J<v3pCE5U-dAZ-n6L:!2P*f8VCj4b5b;Y1tAH=d:V:!'S1r;L</A(4j7\\)nAW7s:HO!0\\;u5b6p4b4v)[=tA[1o)P,v4[O!*P)nAL4j:b-m+P.f4KCo/I0-AHCc/I-o*\\5!,L4j9b5b9Z)!7\\1tAL:b:pCN5Y*jAP6!2H+j4P)!*V4p8pCE;P;!9P<!'T-uAV,j5b-h+[Cs/Z=tAP5q+Y,j+[Cb2P9v+[Q!d\\:b(P<v8b>f4L6b:P;!3L<v9b;f3nCo5UCt;Z+j6P<!5Y+jAP6u+Y,v3b6p4pCD8H;!(S)o*P<!'S1r;L<!'S1r;L</A06u+N-sAW:f:P=nAU-r;LCp*P7-A\\<!3V4f9[1fAT)h4HCj4[-s*\\5!;[Q!o\\4m'TCg+Y5f4[=nA[7s:V:!<L4!<L;u/I=m;TCu/U+j*\\6uObsf2S-o:L;r;LCd5T5p*VCi+U,s+Y1uAQ=t:VO!7\\1tAW4b)L:b:b-s5ZQ!qY7j4b.f;N1b:b>f9[1c;S=nAZ7m2P+j:\\,j4pCJ4b0b)b0b(P<b9Z-!6S)u+HCe/J<v3Z</A+=j9b>j:H-!/H+v2P;!+U1nObqv2S)!,H+j2P;jObss5P6!9\\;d/W1uA[-m2\\;!2V:f3nCw+O1d;S)!3H@j3\\;!+S1uA\\4u8P+j+ZCq.H:f:Y)/A:-eAZ-eAT1!7\\)nObqv4JCw/[)fAU-r;LCd5U;f7\\)uMb5b:[1tAS1h;S)!/UO!:Y1t:P9v+b-t:pCE5U-dAT)m+Z=b*HCr;P;!+Y7tAP6u+Y,v3b1n6L:e/L</A7-m2L6u+Z9v+b6p4b7s)PCe/H5/A4)f)L6b9b-g,P+j:\\:!<L;u/I=m;TCm+J<v9b6p4b;d+S-s/Z9v+pCB+U-b4b>j<L:s'b<f2S=tA\\<!6V:u'b;p*H4f9pCR;P;r;LCq+S4f4[-t7\\-!'[Cm/N=m'b1oAP6u+Y,v3pCN'L+f4H;!+\\Cj4[-s*\\5!'U<fObdf4L)oA]-o+U)u/ZCe5S7sA]7m;[8b:b4b)\\;!<H:j;ZCd5U,j3L6u;TQ!eV6f)b)v)[7sAT1!<L4!9L5q+YCb)J=n9H6/A:=t6L6e/Z;fAT7m2P;!8P;v9b)dAU1t/b,j-U1t9P5!'\\+u5YQ!dY)tAH<!6V;v+Y-!5K1pObfv8H*j:\\:!<P<b+b-s5ZCv:b)v-\\-!<L;u/I=m;TCf2L1g+U,/A=-t:P*v2\\5!9\\;d/W1uAU1t2b)uAM1o/I=tAW:f:P=nObqb3b6v2S)!*\\1-AS7c5Y<j9b-h+[Cm/N=m'b)d)\\5t'UO!<L6f4H<j9b1n6L:e/L<!4P;mObdm/X=b3b5b2L;v'K)!+Y)uAP6!*P)nAZ-n6L:!;S<s/J1f9pCW+Z<j(\\4v3b=uAU1t/b-h+[Cu+S4v9b>j<L:s'b1b)\\4j9b9v/ZCt/[Cb3L<!+Z</A+7o+JCn'_1n;ZCo+X=fA]1u'LCf8H<!6V;v+Y-!)V6w'S4j9pCN5Y*jAS)d/U1bAS)d;ZCw5S=u6H<-AI1c+U,v3b1q9\\5!9P<!'T-uMb.b)P4j9P;!*V4p8pCW+Z<j(\\4v3b;v9J1q/[Cm5Y-nAK7m5YO!7\\1tAJ7o-\\-!4\\4m'b=m:Y1d+ZCr;P;/A70b9L4m;ZCj4b2v9[7!<L4!2H+v9b<j4J1e;U<!<L;u/I=m;TQ!t\\;q+U,j9Z-!<L4!0\\;u5b;j:b)n+[Ce;PCw+Z<j(\\4v3b=m2H5d5Y8f8b)!2H+j4P)!+U1nObqv4JCv2[:j)P-tAT)t9HCbA]-m/[Cg8P6h/S4bA]-o+U)u/ZQ!wP>b3\\;!/UCd5U,j3L6u;TCm+VQ!nV:c/b)dAZ7e'S-tAV,j5nCj*b-m+P.f4KCm/I-s5pCQ.H;f2S=tAT)y/T=tAP6!4P*iAX=j9b)v)[7sObloAM)d/S1t/ZCu5Y<p8b)uAL@!)V6t+X=b:b.s/U/j2S)/A+=j9b.b;J1c;ZCw;S8v:H<fA\\:o'b<j4J1e;U<!(S)o*P</A+=j9b8v8\\;!2H+v9nCf2L1g+U,!'S1r;H5!*P)nA]1u'LO!6L4m+U<f9X=fAW7t;L:fAK7m5YQ!nV:c/b-v/Z5p*b=m2H5d5Y8f8b<f2S=tAL=!3H<u/ZQ!qO)t+S4v9b8m'J-s'[Cf8V;!'JCm+VCq5Z=f8LCq8L<j;TQ!nH=s/ZCr;P;!,L4j9b>b8P=tMb7s4H:fAL6j3b-uMb<s/Z<j7\\-!3PQ!wL;u/I=m;TCm;J<v9b-uAW=s;ZCt/[Cb3L<!8O7o)\\;/A*4b9ZCb6[-o:b<b)P<jAZ7d/V;r;b)eAS1u5Y)!:V:r;L6uAW-sAJ7o;I1bAU7t:Y)-AW-sAP6d+W<p9b0j3L6b+V;/A4)v8P;!4V6!6S)d+Y)uAH=h;LQ!mV:f3b1q9\\5!*V4p8b;j:b)n+[O!)V6t+J<f:\\:!'K1q/Z+j4NCf2P</A5)nAL=!<H:j;ZCn'Z;bMb>f2b)m/X=b3b6j9PQ!qY)f9L6uAN:b<P,bA])s/\\;!,P6j(\\;/A70b9L4m;ZCn/b:j9\\;-AI4b4K1uAZ-eAU1t/b-uMb+v8Z=tAH=d:V:!+Z</A*=s'I1u;YCbAU1t/b9v'TQ!jUCd;Y;v9b5b;Y1tAU1t/nCw'Y1v9b/s']1e'b;f3b8i'Y-u8HCj4pCW+Z<j(\\4v3b9v/ZCk;Z<pAS7s+TQ!o\\6dAI1c+U,v3b;p*H4f9b1b)\\4j9pCN'L+f4H;!,H+j2P;j9b8v8\\;!:P6d/K=o:b5b9Z)!(S)o*P<!6V:u:P<p8pCF:P)nAW=m<P6b8b8p8[)!2V*p8[1tObss'L;f4[Cd5U;f)[-u;YCu8P;u/X=fA[=s6P;-AU-dAM)v)P*v9b<f2S=tAT7m2P;!<L4/A+=j9b-vAU1t2b,j'TQ!r\\1t7\\-!4L+!4\\4m'b1n6L:e/L<-AY0p4J=tAQ=t:VCt+KO!<H:j;ZCm5Y-nObvf*b.f8T-o:\\5!'[Co/Z4!4V6!-Y)w/K)/A7:b+Z-o:b-h+[Ce;PCp8J1/A4)v8P;!<P<b+b.b;J1c;ZCo;U+/A:=t6L6e/Z;fAX=b3b4b)\\;-AL.g/J1u;YCt/[Cb3L<!:P6d/K=o:b-vMb+v8Z=tAK1d:\\5!+Z</A06u+N-sAW-m2L6u+Z9v+b8v2]1o'YCf8H<!/KCj3W-s*P-uObsf2S-o:L;r;LCg/U1c;ZCb2P9v+[Cq5Y<bObqb3b6p4b;b6P-oA]-mA[-m2\\;!'S1r;L<!9J-m+Y1t7\\-!'[Cr;P;!'\\/v+pCN5Y*jAZ7e'S-tA]-o+U)u/ZCb8J=/A+7o+JCf4P5!2P/v2HO!'S1r;H5!;[Ce5S7sAZ-eMb5p2L;u/LCw'Y1v9b8v8\\;/A06u+N-sAZ-eAL:p9b.b;J1c;ZCm/I-s5b5b>P5v9b*j(L6e;TCb)b1oAT-u;ZQ!d\\:b(P<v8b5p2S1tMb4f)[=tA\\<!2H+j4P)!)\\:t;ZO!;Y6bAV:d/b=m:Y1d+ZCb4[--AH<!<L0j)\\4bAK1b3b-s'[Co+JCf9[Q!pY+jA])s/\\;!4H<p7\\-!6L6b:P*v9b-uAT)h4P;!*P;!6H:u;Y1f4[Cn5U<f9nCo'Z+f:\\:!8P,j)\\4v9b5v9pCO;S4bAM)d/S1t/pCV:b1eAL;uAU1t/pCD8H;!<P>f8Y)!'JCe5S7sAHCv2S)n)V:q+YQ!oH5!,L:n+U<v3b5p2L;u/LCf9[O!7\\1tAS)p8L-uAS-d:\\;!+N-t:H;!+[Q!g\\;d+b>f2b6j9SCt5S4j)P<v*P6-AL4f/M-o*b5b;Y1tAZ-eMb.s/U/j2S)!5Y+jObloA[-n6\\;!*H8j(\\;!2L7!'JCw+U-o'[1tObqb3b;f*b5b>P5v9b8v8\\;-AH<!*P/o/Z;j3b4j-\\4bObqv2S)!4L+!8\\<s;TCe5S7sObpb;Y1tA[1o)P,v4[Ct+T8f8b)m/X=f:pCQ8V1oAW4b)L:b:b6v2S)!'\\/v+nCt/[Cb3L<!*H8j(\\;!4P;mAL=j9T7eAT7m+Z<j+pCG;Z+fAU7oA]-t:P*v2\\5!+_Q!nV:c/b)!8O7o)\\;!4P;mObpp8I1!4V6!/T8f8K1f:b6j9SO!9P<!'T-uA[1o)P,v4[Co+X=fObdf4L)oAZ+f2L:j9X=fAJ7o9L+u+[=sAW0b8L<s'pCE5U-dAH+!,L=h/H<!;Y6bObtv/Z9v+b+v8Z=tAL4f3L6u;TCb;N=fMb=uAL4f3L6u;TCb4[-!)V6t+X=b:b-vObvf*b1n6L:e/L<!;S<s/J1f9b-yAH+!/T8f8K1f:pCV:b.b;J1c;ZCw+S1uA]-mAM)v)P*v9b<f3W=tObfs'ZCf-L<!6\\4w/U)sAT)t9HQ!tL,!9L,!4\\6dAK1d:\\5!+U1nAK)q/I=tA\\4u8P+j+ZCbAU7oAL:p9pCQ8V1oAL.g/J1u;YCc/I-o*\\5!*P/o/Z;j3pCO;U+!;S<s/J1f9b8s+[1v3b>j<L:s'pCQ+S4f4[-t7\\-!,P6j(\\;!+U1nAW=s;ZO!+[Cn5S4j9b)s)\\Cq.H:f:Y)!+N-uObqv2S)nAS)d/U1bAU=o)b>f2b:j9\\;!*P+u;TO!'[Cd;Y;v9b4b)\\;!6\\4w/U)sObqv2S)nA[-n6\\;!+_Cn'N6bMb>j:H-!:L5q;ZCe;PCj3W-s*P-uA]1u'LQ!qO)t+S4v9b5b2L;v'K)!6L4m+U<f9X=fAY1t;ZO!/KCd5U;f)[-u;YCo/Z1!+\\1t3V,!<L4/A+7o+JCb)b<f2S=tA[-m2\\;/A4)v8P;!+\\Cb)J=n9H6!2V:f3nCj4b+p4Z-d:L<v8b-m/[Q!jU<f-L:!6S)d+Y)uAT1!2P/v2HO!'b;p*H4f9b4p8L5!)V6t+J<f:\\:!/UQ!wL;u/I=m;TCt+KCe;PCj*b-m/[Cm;J<v9b<j4J1e;U<!+N-uAH+!4P*iObgp4L+!)V6e/T-o:\\5!6O)s+[:bAV,j5b)dAZ+f2L:j9X=fObqv2S)!<L4j:b)o:LO!<H:j;ZCw+SCn'N6bA\\<-AJ7n3V,pAJ7o9L9v'[Cf8V;/A=1w'T=tAL:p9b5b-U)-AL.g/J1u;YCj4b:i5U+v9b<f3W=tMb8s+[1v3b;f*b6j9PQ!t\\;q+U,j9Z-!:L5q5YCo;S4bAL;uMb-h+[Cf;P;n5KCm/N=m'b5p2L;u/LCj*pCB2P9v'TCf:b,p2V:!<P<b+b.f2P;!2H7s+L<!/H+v2P;/A:-eAH+!+_Cb)b4j-\\4bAK1d:\\5!)V6e/T-o:\\5!9P<!'T-uAU-dAL;uObgp4L+!4V6!3L<v9b9v/ZCp8J1!9H/j:[1tAH+d;T;b4b)!+N-uA[-m2\\;/A(4j7\\)nAL:b:b>p2\\<q'[Q!jU<f-L:!9V4m/J1u;K1oAL<!5Y+jAH<!'S1r;L</A+7o+JCg/U1c;ZCu5Y<p8b-vAT)t9HCi+U,s+Y1uMb6p4b>b8P=tAL;uAP5q+Y,j+[Q!f[1b3b<j4J1e;U<!9H/j:[1tA\\4u8P+f9pCV:b6p4b-s'[Cb;J<p8nCf2L5f4[=nAS)d;ZCv:nCq.H:f:Y)!:\\:q/ZQ!dY)tAS=d:\\;!6\\4w/U)sAV:d/b-uA\\4u8P+f9pCB+U-b4b.b;J1c;ZCj6Z=nA\\<!3H/o'b-v/Z5p*b8m'J-s'[Q!qO)t+S4v9b>f.P+v2HCt+TCn'N6bMb9v/ZCd5T5p*VCf9[Cb;J<p8b5b>P5v9pCO;U+!+\\1t3V,!'\\/v+b5b-U)-AZ7e'S-tA]7m;[8b:b5b-U)!/H+v2P;!+[Q!eV6f)b6v2S)!3L<v9nCf2L5f4[=nAL=!+U1nAX=j9nCj4[-s*\\5!:P6d/K=o:b)o:LQ!d\\:b(P<v8b5b-U)!/W;v3nCs;[:v3b8p9\\-s+b)s)\\Ct+KO!:L5q;ZCj'J=m/ZCq;Y=tObpb+J-o'ZCe/J<v3b6f7\\-!+\\Cp8U)s+b<f3W7sObyf9[1c;S=nAW4b)L:b:b>j:H-!+U1nAU7oAL=j9T7eObyf9[1c;S=nAT)u:P;!<H:j;ZCo;U+-AP6!+S-n+U<v3b-m/[Cj4[-s*\\5!9P<!'T-uObvf*b4v)[=tAP8t;TCo+JCu;Y8j9b-g,P+j:\\:!/H+v2P;/A06!*P)nAH:d;nCw;S8v:H<fAHCo;S4bAU7oMb*j(L6e;TCd5U>b2S1tAV:d/pCT+KCd;Y;v9nCo;U+!'JCf2L1g+U,!<V4v:W)uMb-s5ZCe5S7sA]-o+U)u/ZCb8J=-AP6!<H:j;ZCr;H5!7\\)nAH<!9H8j+UQ!o\\4m'TCu+T8p8nCk;Z<pA\\<!)V6e/T-o:\\5!2H+j4P)-AU-r;LCe/H5!:P6d/K=o:b6v4JO!+N-uAW0b8L<s'b5f:\\;!2H+v9b>j:H-!:L4m;ZQ!qL4m+U<f9X=fAT7m+Z<j+b5b>P5v9b5b;Y1tAH+!,L:n+U<v3pCQ8V1oAU1t2b4b)\\;-AL4f/M-o*b;j:b)n+[Cm5Y-nAX=j9nCg8P6h/S4bAW4b)L:b:b4f5pCQ+S4f4[-t7\\-!'b5f:\\;!2P*f8VQ!jUCi'JCi'I1u'Z;fAW4b:L)!*P+u;T;uObqv2S)!<H:j;ZCj4[-s*\\5!9L5!+[Cq;S>j4H:/A8=j9X=fAL/f:b>f2P<!9P<!'T-uAH=h;LCg8P6h/S4bAZ7m2P+j:\\,j4pCE;P;!(P*f4K=nAU=o)b7s)PQ!wP>b3\\;!<P<b+b5f:\\;!/UCn'\\:j9b-m+P.f4KCf-L;u'ZQ!qL4m+U<f9X=fAS=d:\\;!2L+u;ZCm+J<v9nCf;b-m+T-o:\\5!4P*iAT7m+Z<j+b;j:b)n+[Q!eV6f)b;f3W-sMb-t:b-h+[Ct5S4j)P<v*P6!'J+v3Z)oMb)o:LCw+S1uAJ7o-\\-!'Y+vMb)dAJ7o9L+u+[=sAS-d:\\;!4L9v+b-h+[Ct'W1f4pCR;P;r;LCt+T8f8nCm+J<v9b>j:H-!+S-j,L6eAT)y/T=tMb6f7\\-!4\\4m'b>j<L:s'b4b)\\;-AP6u+Y,v3b)m/X=f:b9v'TCb8J=!9L,!3H=s/ZQ!f[1b3b9v/ZCf8H<!4V6!6\\:v9b;p*H4f9b-m+T-o:\\5!<L4!4V6!,L4j9pCT;Z8f4K1t9LCd5T5p*VCf2P<!+[Co;U+!<H:j;ZCf-L;u'Z."
chunkSize = 4
# for chunkSize in range(1,4):
print(chunkSize)
chunks = [texto[i:i + chunkSize] for i in range(0, len(texto), chunkSize)]
print(Counter([chunk[0] for chunk in chunks]))


chave = []
print(chunks[:-1])
for index in range(0,chunkSize):
    temp = []
    for chunk in chunks[:-1]:
        temp.append(chunk[index])
    mostCommon = Counter(temp).most_common(1)[0]
    chave.append(chr((((ord(mostCommon[0])-inicioDoAlfabeto)+tamanhoDoAlfabeto)%tamanhoDoAlfabeto)+inicioDoAlfabeto))
print('chave: ', ''.join(chave),)
