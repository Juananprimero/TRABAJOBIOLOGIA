from chembl_webresource_client.new_client import new_client

brca_genes = ['BRIP1', 'BCL11A', 'CHEK2', 'FBLN1', 'BRCA1', 'TRIM33'
		,'MRPS30', 'ADGRB3', 'CHD9', 'SLC4A7', 'CCND1', 'PELI2'
		, 'RAD51D', 'TNP1', 'CCN3', 'MAP3K1', 'SIK1', 'FGFR2'
		, 'XRCC3', 'TERT', 'BRCA2', 'ZNF365', 'RAD51C', 'LSP1'
		, 'RAD51', 'NBN', 'AKT2', 'AKT1', 'PIK3CA', 'SEMA3A'
		, 'CCDC170', 'FGF10', 'ENPP2', 'ZMIZ1', 'RNF146'
		, 'MELK', 'BABAM1', 'PALB2', 'ESR1', 'NTRK3']

new_genes = ['GENES','XRCC2','RAD51B','BLM','ATM','FANCD2','ATR','CHEK1',
                'MSH2','MSH6','NLRP2','RAD50','MRE11','TOPBP1','MDC1','BARD1',
                'RFC1','MLH1','RFC4','RFC2','BACH1','RBBP8','DCLRE1C',
                'ABRAXAS1','UIMC1','H2AFX','PRKDC','XRCC5','LIG4','WRN',
                'RPA1','RPA2','TP53BP1','FANCE','PCNA','PMS2','XRCC6','TERF2',
                'PARP1','TP53','CDK2','POLA1','RPA3','CCNA2','POLE','POLD1',
                'LIG1','CCNB1','CDK1','TOP2B','TOP1','PRIM1','POLA2','POLD2',
                'POLD3','PRIM2','POLD4','POLE4','POLE3','POLE2','TOP2A','RAD17',
                'RAD9A','RFC3','RFC5','XRCC1','HUS1','RAD1','FEN1','CHD1L','APLF',
                'TERF2IP','TERF1','XRCC4','FANCA','FANCG','TOP3A','FANCC','RMI1',
                'FANCF','FANCL','FANCB','FANCM','TINF2','CENPS','LIG3','RECQL',
                'FAN1','CDKN1A','TDP1','NHEJ1','CLSPN','ORC2','ACD','POT1','CCNB2',
                'PMS1','SMC1A','CHTF18','CHTF8','DSCC1','EP300','MYC','RB1','HDAC1',
                'E2F1','SUMO2','ABL1','CSNK2A1','APEX1','CDK4','CDK5','JUN','CDKN1B',
                'SP1','AR','CDK6','CDK7','UBC','MDM2','CREBBP','PML','CEBPA','CSNK2A2',
                'CSNK2B','RELA','MAPK1','NCOA6','SMAD3','CDK9','MYOD1','RBL2','PTPN1',
                'SRC','STAT3','HSP90AA1','KAT5','NPM1','HDAC2','SMARCA4','ACTB','POLR2A',
                'NR3C1','NCL','HSP90AB1','ENSG00000269099','NEK10','TOX3','C8orf4',
                'COX11','BAI3','SOX4','LAPTM4B','HMMR','BPI','RB1CC1','BAG4','ARHGEF5','CCL27',
                'TNC','SLC22A18','APLNR','ITGA6','HNRNPL','LPHN3','ACP1','CYP1B1','CASP8','NCOA3',
                'LSM1','MCF2','COMT','GRM8','MAP2K4','CCL21','CYP17A1','CYP1A1','PGR','PGM1',
                'LCN2','TNFSF11','VIM','SNAI2','CCR7','EIF2C2','PPM1D','CXCL12','PAX2','CYP19A1',
                'ZNF217','FN1','GNAS','SUCLG1','BACE1','DICER1','RAF1','NOTCH2','CDH1','GNAO1',
                'SNCA','TGFB1','RHOG','PTEN','YWHAZ','RHOA','RAC3','CDC42','RAC1','ERBB2','FHIT',
                'CDH13','CDKN2A','FASLG','GSTM1','VEGFC','EGFR','MTOR','MYCL1','NF1','RASSF1',
                'HRAS','BIRC5','HIF1A','THBS1','WWOX','ALK','ESR2','BIRC3','PRDM10','SUMO1',
                'ATRIP','BRAP','FAM175A','PAXIP1','RAD52','EXO1','SMARCA2','UBE2D1','RAD18',
                'DDB2','MCPH1','RNF8','PIAS4','DCLRE1B','ATRX','OGG1','DCLRE1A','ERCC4',
                'MSH3','ERCC2','PARK2','PARP2','UBE2E2','SLX4','BCL2','POLI','MLH3',
                'REV3L','UBE2D3','MUTYH','BAX','POLH','BRCC3','GAPDH','OBFC1','SIRT1','ICAM1',
                'XPC','MCM7','PIAS1','TSPO','XPA','hCG_32740','IFI35','SMARCE1','MAPKAPK2',
                'CENPC1','SALL4','RSF1','DBF4','NPAT','SLX1A','SLX1B','MRE11A','PNKP','ERCC1',
                'PLK1','LYPD6B','RMI2','C11orf30','GADD45A','MDM4','SCG2','ERC1','EME1','NUDT5',
                'POLN','APITD1','POLB','USP1','DNA2','TRDMT1','SMC2','TIPIN','UBE2T','ESCO1','CBX1','RNF4']

genesV2 = brca_genes + new_genes

target = new_client.target
res = target.filter(target_synonym__in=genesV2).only('target_chembl_id')

with open('targetsV2.txt', mode = 'w') as f:
	for element in res:
		f.write('%s\n' % element['target_chembl_id'])






