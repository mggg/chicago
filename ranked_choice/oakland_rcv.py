#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:27:39 2019

@author: ruthbuck
"""

import pandas as pd 

### Mayor 2014

mayor14 = pd.read_table('/Users/ruthbuck/Downloads/ballot_image_may14.txt', sep=r'\s{2,}',header=None,)

mayor14.columns = ["Ballot_Im"]

mayor14["Contest_Id"] = mayor14.Ballot_Im.str[0:7]
mayor14["Pref_Voter_Id"] = mayor14.Ballot_Im.str[7:16]
mayor14["Serial_Number"] = mayor14.Ballot_Im.str[16:23]
mayor14["Tally_Type_Id"] = mayor14.Ballot_Im.str[23:26]
mayor14["Precinct_Id"] = 'C' + mayor14.Ballot_Im.str[26:33]
mayor14["Vote_Rank"] = mayor14.Ballot_Im.str[34:36]
mayor14["Candidate_Id"] = mayor14.Ballot_Im.str[36:43]
mayor14["Over_Vote"] = mayor14.Ballot_Im.str[43]
mayor14["Under_Vote"] = mayor14.Ballot_Im.str[44]

racial_ids = [['0000430', 'Black'],['0000418', 'Black'],['0000422', 'White'],
              ['0000419', 'White'], ['0000423', 'Black'], ['0000421', 'Black'],
              ['0000432', 'Asian'], ['0000428', 'White'], ['0000429', 'Undetermined'],
              ['0000431', 'White'], ['0000426', 'White'], ['0000425', 'Black'],
              ['0000427', 'Asian'], ['0000420', 'White'], ['0000424', 'Asian'],
              ['0000417', 'Black']]
df_racial_ids = pd.DataFrame(racial_ids, columns= ["Candidate_Id","Candidate_Race_Id"])

mayor14 = mayor14.join(df_racial_ids.set_index('Candidate_Id'), on = 'Candidate_Id')
precinct_idjoin = pd.read_csv('/Users/ruthbuck/Dropbox/Chicago RCV project/RCV Ballot data and candidate identification files/Oakland/No_Excel/WinEDS_key_mayoral14.csv')
mayor14 = mayor14.join(precinct_idjoin.set_index('Precinct_Id'), on = 'Precinct_Id')


### District 1 2012

dist1_12 = pd.read_table('/Users/ruthbuck/Downloads/ballot_image_dist1.txt', sep=r'\s{2,}',header=None)

dist1_12.columns = ["Ballot_Im"] 

dist1_12["Contest_Id"] = dist1_12.Ballot_Im.str[0:7]
dist1_12["Pref_Voter_Id"] = dist1_12.Ballot_Im.str[7:16]
dist1_12["Serial_Number"] = dist1_12.Ballot_Im.str[16:23]
dist1_12["Tally_Type_Id"] = dist1_12.Ballot_Im.str[23:26]
dist1_12["Precinct_Id"] = dist1_12.Ballot_Im.str[26:33]
dist1_12["Vote_Rank"] = dist1_12.Ballot_Im.str[34:36]
dist1_12["Candidate_Id"] = dist1_12.Ballot_Im.str[36:43]
dist1_12["Over_Vote"] = dist1_12.Ballot_Im.str[43]
dist1_12["Under_Vote"] = dist1_12.Ballot_Im.str[44]

### At large 2012

dist_atlarge_12 = pd.read_table('/Users/ruthbuck/Downloads/ballot_image_cc_large12.txt', sep=r'\s{2,}',header=None,)

dist_atlarge_12.columns = ["Ballot_Im"] 

dist_atlarge_12["Contest_Id"] = dist_atlarge_12.Ballot_Im.str[0:7]
dist_atlarge_12["Pref_Voter_Id"] = dist_atlarge_12.Ballot_Im.str[7:16]
dist_atlarge_12["Serial_Number"] = dist_atlarge_12.Ballot_Im.str[16:23]
dist_atlarge_12["Tally_Type_Id"] = dist_atlarge_12.Ballot_Im.str[23:26]
dist_atlarge_12["Precinct_Id"] = dist_atlarge_12.Ballot_Im.str[26:33]
dist_atlarge_12["Vote_Rank"] = dist_atlarge_12.Ballot_Im.str[34:36]
dist_atlarge_12["Candidate_Id"] = dist_atlarge_12.Ballot_Im.str[36:43]
dist_atlarge_12["Over_Vote"] = dist_atlarge_12.Ballot_Im.str[43]
dist_atlarge_12["Under_Vote"] = dist_atlarge_12.Ballot_Im.str[44]

racial_ids1 = [['0000369', 'Black'],['0000373', 'Hispanic'],['0000371', 'White'],
              ['0000370', 'White'], ['0000372', 'Black']
              ]
df_racial_ids1 = pd.DataFrame(racial_ids1, columns= ["Candidate_Id","Candidate_Race_Id"])

dist_atlarge_12 = dist_atlarge_12.join(df_racial_ids1.set_index('Candidate_Id'), on = 'Candidate_Id')

### District 5, 2012

dist5_12 = pd.read_table('/Users/ruthbuck/Downloads/ballot_image_dist5.txt',sep=r'\s{2,}',header=None)

dist5_12.columns = ["Ballot_Im"]

dist5_12["Contest_Id"] = dist5_12.Ballot_Im.str[0:7]
dist5_12["Pref_Voter_Id"] = dist5_12.Ballot_Im.str[7:16]
dist5_12["Serial_Number"] = dist5_12.Ballot_Im.str[16:23]
dist5_12["Tally_Type_Id"] = dist5_12.Ballot_Im.str[23:26]
dist5_12["Precinct_Id"] = dist5_12.Ballot_Im.str[26:33]
dist5_12["Vote_Rank"] = dist5_12.Ballot_Im.str[34:36]
dist5_12["Candidate_Id"] = dist5_12.Ballot_Im.str[36:43]
dist5_12["Over_Vote"] = dist5_12.Ballot_Im.str[43]
dist5_12["Under_Vote"] = dist5_12.Ballot_Im.str[44]

racial_ids2 = [['0000389', 'Hispanic'],['0000387', 'White'],['0000388', 'Hispanic'],
               ['0000389', 'Hispanic']
              ]
df_racial_ids2 = pd.DataFrame(racial_ids2, columns= ["Candidate_Id","Candidate_Race_Id"])

dist5_12 = dist5_12.join(df_racial_ids2.set_index('Candidate_Id'), on = 'Candidate_Id')


### District 3, 2012

dist3_12 = pd.read_table('/Users/ruthbuck/Downloads/ballot_image_dist3.txt',sep=r'\s{2,}',header=None)

dist3_12.columns = ["Ballot_Im"]

dist3_12["Contest_Id"] = dist3_12.Ballot_Im.str[0:7]
dist3_12["Pref_Voter_Id"] = dist3_12.Ballot_Im.str[7:16]
dist3_12["Serial_Number"] = dist3_12.Ballot_Im.str[16:23]
dist3_12["Tally_Type_Id"] = dist3_12.Ballot_Im.str[23:26]
dist3_12["Precinct_Id"] = dist3_12.Ballot_Im.str[26:33]
dist3_12["Vote_Rank"] = dist3_12.Ballot_Im.str[34:36]
dist3_12["Candidate_Id"] = dist3_12.Ballot_Im.str[36:43]
dist3_12["Over_Vote"] = dist3_12.Ballot_Im.str[43]
dist3_12["Under_Vote"] = dist3_12.Ballot_Im.str[44]

dist3_12 = pd.read_table('/Users/ruthbuck/Downloads/ballot_image_dist3.txt',sep=r'\s{2,}',header=None)

dist3_12.columns = ["Ballot_Im"]

dist3_12["Contest_Id"] = dist3_12.Ballot_Im.str[0:7]
dist3_12["Pref_Voter_Id"] = dist3_12.Ballot_Im.str[7:16]
dist3_12["Serial_Number"] = dist3_12.Ballot_Im.str[16:23]
dist3_12["Tally_Type_Id"] = dist3_12.Ballot_Im.str[23:26]
dist3_12["Precinct_Id"] = dist3_12.Ballot_Im.str[26:33]
dist3_12["Vote_Rank"] = dist3_12.Ballot_Im.str[34:36]
dist3_12["Candidate_Id"] = dist3_12.Ballot_Im.str[36:43]
dist3_12["Over_Vote"] = dist3_12.Ballot_Im.str[43]
dist3_12["Under_Vote"] = dist3_12.Ballot_Im.str[44]

dist3_12 = pd.read_table('',sep=r'\s{2,}',header=None)
