# import csv
#
# from proteins.models import LipopeptideData, LipopeptideMetabolismData
#
#
# def add_classification():
#     inputfile = 'Classification.csv'
#     with open(inputfile,'r') as csvfile:
#             csvreader = csv.reader(csvfile)
#             last_peptide=''
#             lipopeptide_instance=''
#             for row in csvreader:
#                 peptide = row[0]
#                 if peptide != last_peptide:
#                     lipopeptide = LipopeptideData.objects.get(lipopeptide_name=peptide)
#                     lipopeptide_instance=lipopeptide
#                 lipopeptide_metabolism = LipopeptideMetabolismData.objects.create(lipopeptide_id=lipopeptide_instance,
#                                                                                   lipopeptide_metabolism_stage=row[2],
#                                                                                   metabolism_model=row[1],
#                                                                                   metabolism_result=row[3],
#                                                                                   metabolism_probability=row[4])
#                 print lipopeptide_metabolism.id
#                 last_peptide = peptide