from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class LipopeptideData(models.Model):
    lipopeptide_name = models.CharField(max_length=255)
    lipopeptide_organism = models.TextField(null=True, blank=True)
    lipopeptide_summary = models.TextField(null=True, blank=True)
    lipopeptide_activity = models.TextField(null=True, blank=True)
    molecular_formula = models.CharField(max_length=100, null=True, blank=True)
    molecular_weight = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    lipopeptide_structure_2d = models.ImageField(null=True, blank=True, upload_to='structures/2d/')
    canonical_smiles = models.TextField(null=True, blank=True)
    cas_number = models.CharField(max_length=255, null=True, blank=True)
    ec_number = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lipopeptide_name)


class LipopeptideApplicationsData(models.Model):
    lipopeptide_id = models.ForeignKey(LipopeptideData)
    lipopeptide_application = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lipopeptide_id.lipopeptide_name)+ " " + str(self.lipopeptide_application)


class LipopeptideFunctionsData(models.Model):
    lipopeptide_id = models.ForeignKey(LipopeptideData)
    lipopeptide_function = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lipopeptide_id.lipopeptide_name)


class LipopeptideLigandData(models.Model):
    lipopeptide_id = models.ForeignKey(LipopeptideData)
    ligand_name = models.CharField(max_length=255, null=True, blank=True)
    ligand_iupac_name = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lipopeptide_id.lipopeptide_name)+str(self.ligand_name)


# class LipopeptidePathwayData(models.Model):
#     lipopeptide_id = models.ForeignKey(LipopeptideData)
#     lipopeptide_pathway_name = models.CharField(max_length=255, null=True, blank=True)
#     lipopeptide_pathway_description = models.TextField(null=True, blank=True)
#     lipopeptide_pathway_image = models.ImageField(null=True, blank=True, upload_to='pathways/')
#     is_deleted = models.BooleanField(default=False)
#     created_at = models.DateTimeField(default=timezone.now())
#     modified_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return str(self.lipopeptide_id.lipopeptide_name)


# class LipopeptideDiscoverData(models.Model):
#     lipopeptide_id = models.ForeignKey(LipopeptideData)
#     discoverer_name = models.CharField(max_length=255, null=True, blank=True)
#     discoverer_profile = models.URLField(null=True, blank=True)
#     discoverer_introduction = models.TextField(null=True, blank=True)
#     discoverer_image = models.ImageField(null=True, blank=True, upload_to='discoverer/')
#     is_deleted = models.BooleanField(default=False)
#     created_at = models.DateTimeField(default=timezone.now())
#     modified_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return str(self.lipopeptide_id.lipopeptide_name)


STAGE_CHOICE = ((1, 'Absorption'), (2, 'Distribution'), (3, 'Metabolism'), (4, 'Excretion'), (5, 'Toxicity'))

class LipopeptideMetabolismData(models.Model):
    lipopeptide_id = models.ForeignKey(LipopeptideData)
    lipopeptide_metabolism_stage = models.IntegerField(choices=STAGE_CHOICE, default=None)
    metabolism_model = models.CharField(max_length=255, null=True, blank=True)
    metabolism_result = models.CharField(max_length=255, null=True, blank=True)
    metabolism_probability = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=6)
    metabolism_value = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=6)
    metabolism_units = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lipopeptide_id.lipopeptide_name)+str(self.metabolism_model)


class LipopeptidePropertiesData(models.Model):
    lipopeptide_id = models.ForeignKey(LipopeptideData)
    property_name = models.CharField(max_length=255, null=True, blank=True)
    property_value = models.CharField(max_length=255,null=True,blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lipopeptide_id.lipopeptide_name) + str(self.property_name)


class LipopeptideReferencesData(models.Model):
    lipopeptide_id = models.ForeignKey(LipopeptideData)
    reference_data = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lipopeptide_id.lipopeptide_name)


# class DrugTarget(models.Model):
