from django.contrib import admin

from proteins.models import *

class LipopeptideDataAdmin(admin.ModelAdmin):
    list_display = ['lipopeptide_name', 'lipopeptide_organism', 'molecular_formula', 'molecular_weight',
                    'cas_number', 'ec_number']
    search_fields = ['lipopeptide_name']


class LipopeptideApplicationsDataAdmin(admin.ModelAdmin):
    list_display = ['lipopeptide_id', 'lipopeptide_application', 'application_description']
    search_fields = ['lipopeptide_id', 'lipopeptide_application']


class LipopeptideLigandDataAdmin(admin.ModelAdmin):
    list_display = ['lipopeptide_id', 'ligand_iupac_name', 'ligand_name']
    search_fields = ['ligand_name', 'lipopeptide_id__lipopeptide_name', 'ligand_iupac_name']


class LipopeptideMetabolismDataAdmin(admin.ModelAdmin):
    list_display = ['lipopeptide_id', 'lipopeptide_metabolism_stage', 'metabolism_model', 'metabolism_result',
                    'metabolism_probability', 'metabolism_value', 'metabolism_units']
    search_fields = ['lipopeptide_id__lipopeptide_name', 'metabolism_model', 'lipopeptide_metabolism_stage']


class LipopeptidePropertiesDataAdmin(admin.ModelAdmin):
    list_display = ['lipopeptide_id', 'property_name', 'property_value']
    search_fields = ['lipopeptide_id__lipopeptide_name', 'property_name']


class LipopeptideReferencesDataAdmin(admin.ModelAdmin):
    list_display = ['lipopeptide_id', 'reference_data']
    search_fields = ['lipopeptide_id__lipopeptide_name', 'reference_data']

admin.site.register(LipopeptideData, LipopeptideDataAdmin)
admin.site.register(LipopeptideApplicationsData, LipopeptideApplicationsDataAdmin)
admin.site.register(LipopeptideLigandData, LipopeptideLigandDataAdmin)
admin.site.register(LipopeptideMetabolismData, LipopeptideMetabolismDataAdmin)
admin.site.register(LipopeptidePropertiesData, LipopeptidePropertiesDataAdmin)
admin.site.register(LipopeptideReferencesData, LipopeptideReferencesDataAdmin)
