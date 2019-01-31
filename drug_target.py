from chembl_webresource_client.new_client import new_client
import csv

targets = list()
NANPD = list()

with open('targetsV2.txt', 'r') as f:
	lines = f.read().splitlines()
	for line in lines:
		targets.append(line)
print(len(targets))

with open('non_antineoplasic_drugs.txt', 'r') as f:
	lines = f.read().splitlines()
	for line in lines:
		NANPD.append(line)

activity = new_client.activity.filter(target_chembl_id__in=targets
										, molecule_chembl_id__in=NANPD
										, pchembl_value__gte=6).only('molecule_pref_name','target_pref_name', 'pchembl_value')

print("OK maquina, ya he encontrado las interacciones, ahora te las pinto")
print(len(activity))
cnt =0;
with open ('drug_targetV2.csv', 'w') as f:
	fieldnames = ['drug', 'target', 'pchembl_value']
	writer = csv.DictWriter(f, fieldnames=fieldnames)

	writer.writeheader()
	[ writer.writerow({'drug':  element['molecule_pref_name'] , 'target': element['target_pref_name'], 'pchembl_value': element['pchembl_value']}) for element in activity ]

print(cnt)


