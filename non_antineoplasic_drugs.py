from chembl_webresource_client.new_client import new_client

def is_antineoplasic( drug , antineoplasic_atc_codes):
	for code in drug['atc_classifications'] :
		if code in antineoplasic_atc_codes :
			return True
	return False


atc_codes = new_client.atc_class
atc_codes = atc_codes.filter(level2__contains="L01").only('level5')
antineoplasic_atc_codes = list()
for code in atc_codes:
        antineoplasic_atc_codes.append(code['level5'])

drug = new_client.molecule
drugs = drug.filter(atc_classifications__isnull=False
					, biotherapeutic_isnull=False
					, max_phase=4).only('molecule_chembl_id', 'atc_classifications', 'pref_name')

with open('non_antineoplasic_drugs.txt', 'w') as f:
        for drug in drugs:
                if not is_antineoplasic(drug , antineoplasic_atc_codes) :
                        f.write("%s\n" % drug['molecule_chembl_id'])
