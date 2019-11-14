import numpy as np
import STLgen

aircord = np.array([[100,	0	],
[99,	0.2969	],
[98,	0.53335	],
[97,	0.76868	],
[96,	1.00232	],
[94,	1.46239	],
[92,	1.91156	],
[90,	2.35025	],
[88,	2.77891	],
[86,	3.1974	],
[84,	3.60536	],
[82,	4.00245	],
[80,	4.38836	],
[78,	4.76281	],
[76,	5.12565	],
[74,	5.47675	],
[72,	5.81599	],
[70,	6.14329	],
[68,	6.45843	],
[66,	6.76046	],
[64,	7.04822	],
[62,	7.32055	],
[60,	7.57633	],
[58,	7.81451	],
[56,	8.0348	],
[54,	8.23712	],
[52,	8.42145	],
[50,	8.58772	],
[48,	8.73572	],
[46,	8.86427	],
[44,	8.97175	],
[42,	9.05657	],
[40,	9.11712	],
[38,	9.15212	],
[36,	9.16266	],
[34,	9.15079	],
[32,	9.11857	],
[30,	9.06804	],
[28,	9.00016	],
[26,	8.9084	],
[24,	8.78308	],
[22,	8.61433	],
[20,	8.39202	],
[18,	8.10687	],
[16,	7.75707	],
[14,	7.3436	],
[12,	6.86204	],
[10,	6.29981	],
[8,	5.64308	],
[6,	4.87571	],
[5,	4.42753	],
[4,	3.91283	],
[3,	3.30215	],
[2,	2.53735	],
[1.2,	1.78581	],
[0.8,	1.3735	],
[0.4,	0.89238	],
[0.2,	0.58025	],
[0.1,	0.37271	],
[0.05,	0.2339	],
[0,	0	],
[0.05,	-0.467	],
[0.1,	-0.59418	],
[0.2,	-0.78113	],
[0.4,	-1.05126	],
[0.8,	-1.42862	],
[1.2,	-1.69733	],
[2,	-2.02723	],
[3,	-2.26056	],
[4,	-2.45211	],
[5,	-2.60452	],
[6,	-2.71277	],
[8,	-2.84595	],
[10,	-2.93786	],
[12,	-2.99633	],
[14,	-3.02404	],
[16,	-3.02546	],
[18,	-3.0049	        ],
[20,	-2.96656	],
[22,	-2.91445	],
[24,	-2.85181	],
[26,	-2.78164	],
[28,	-2.70696	],
[30,	-2.63079	],
[32,	-2.55565	],
[34,	-2.48176	],
[36,	-2.4087	    ] ,
[38,	-2.33606	],
[40,	-2.26341	],
[42,	-2.19042	],
[44,	-2.11708	],
[46,	-2.04353	],
[48,	-1.96986	],
[50,	-1.89619	],
[52,	-1.82262	],
[54,	-1.74914	],
[56,	-1.67572	],
[58,	-1.60232	],
[60,	-1.52893	],
[62,	-1.45551	],
[64,	-1.38207	],
[66,	-1.30862	],
[68,	-1.23515	],
[70,	-1.16169	],
[72,	-1.08823	],
[74,	-1.01478	],
[76,	-0.94133	],
[78,	-0.86788	],
[80,	-0.79443	],
[82,	-0.72098	],
[84,	-0.64753	],
[86,	-0.57408	],
[88,	-0.50063	],
[90,	-0.42718	],
[92,	-0.35373	],
[94,	-0.28028	],
[96,	-0.20683	],
[97,	-0.17011	],
[98,	-0.13339	],
[99,	-0.09666	],
[100,0]]	)
cord=np.array([[6.996108596,-5.549789742,0.],
[7.251920749,-4.959425886,0.],
[7.731919605,-4.106932791,0.],
[8.196776384,-3.450571522,0.],
[8.578950028,-2.94993704,0.],
[9.089168438,-2.252573101,0.],
[9.564169885,-1.59297561,0.],
[9.986987719,-1.021618206,0.],
[10.31757063,-0.585197434,0.],
[10.771939134,0.,0.],
[11.329426686,0.695171282,0.],
[11.967531498,1.461926924,0.],
[12.53428364,2.119473054,0.],
[13.153228003,2.814697238,0.],
[13.870333425,3.593061985,0.],
[14.525932764,4.281190357,0.],
[15.489617136,5.25420701,0.],
[16.486622655,6.215244482,0.],
[17.777147427,7.39459656,0.],
[18.830619653,8.306497723,0.],
[19.913940556,9.199328793,0.],
[21.274195996,10.259599621,0.],
[22.253441385,10.983516004,0.],
[23.058121372,11.555028304,0.],
[24.366552581,12.441495709,0.],
[25.39875337,13.105078635,0.],
[26.526906266,13.795944494,0.],
[27.75078179,14.506448589,0.],
[28.948528967,15.164035225,0.],
[29.878277023,15.649606495,0.],
[31.097502922,16.254410262,0.],
[32.30202766,16.81730299,0.],
[33.451651223,17.323299508,0.],
[34.682950622,17.832213813,0.],
[35.121779093,18.005526473,0.],
[35.526767103,18.161832094,0.],
[36.205083056,18.415993927,0.],
[36.674031817,18.586258913,0.],
[37.650788923,18.927090872,0.],
[37.650788923,18.927090872,0.],
[37.253430759,18.844852621,0.],
[37.031242534,18.798422876,0.],
[36.772197399,18.743886759,0.],
[36.479087596,18.681652232,0.],
[36.034850555,18.586258913,0.],
[35.526767103,18.475565751,0.],
[34.682950621,18.287951326,0.],
[33.451651223,18.005526473,0.],
[32.30202766,17.732178573,0.],
[31.097502923,17.435313662,0.],
[29.878277023,17.12343357,0.],
[28.948528967,16.877575437,0.],
[27.75078179,16.550149754,0.],
[26.526906266,16.202572984,0.],
[25.39875337,15.869981989,0.],
[24.366552581,15.554985118,0.],
[23.058121372,15.140761465,0.],
[21.148883007,14.506448581,0.],
[19.343694837,13.874099647,0.],
[17.27416345,13.105078627,0.],
[15.489617137,12.393709115,0.],
[13.870333427,11.70013495,0.],
[11.9675315,10.810570526,0.],
[10.317570629,9.956726065,0.],
[8.578950027,8.95165657,0.],
[6.937290293,7.864367552,0.],
[5.756191991,6.972076568,0.],
[4.852854111,6.215244482,0.],
[3.807325558,5.254207013,0.],
[2.816627033,4.281190357,0.],
[2.148351974,3.593061987,0.],
[1.298549855,2.62248969,0.],
[0.920394774,2.119473051,0.],
[0.506228422,1.461926925,0.],
[0.330619066,1.116420227,0.],
[0.160964249,0.695171282,0.],
[0.,0.,0.],
[0.081369994,-1.021618207,0.],
[0.300728083,-1.59297561,0.],
[0.701252119,-2.252573101,0.],
[1.29854986,-2.94993704,0.],
[1.849508493,-3.450571522,0.],
[2.464274424,-3.910884138,0.],
[3.31396112,-4.41096921,0.],
[4.287912125,-4.831401052,0.],
[4.85285411,-5.023036314,0.],
[5.756191996,-5.274102331,0.],
[6.341854651,-5.411154181,0.],
[6.996108596,-5.549789742,0.]])
initial_cpoints = np.array([[  6.9961086  , -5.54978974],
[ 13.75059254 ,  5.94414712],
[ 25.11931948 , 14.62378626],
[ 37.65078892 , 18.92709087],
[ 27.62107402 , 17.09798259],
[ 14.53714153 , 11.92558065],
[ 14.03779692 , 14.61821902],
[-13.94023124 , -1.9938111 ]])
#aircord = np.append(aircord.transpose(), np.zeros((1, aircord.shape[0])), 0).transpose()
#aircord_rot=STLgen.rotate(aircord,13,[0,0,1])

"""[[-0.11236, 0.019943],
                            [-0.09054228, 0.06216698],
                            [-0.05712186, 0.09847833],
                            [-0.01482015, 0.12391961],
                            [0.030924, 0.1368],
                            [-0.13130294, 0.07826767],
                            [0.03289166, 0.15488873],
                            [-0.22181531, 0.04901755],
                            [-0.11236, 0.019943]]"""