# this file was automatically generated by prognosis.py
train_congress = 112
test_congress = 113
model_test_results = {('bill', 0): {'bill_type': 'bill',
               'bill_type_descr': 'bills',
               'bins': [(0.7576905943527571, 889, 0.019122609673790775),
                        (1.8055752750381848, 891, 0.013468013468013467),
                        (2.3206643101627336, 819, 0.01098901098901099),
                        (3.8084965128648576, 962, 0.040540540540540543),
                        (5.4122547889377008, 782, 0.079283887468030695),
                        (6.8612121891792723, 1000, 0.091999999999999998),
                        (8.5234485844708825, 642, 0.14018691588785046),
                        (13.661523325057578, 1116, 0.16308243727598568),
                        (23.179953067316038, 913, 0.33625410733844469)],
               'count': 8905,
               'is_introduced_model': True,
               'overall': 11.102596034102884,
               'precision_recall': [{'precision': 0.19908116385911179,
                                     'recall': 0.97524381095273815,
                                     'threshold': 2.7323722447292558},
                                    {'precision': 0.21273757919306435,
                                     'recall': 0.95723930982745686,
                                     'threshold': 3.337326996032608},
                                    {'precision': 0.22824716267339218,
                                     'recall': 0.95048762190547642,
                                     'threshold': 4.076220397836621},
                                    {'precision': 0.2398687765341567,
                                     'recall': 0.93248312078019502,
                                     'threshold': 4.978706836786395},
                                    {'precision': 0.25379023883696783,
                                     'recall': 0.91672918229557387,
                                     'threshold': 6.0810062625217975},
                                    {'precision': 0.31276656241114587,
                                     'recall': 0.82520630157539387,
                                     'threshold': 7.427357821433388},
                                    {'precision': 0.33126358273828005,
                                     'recall': 0.80045011252813203,
                                     'threshold': 9.071795328941251},
                                    {'precision': 0.37369841881989974,
                                     'recall': 0.72693173293323332,
                                     'threshold': 11.080315836233387},
                                    {'precision': 0.39126784214945426,
                                     'recall': 0.69917479369842461,
                                     'threshold': 13.53352832366127},
                                    {'precision': 0.46583850931677018,
                                     'recall': 0.61890472618154535,
                                     'threshold': 16.529888822158654},
                                    {'precision': 0.49834983498349833,
                                     'recall': 0.56639159789947491,
                                     'threshold': 20.189651799465537},
                                    {'precision': 0.5334855403348554,
                                     'recall': 0.52588147036759192,
                                     'threshold': 24.659696394160648},
                                    {'precision': 0.57793983591613496,
                                     'recall': 0.47561890472618157,
                                     'threshold': 30.119421191220212},
                                    {'precision': 0.58465011286681712,
                                     'recall': 0.38859714928732181,
                                     'threshold': 36.787944117144235},
                                    {'precision': 0.63306451612903225,
                                     'recall': 0.35333833458364589,
                                     'threshold': 44.932896411722155},
                                    {'precision': 0.69734151329243355,
                                     'recall': 0.2558139534883721,
                                     'threshold': 54.88116360940264},
                                    {'precision': 0.73139158576051777,
                                     'recall': 0.16954238559639909,
                                     'threshold': 67.03200460356393},
                                    {'precision': 0.80434782608695654,
                                     'recall': 0.083270817704426112,
                                     'threshold': 81.87307530779819}],
               'success_name': 'sent out of committee to the floor'},
 ('bill', 1): {'bill_type': 'bill',
               'bill_type_descr': 'bills',
               'bins': [(17.84050904399524, 126, 0.16307714809494031),
                        (23.875236173586959, 101, 0.22836551865817245),
                        (26.722347736322899, 410, 0.31443687885518706),
                        (34.499869158106556, 295, 0.30305835207457349),
                        (39.587651624358408, 124, 0.34211439152190526),
                        (52.260467945904701, 136, 0.34927979851020857)],
               'count': 1333,
               'is_introduced_model': False,
               'overall': 23.46850733390854,
               'precision_recall': [{'precision': 0.32455187045416345,
                                     'recall': 1.0,
                                     'threshold': 2.7323722447292558},
                                    {'precision': 0.32455187045416345,
                                     'recall': 1.0,
                                     'threshold': 3.337326996032608},
                                    {'precision': 0.32455187045416345,
                                     'recall': 1.0,
                                     'threshold': 4.076220397836621},
                                    {'precision': 0.32455187045416345,
                                     'recall': 1.0,
                                     'threshold': 4.978706836786395},
                                    {'precision': 0.32455187045416345,
                                     'recall': 1.0,
                                     'threshold': 6.0810062625217975},
                                    {'precision': 0.32455187045416345,
                                     'recall': 1.0,
                                     'threshold': 7.427357821433388},
                                    {'precision': 0.32598604760127697,
                                     'recall': 0.99989793035838637,
                                     'threshold': 9.071795328941251},
                                    {'precision': 0.32598604760127697,
                                     'recall': 0.99989793035838637,
                                     'threshold': 11.080315836233387},
                                    {'precision': 0.32733307485485696,
                                     'recall': 0.99192381200168667,
                                     'threshold': 13.53352832366127},
                                    {'precision': 0.3275723452258234,
                                     'recall': 0.99189170843848762,
                                     'threshold': 16.529888822158654},
                                    {'precision': 0.34138836583093995,
                                     'recall': 0.95481629303629212,
                                     'threshold': 20.189651799465537},
                                    {'precision': 0.35323913841003407,
                                     'recall': 0.9308064891587674,
                                     'threshold': 24.659696394160648},
                                    {'precision': 0.37416645827859685,
                                     'recall': 0.616651961275964,
                                     'threshold': 30.119421191220212},
                                    {'precision': 0.42486417152288097,
                                     'recall': 0.47826082019636368,
                                     'threshold': 36.787944117144235},
                                    {'precision': 0.44369061795776854,
                                     'recall': 0.32408062092426182,
                                     'threshold': 44.932896411722155},
                                    {'precision': 0.53588579819963045,
                                     'recall': 0.22296181292699171,
                                     'threshold': 54.88116360940264},
                                    {'precision': 0.60780781810129336,
                                     'recall': 0.14330197897487215,
                                     'threshold': 67.03200460356393},
                                    {'precision': 0.73398268398268396,
                                     'recall': 0.071255901474605088,
                                     'threshold': 81.87307530779819}],
               'success_name': 'enacted'},
 ('cr', 0): {'bill_type': 'cr',
             'bill_type_descr': 'concurrent resolutions',
             'bins': [(1.2965902994232746e-15, 15, 0.0),
                      (1.9413387726567168e-14, 16, 0.0625),
                      (11.541199676432427, 19, 0.21052631578947367)],
             'count': 169,
             'is_introduced_model': True,
             'overall': 40.094339622641506,
             'precision_recall': [{'precision': 0.46478873239436619,
                                   'recall': 1.0,
                                   'threshold': 2.7323722447292558},
                                  {'precision': 0.46762589928057552,
                                   'recall': 0.98484848484848486,
                                   'threshold': 3.337326996032608},
                                  {'precision': 0.46762589928057552,
                                   'recall': 0.98484848484848486,
                                   'threshold': 4.076220397836621},
                                  {'precision': 0.46762589928057552,
                                   'recall': 0.98484848484848486,
                                   'threshold': 4.978706836786395},
                                  {'precision': 0.46762589928057552,
                                   'recall': 0.98484848484848486,
                                   'threshold': 6.0810062625217975},
                                  {'precision': 0.46762589928057552,
                                   'recall': 0.98484848484848486,
                                   'threshold': 7.427357821433388},
                                  {'precision': 0.46762589928057552,
                                   'recall': 0.98484848484848486,
                                   'threshold': 9.071795328941251},
                                  {'precision': 0.48062015503875971,
                                   'recall': 0.93939393939393945,
                                   'threshold': 11.080315836233387},
                                  {'precision': 0.49193548387096775,
                                   'recall': 0.9242424242424242,
                                   'threshold': 13.53352832366127},
                                  {'precision': 0.49193548387096775,
                                   'recall': 0.9242424242424242,
                                   'threshold': 16.529888822158654},
                                  {'precision': 0.49193548387096775,
                                   'recall': 0.9242424242424242,
                                   'threshold': 20.189651799465537},
                                  {'precision': 0.49193548387096775,
                                   'recall': 0.9242424242424242,
                                   'threshold': 24.659696394160648},
                                  {'precision': 0.49193548387096775,
                                   'recall': 0.9242424242424242,
                                   'threshold': 30.119421191220212},
                                  {'precision': 0.57843137254901966,
                                   'recall': 0.89393939393939392,
                                   'threshold': 36.787944117144235},
                                  {'precision': 0.57843137254901966,
                                   'recall': 0.89393939393939392,
                                   'threshold': 44.932896411722155},
                                  {'precision': 0.57843137254901966,
                                   'recall': 0.89393939393939392,
                                   'threshold': 54.88116360940264}],
             'success_name': 'sent out of committee to the floor'},
 ('cr', 1): {'bill_type': 'cr',
             'bill_type_descr': 'concurrent resolutions',
             'bins': [],
             'count': 66,
             'is_introduced_model': False,
             'overall': 58.8235294117647,
             'precision_recall': [{'precision': 0.84441361529544245,
                                   'recall': 1.0,
                                   'threshold': 2.7323722447292558},
                                  {'precision': 0.84441361529544245,
                                   'recall': 1.0,
                                   'threshold': 3.337326996032608},
                                  {'precision': 0.84441361529544245,
                                   'recall': 1.0,
                                   'threshold': 4.076220397836621},
                                  {'precision': 0.84441361529544245,
                                   'recall': 1.0,
                                   'threshold': 4.978706836786395},
                                  {'precision': 0.84441361529544245,
                                   'recall': 1.0,
                                   'threshold': 6.0810062625217975},
                                  {'precision': 0.84441361529544245,
                                   'recall': 1.0,
                                   'threshold': 7.427357821433388},
                                  {'precision': 0.84441361529544245,
                                   'recall': 1.0,
                                   'threshold': 9.071795328941251},
                                  {'precision': 0.84441361529544245,
                                   'recall': 1.0,
                                   'threshold': 11.080315836233387},
                                  {'precision': 0.84441361529544245,
                                   'recall': 1.0,
                                   'threshold': 13.53352832366127},
                                  {'precision': 0.84441361529544245,
                                   'recall': 1.0,
                                   'threshold': 16.529888822158654},
                                  {'precision': 0.85475424347612783,
                                   'recall': 0.98157180879234041,
                                   'threshold': 20.189651799465537},
                                  {'precision': 0.85475424347612783,
                                   'recall': 0.98157180879234041,
                                   'threshold': 24.659696394160648},
                                  {'precision': 0.85475424347612783,
                                   'recall': 0.98157180879234041,
                                   'threshold': 30.119421191220212},
                                  {'precision': 0.85475424347612783,
                                   'recall': 0.98157180879234041,
                                   'threshold': 36.787944117144235},
                                  {'precision': 0.85475424347612783,
                                   'recall': 0.98157180879234041,
                                   'threshold': 44.932896411722155},
                                  {'precision': 0.85475424347612783,
                                   'recall': 0.98157180879234041,
                                   'threshold': 54.88116360940264},
                                  {'precision': 0.85475424347612783,
                                   'recall': 0.98157180879234041,
                                   'threshold': 67.03200460356393}],
             'success_name': 'agreed to'},
 ('jr', 0): {'bill_type': 'jr',
             'bill_type_descr': 'joint resolutions',
             'bins': [(5.9525793049872014e-16, 24, 0.0),
                      (2.8298449385489729e-15, 29, 0.0),
                      (3.271144945177133e-14, 3, 0.0),
                      (7.4170702258698826, 19, 0.0)],
             'count': 178,
             'is_introduced_model': True,
             'overall': 20.809248554913296,
             'precision_recall': [{'precision': 0.27049180327868855,
                                   'recall': 1.0,
                                   'threshold': 2.7323722447292558},
                                  {'precision': 0.27049180327868855,
                                   'recall': 1.0,
                                   'threshold': 3.337326996032608},
                                  {'precision': 0.27049180327868855,
                                   'recall': 1.0,
                                   'threshold': 4.076220397836621},
                                  {'precision': 0.27049180327868855,
                                   'recall': 1.0,
                                   'threshold': 4.978706836786395},
                                  {'precision': 0.27049180327868855,
                                   'recall': 1.0,
                                   'threshold': 6.0810062625217975},
                                  {'precision': 0.32038834951456313,
                                   'recall': 1.0,
                                   'threshold': 7.427357821433388},
                                  {'precision': 0.32038834951456313,
                                   'recall': 1.0,
                                   'threshold': 9.071795328941251},
                                  {'precision': 0.32038834951456313,
                                   'recall': 1.0,
                                   'threshold': 11.080315836233387},
                                  {'precision': 0.32038834951456313,
                                   'recall': 1.0,
                                   'threshold': 13.53352832366127},
                                  {'precision': 0.32038834951456313,
                                   'recall': 1.0,
                                   'threshold': 16.529888822158654},
                                  {'precision': 0.32038834951456313,
                                   'recall': 1.0,
                                   'threshold': 20.189651799465537},
                                  {'precision': 0.32038834951456313,
                                   'recall': 1.0,
                                   'threshold': 24.659696394160648},
                                  {'precision': 0.63829787234042556,
                                   'recall': 0.90909090909090906,
                                   'threshold': 30.119421191220212},
                                  {'precision': 0.63829787234042556,
                                   'recall': 0.90909090909090906,
                                   'threshold': 36.787944117144235},
                                  {'precision': 0.63829787234042556,
                                   'recall': 0.90909090909090906,
                                   'threshold': 44.932896411722155},
                                  {'precision': 0.63043478260869568,
                                   'recall': 0.87878787878787878,
                                   'threshold': 54.88116360940264},
                                  {'precision': 0.63043478260869568,
                                   'recall': 0.87878787878787878,
                                   'threshold': 67.03200460356393}],
             'success_name': 'sent out of committee to the floor'},
 ('jr', 1): {'bill_type': 'jr',
             'bill_type_descr': 'joint resolutions',
             'bins': [],
             'count': 33,
             'is_introduced_model': False,
             'overall': 33.333333333333336,
             'precision_recall': [{'precision': 0.54917590603072564,
                                   'recall': 1.0,
                                   'threshold': 2.7323722447292558},
                                  {'precision': 0.54917590603072564,
                                   'recall': 1.0,
                                   'threshold': 3.337326996032608},
                                  {'precision': 0.54917590603072564,
                                   'recall': 1.0,
                                   'threshold': 4.076220397836621},
                                  {'precision': 0.54917590603072564,
                                   'recall': 1.0,
                                   'threshold': 4.978706836786395},
                                  {'precision': 0.54917590603072564,
                                   'recall': 1.0,
                                   'threshold': 6.0810062625217975},
                                  {'precision': 0.54917590603072564,
                                   'recall': 1.0,
                                   'threshold': 7.427357821433388},
                                  {'precision': 0.54917590603072564,
                                   'recall': 1.0,
                                   'threshold': 9.071795328941251},
                                  {'precision': 0.47592880097358037,
                                   'recall': 0.70905567310862772,
                                   'threshold': 11.080315836233387},
                                  {'precision': 0.47592880097358037,
                                   'recall': 0.70905567310862772,
                                   'threshold': 13.53352832366127},
                                  {'precision': 0.47592880097358037,
                                   'recall': 0.70905567310862772,
                                   'threshold': 16.529888822158654},
                                  {'precision': 0.47592880097358037,
                                   'recall': 0.70905567310862772,
                                   'threshold': 20.189651799465537},
                                  {'precision': 0.47592880097358037,
                                   'recall': 0.70905567310862772,
                                   'threshold': 24.659696394160648},
                                  {'precision': 0.47592880097358037,
                                   'recall': 0.70905567310862772,
                                   'threshold': 30.119421191220212},
                                  {'precision': 0.47592880097358037,
                                   'recall': 0.70905567310862772,
                                   'threshold': 36.787944117144235},
                                  {'precision': 0.47592880097358037,
                                   'recall': 0.70905567310862772,
                                   'threshold': 44.932896411722155},
                                  {'precision': 0.47592880097358037,
                                   'recall': 0.70905567310862772,
                                   'threshold': 54.88116360940264}],
             'success_name': 'enacted or passed'},
 ('sr', 0): {'bill_type': 'sr',
             'bill_type_descr': 'simple resolutions',
             'bins': [(1.2070827440677963e-14, 139, 0.014388489208633094),
                      (1.2247918450599411, 135, 0.037037037037037035),
                      (4.9432124097223866, 137, 0.080291970802919707),
                      (12.616447481640579, 143, 0.13986013986013987),
                      (27.679036579962723, 138, 0.21739130434782608),
                      (65.578551990096884, 98, 0.55102040816326525),
                      (71.643648561717825, 139, 0.74100719424460426),
                      (82.48632874242, 314, 0.87579617834394907)],
             'count': 1385,
             'is_introduced_model': True,
             'overall': 47.05084745762712,
             'precision_recall': [{'precision': 0.56082289803220031,
                                   'recall': 0.98895899053627756,
                                   'threshold': 2.7323722447292558},
                                  {'precision': 0.57155963302752288,
                                   'recall': 0.98264984227129337,
                                   'threshold': 3.337326996032608},
                                  {'precision': 0.58419567262464722,
                                   'recall': 0.97949526813880128,
                                   'threshold': 4.076220397836621},
                                  {'precision': 0.59767891682785301,
                                   'recall': 0.97476340694006314,
                                   'threshold': 4.978706836786395},
                                  {'precision': 0.61332007952286283,
                                   'recall': 0.97318611987381698,
                                   'threshold': 6.0810062625217975},
                                  {'precision': 0.63152507676560898,
                                   'recall': 0.97318611987381698,
                                   'threshold': 7.427357821433388},
                                  {'precision': 0.63825363825363823,
                                   'recall': 0.96845425867507884,
                                   'threshold': 9.071795328941251},
                                  {'precision': 0.6566523605150214,
                                   'recall': 0.96529968454258674,
                                   'threshold': 11.080315836233387},
                                  {'precision': 0.68462401795735128,
                                   'recall': 0.96214511041009465,
                                   'threshold': 13.53352832366127},
                                  {'precision': 0.68848758465011284,
                                   'recall': 0.96214511041009465,
                                   'threshold': 16.529888822158654},
                                  {'precision': 0.73547589616810882,
                                   'recall': 0.93848580441640383,
                                   'threshold': 20.189651799465537},
                                  {'precision': 0.76005188067444873,
                                   'recall': 0.9242902208201893,
                                   'threshold': 24.659696394160648},
                                  {'precision': 0.7831325301204819,
                                   'recall': 0.92271293375394325,
                                   'threshold': 30.119421191220212},
                                  {'precision': 0.8041666666666667,
                                   'recall': 0.91324921135646686,
                                   'threshold': 36.787944117144235},
                                  {'precision': 0.81673881673881676,
                                   'recall': 0.89274447949526814,
                                   'threshold': 44.932896411722155},
                                  {'precision': 0.83667180277349773,
                                   'recall': 0.85646687697160884,
                                   'threshold': 54.88116360940264},
                                  {'precision': 0.85906040268456374,
                                   'recall': 0.80757097791798105,
                                   'threshold': 67.03200460356393},
                                  {'precision': 0.89692982456140347,
                                   'recall': 0.64511041009463721,
                                   'threshold': 81.87307530779819}],
             'success_name': 'sent out of committee to the floor'},
 ('sr', 1): {'bill_type': 'sr',
             'bill_type_descr': 'simple resolutions',
             'bins': [(82.441783832240702, 57, 0.90728432388757108),
                      (95.285102698460804, 43, 0.84131871035940808)],
             'count': 634,
             'is_introduced_model': False,
             'overall': 96.82997118155619,
             'precision_recall': [{'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 2.7323722447292558},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 3.337326996032608},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 4.076220397836621},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 4.978706836786395},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 6.0810062625217975},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 7.427357821433388},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 9.071795328941251},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 11.080315836233387},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 13.53352832366127},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 16.529888822158654},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 20.189651799465537},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 24.659696394160648},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 30.119421191220212},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 36.787944117144235},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 44.932896411722155},
                                  {'precision': 0.96277504592058716,
                                   'recall': 1.0,
                                   'threshold': 54.88116360940264},
                                  {'precision': 0.96677134154144295,
                                   'recall': 0.98672863438181024,
                                   'threshold': 67.03200460356393},
                                  {'precision': 0.96677134154144295,
                                   'recall': 0.98672863438181024,
                                   'threshold': 81.87307530779819}],
             'success_name': 'agreed to'}}
