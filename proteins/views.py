from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from selenium import webdriver

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from proteins.models import LipopeptideData, LipopeptideApplicationsData, LipopeptideFunctionsData, \
    LipopeptideLigandData, LipopeptideReferencesData, LipopeptidePropertiesData


@require_http_methods(['GET'])
def list_lipopeptides(request):
    response_json={'lipopeptide_data': []}
    try:
        search_query = request.GET.get('query')
        if search_query == '':
            lipopeptide_list = LipopeptideData.objects.filter(lipopeptide_name=search_query,
                                                              is_deleted=False)
        else:
            lipopeptide_list = LipopeptideData.objects.filter(is_deleted=False)
        for lipopeptide in lipopeptide_list:
            temp_json = {'lipopeptide_name': lipopeptide.lipopeptide_name,
                         'lipopeptide_organism': lipopeptide.lipopeptide_organism,
                         'lipopeptide_family': lipopeptide.lipopeptide_family,
                         'lipopeptide_structure_3d': lipopeptide.lipopeptide_structure_3d,
                         'lipopeptide_primary_sequence': lipopeptide.lipopeptide_primary_sequence,
                         'lipopeptide_secondary_sequence': lipopeptide.lipopeptide_secondary_sequence,
                         'lipopeptide_tertiary_sequence': lipopeptide.lipopeptide_tertiary_sequence,
                         'lipopeptide_source': lipopeptide.lipopeptide_source,
                         'lipopeptide_summary': lipopeptide.lipopeptide_summary,
                         'lipopeptide_activity': lipopeptide.lipopeptide_activity,
                         'molecular_formula': lipopeptide.molecular_formula,
                         'molecular_weight': lipopeptide.molecular_weight,
                         'lipopeptide_structure_2d': lipopeptide.lipopeptide_structure_2d,
                         'canonical_smiles': lipopeptide.canonical_smiles,
                         'cas_number': lipopeptide.cas_number,
                         'ec_number': lipopeptide.ec_number}
            response_json['lipopeptide_data'].append(temp_json)
            # response_json['lipopeptide_application'] = get_applications(lipopeptide)
            # response_json['lipopeptide_functions'] = get_functions(lipopeptide)
            # response_json['lipopeptide_ligands'] = get_ligands(lipopeptide)
        response_json['success'] = True
        response_json['message'] = "All the protein information has been successfully shown."
        return JsonResponse(response_json)
    except Exception as e:
        print str(e)
        response_json['success'] = False
        response_json['message'] = "An error has occured. Please try again later."
        return JsonResponse(response_json)

def get_ligands(lipopeptide):
    response_json = {'lipopeptide_ligands': []}
    try:
        lipopeptide_ligands = LipopeptideLigandData.objects.filter(lipopeptide_id=lipopeptide,
                                                                   is_deleted=False)
        for ligand in lipopeptide_ligands:
            temp_json = {'ligand_name': ligand.ligand_name}
            response_json['lipopeptide_ligands'].append(temp_json)
        return response_json['lipopeptide_ligands']
    except Exception as e:
        print str(e)

def get_functions(lipopeptide):
    response_json = {'lipopeptide_functions': []}
    try:
        lipopeptide_functions = LipopeptideFunctionsData.objects.filter(lipopeptide_id=lipopeptide,
                                                                        is_deleted=False)
        for fun in lipopeptide_functions:
            temp_json = {'function_description': fun.function_description,
                         'lipopeptide_function': fun.lipopeptide_function}
            response_json['lipopeptide_functions'].append(temp_json)
        return response_json['lipopeptide_functions']
    except Exception as e:
        print str(e)

def get_applications(lipopeptide):
    response_json = {'lipopeptide_applications': []}
    try:
        lipopeptide_applications = LipopeptideApplicationsData.objects.filter(lipopeptide_id=lipopeptide,
                                                                              is_deleted=False)
        for app in lipopeptide_applications:
            temp_json = {'application_description': app.application_description,
                         'lipopeptide_application': app.lipopeptide_application}
            response_json['lipopeptide_applications'].append(temp_json)
        return response_json['lipopeptide_applications']
    except Exception as e:
        print str(e)


def get_admet_properties(request):
    response_json = {}
    if request.method == 'GET':
        try:
            lipopeptides = LipopeptideData.objects.filter(id=1)
            for lip in lipopeptides:
                canonical_smiles = lip.canonical_smiles
                browser = webdriver.Firefox(executable_path='/home/yash/Downloads/geckodriver')
                browser.get('http://swissadme.ch/')
                input = browser.find_element_by_id("smiles")
                browser.find_element_by_id("smiles").clear()
                print("\n\n\n\ncleared")
                browser.find_element_by_id("smiles").send_keys(canonical_smiles)
                print("\n\n\n\ninsert")
                browser.find_element_by_id("submitButton").click()
                print("\n\n\n\nclick\n\n\n\n\n")
                res = browser.find_element_by_name("main results")
                print res
                browser.close()
        except Exception as e:
            print str(e)
        response_json['success'] = True
        return JsonResponse(response_json)


def get_properties(request):
    response_json = {}
    if request.method == 'GET':
        try:
            lipopeptides = LipopeptideData.objects.filter(id=1)
            for lip in lipopeptides:
                name = lip.lipopeptide_name
                browser = webdriver.Firefox(executable_path='/home/yash/Downloads/geckodriver')
                browser.get('https://pubchem.ncbi.nlm.nih.gov/')
                input = browser.find_element_by_tag_name("input")
                browser.find_element_by_tag_name("input").clear()
                print("\n\n\n\ncleared")
                browser.find_element_by_tag_name("input").send_keys(name)
                print("\n\n\n\ninsert")
                # browser.find_element_by_tag_name("button width-2em height-2em lh-1").click()
                # browser.find_elements_by_tag_name("button").click()
                browser.find_element_by_xpath("/html/body/div[1]/div/div/main/div[1]/div[2]/div/div/div[2]/form/div/div[3]/button").click()
                print("\n\n\n\nclick\n\n\n\n\n")
                browser.find_element_by_xpath("//*[@id=\"featured-results\"]/div/div[2]/div/div[1]/div[2]/div[1]/a/span/span").click()
                # browser.find_element_by_class_name("capitalized")
                print ("\n\n\ndata\n\n\n\n")

                res = browser.find_element_by_xpath("//*[@id=\"Computed-Properties\"]/div[2]/div[2]/div[1]/table")
                print res
                browser.close()
        except Exception as e:
            print str(e)
        response_json['success'] = True
        return JsonResponse(response_json)

import csv

from proteins.models import LipopeptideData, LipopeptideMetabolismData


def add_classification(requestss):
    try:
        inputfile = 'Classification.csv'
        with open(inputfile,'r') as csvfile:
                csvreader = csv.reader(csvfile)
                last_peptide=''
                lipopeptide_instance=''
                for row in csvreader:
                    peptide = row[0]
                    if peptide != last_peptide:
                        lipopeptide = LipopeptideData.objects.get(lipopeptide_name=peptide)
                        lipopeptide_instance=lipopeptide
                    lipopeptide_metabolism = LipopeptideMetabolismData.objects.create(lipopeptide_id=lipopeptide_instance,
                                                                                      lipopeptide_metabolism_stage=row[2],
                                                                                      metabolism_model=row[1],
                                                                                      metabolism_result=row[3],
                                                                                      )
                    print lipopeptide_metabolism.id
                    last_peptide = peptide
    except Exception as e:
        print str(e)
    response1={}
    response1['success'] = True
    return JsonResponse(response1)


def add_regression(request):
    try:
        inputfile = 'Regression.csv'
        with open(inputfile,'r') as csvfile:
                csvreader = csv.reader(csvfile)
                last_peptide=''
                lipopeptide_instance=''
                for row in csvreader:
                    peptide = row[0]
                    if peptide != last_peptide:
                        lipopeptide = LipopeptideData.objects.get(lipopeptide_name=peptide)
                        lipopeptide_instance=lipopeptide
                    lipopeptide_metabolism = LipopeptideMetabolismData.objects.create(lipopeptide_id=lipopeptide_instance,
                                                                                      metabolism_model=row[1],
                                                                                      lipopeptide_metabolism_stage=0,
                                                                                      metabolism_value=row[3],
                                                                                      metabolism_units=row[4])
                    print lipopeptide_metabolism.id
                    last_peptide = peptide
    except Exception as e:
        print str(e)
    response1={}
    response1['success'] = True
    return JsonResponse(response1)


def add_ligand(request):
    try:
        inputfile = 'Ligand.csv'
        with open(inputfile,'r') as csvfile:
                csvreader = csv.reader(csvfile)
                last_peptide=''
                lipopeptide_instance=''
                for row in csvreader:
                    peptide = row[0]
                    if peptide != last_peptide:
                        lipopeptide = LipopeptideData.objects.get(lipopeptide_name=peptide)
                        lipopeptide_instance=lipopeptide
                    lipopeptide_ligand = LipopeptideLigandData.objects.create(lipopeptide_id=lipopeptide_instance,
                                                                                  ligand_name=row[1],
                                                                                  ligand_iupac_name=row[2])
                    print lipopeptide_ligand.id
                    last_peptide = peptide
    except Exception as e:
        print str(e)
    response1={}
    response1['success'] = True
    return JsonResponse(response1)

def add_lipopetide(request):
    try:
        inputfile = 'Lipopeptides.csv'
        with open(inputfile,'r') as csvfile:
                csvreader = csv.reader(csvfile)
                # last_peptide=''
                # lipopeptide_instance=''
                for row in csvreader:
                    # peptide = row[0]
                    # if peptide != last_peptide:
                    #     lipopeptide = LipopeptideData.objects.get(lipopeptide_name=peptide)
                    #     lipopeptide_instance=lipopeptide
                    try:
                        weight = float(row[5])
                    except Exception as e:
                        weight = 0.0
                    lipopeptide = LipopeptideData.objects.create(lipopeptide_name=row[0],
                                                                 lipopeptide_organism=row[1],
                                                                 lipopeptide_summary=row[2],
                                                                 lipopeptide_activity=row[3],
                                                                 molecular_formula=row[4],
                                                                 molecular_weight=weight,
                                                                 canonical_smiles=row[6],
                                                                 cas_number=row[7])
                    print lipopeptide.id
                    # last_peptide = peptide
    except Exception as e:
        print str(e)
    response1={}
    response1['success'] = True
    return JsonResponse(response1)

def add_applications(request):
    try:
        inputfile = 'Applications.csv'
        with open(inputfile,'r') as csvfile:
                csvreader = csv.reader(csvfile)
                last_peptide=''
                lipopeptide_instance=''
                for row in csvreader:
                    peptide = row[0]
                    if peptide == '':
                        continue
                    if peptide != last_peptide:
                        lipopeptide = LipopeptideData.objects.get(lipopeptide_name=peptide)
                        lipopeptide_instance=lipopeptide
                    lipopeptide_ligand = LipopeptideApplicationsData.objects.create(lipopeptide_id=lipopeptide_instance,
                                                                                    lipopeptide_application=row[1],
                                                                                    application_description=row[2])
                    print lipopeptide_ligand.id
                    last_peptide = peptide
    except Exception as e:
        print str(e)
        print row[0] + "," + row[1] + "," + row[2]
    response1={}
    response1['success'] = True
    return JsonResponse(response1)


def add_references(request):
    try:
        inputfile = 'References.csv'
        with open(inputfile,'r') as csvfile:
                csvreader = csv.reader(csvfile)
                last_peptide=''
                lipopeptide_instance=''
                for row in csvreader:
                    peptide = row[0]
                    if peptide == '':
                        continue
                    if peptide != last_peptide:
                        lipopeptide = LipopeptideData.objects.get(lipopeptide_name=peptide)
                        lipopeptide_instance=lipopeptide
                    lipopeptide_ligand = LipopeptideReferencesData.objects.create(lipopeptide_id=lipopeptide_instance,
                                                                                    reference_data=row[1])
                    print lipopeptide_ligand.id
                    last_peptide = peptide
    except Exception as e:
        print str(e)
    response1={}
    response1['success'] = True
    return JsonResponse(response1)


def add_properties(request):
    try:
        inputfile = 'Properties.csv'
        with open(inputfile,'r') as csvfile:
                csvreader = csv.reader(csvfile)
                last_peptide=''
                lipopeptide_instance=''
                for row in csvreader:
                    peptide = row[0]
                    if peptide == '':
                        continue
                    if peptide != last_peptide:
                        lipopeptide = LipopeptideData.objects.get(lipopeptide_name=peptide)
                        lipopeptide_instance=lipopeptide
                    lipopeptide_property = LipopeptidePropertiesData.objects.create(lipopeptide_id=lipopeptide_instance,
                                                                                    property_name=row[1],
                                                                                    property_value=row[2])
                    print lipopeptide_property.id
                    last_peptide = peptide
    except Exception as e:
        print str(e)
        print row[0] + "," + row[1] + "," + row[2]
    response1={}
    response1['success'] = True
    return JsonResponse(response1)