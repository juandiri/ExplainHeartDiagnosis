import os
import csv
import re
import sys

import pandas as pd
import scipy.stats as stats

def write_csv(contents, f_name):
    csv_f = open(f_name, 'w')
    writer = csv.writer(csv_f)
    writer.writerows(contents)
    csv_f.close()


def get_entitlement_per_entity(ents_dir:str, domains:list):

    entitlements_dict = dict()
    
    for domain in domains:
        # Read entailment
        print(f"=========== Reading entailments for domain: {domain} =========== \n")
        ents_df = pd.read_csv(f"{ents_dir}/{domain}_entailments.csv")


        # Join entialments in one string
        
        entitlement_list = ents_df['entailment'].values
        entailments = ''
        for entailment in entitlement_list:
            if entailment != ' ':
                try:
                    entailments += entailment
                except:
                    pass
        # Create dictionary to store all the entailment per entity

        dom_entitlements_dict = dict()

        # Personal Information
        age = re.findall(r'age_\d+', entailments)
        dom_entitlements_dict['Age'] = age

        chest_pain_type = ['TypicalAngina', 'AtypicalAngina', 'NonAnginalPain', 'Asymptomatic']
        dom_entitlements_dict['ChestPainType'] = chest_pain_type
        
        cholesterol = re.findall('chol_\d+', entailments)
        dom_entitlements_dict['Cholesterol'] = cholesterol

        fasting_blood_sugar = ['Higher120mg/dl', 'Lower120mg/dl']
        dom_entitlements_dict['FastingBloodSugar'] = fasting_blood_sugar

        hypertension = ['Hypertensive', 'NonHypertensive']
        dom_entitlements_dict['Hypertension'] = hypertension
        
        rest_blood_pressure = re.findall('rbp_\d+', entailments)
        dom_entitlements_dict['RestBloodPressure'] = rest_blood_pressure

        sex =['Male', 'Female']
        dom_entitlements_dict['Sex'] = sex

        # Exercise ECG Reading

        calblocker =  ['NotUsedClaciumChannelBlocker', 'UsedClaciumChannelBlocker']
        dom_entitlements_dict['CalciumChabbelBlocker'] = calblocker

        betablocker = ['NotUsedBetablocker', 'UsedBetablocker']
        dom_entitlements_dict['Betablocker'] = betablocker
        
        ex_day = re.findall('exday_\d+', entailments)
        dom_entitlements_dict['ExerciseDailyReading'] = ex_day

        digitalis = ['NotUsedDigitalis', 'UsedDigitalis']
        dom_entitlements_dict['Digitalis'] = digitalis

        diuretics = ['NotUsedDiuretics', 'UsedDiuretics']
        dom_entitlements_dict['Diuretics'] = diuretics
        
        ex_dur = re.findall('exdur_\d+', entailments)
        dom_entitlements_dict['ExerciseDuration'] = ex_dur

        ex_peak_height = re.findall('expeakheight_\d+', entailments)
        dom_entitlements_dict['ExerciseHeightAtPeak'] = ex_peak_height
        
        ex_ind_angina = ['InducedAngina', 'NotInduceAngina']
        dom_entitlements_dict['ExerciseInducedAngina'] = ex_ind_angina
        
        ex_ind_hypotension = ['InducedHypotension', 'NonInducedHypotension']
        dom_entitlements_dict['ExerciseInducedHypotension'] = ex_ind_hypotension

        ex_induced_st = re.findall('stdep_\d+', entailments)
        dom_entitlements_dict['ExerciseInducedSTDepression'] = ex_induced_st

        ex_max_heart_rate = re.findall('exmaxhr_\d+', entailments)
        dom_entitlements_dict['ExerciseMaximumHeartRate'] = ex_max_heart_rate

        ex_peak_bp1 = re.findall('expeakbp1_\d+', entailments)
        dom_entitlements_dict['ExercisePeakBloodPressure1'] = ex_peak_bp1

        ex_peak_bp2 = re.findall('expeakbp2_\d+', entailments)
        dom_entitlements_dict['ExercisePeakBloodPressure2'] = ex_peak_bp2

        ex_protocol = ['Bruce','Kottus','McHenry','FastBalke','Balke','Noughton''Bike150kpa/min','Bike125kpa/min','Bike100kpa/min','Bike75kpa/min','Bike50kpa/min']
        dom_entitlements_dict['ExerciseProtocol'] = ex_protocol

        ex_rest_bp = re.findall('exrestbp_\d+', entailments)
        dom_entitlements_dict['ExerciseRestingBloodPressure'] = ex_rest_bp

        ex_rest_heart_rate = re.findall('exminhr_\d+', entailments) 
        dom_entitlements_dict['ExerciseRestingHeartRate'] = ex_rest_heart_rate

        ex_mets = re.findall('met_\d+', entailments)
        dom_entitlements_dict['METSTestScore'] = ex_mets
        
        ex_month = re.findall('exmo_\d+', entailments)
        dom_entitlements_dict['ExerciseMonthlyReading'] = ex_month

        nitrates = ['NotUsedNitrates', 'UsedNitrates']
        dom_entitlements_dict['Nitrates'] = nitrates

        ex_st_dep = ['STWaveAbnormality', 'STWaveNormality', 'VentricularHypertrophy']
        dom_entitlements_dict['STDepression'] = ex_st_dep

        ex_year = re.findall('exyr_\d+', entailments)
        dom_entitlements_dict['ExerciseYearlyReadin'] = ex_year

        # Coronary Angiogram Diagnosis
        ca_day = re.findall('cday_\d+', entailments)
        dom_entitlements_dict['DailyCardiacCath'] = ca_day

        heart_diagnosis = ['PossiblyHealthy''LessThan50DiameterNarrowing','MoreThan50DiameterNarrowing']
        dom_entitlements_dict['HeartDiagnosis'] = heart_diagnosis 

        ca_month = re.findall('camo_\d+', entailments)
        dom_entitlements_dict['MonthlyCardiacCath'] = ca_month

        vessels_dmg = ['0VesselDamaged','1VesselDamaged','2VesselDamaged','3VesselDamaged','1VesselDamaged']
        dom_entitlements_dict['VesselsDamaged'] = vessels_dmg

        ca_year = re.findall('cayr_\d+', entailments)
        dom_entitlements_dict['YearlyyCardiacCath'] = ca_year

        # BloodVesselsDiagnosis

        circumflex = re.findall('cxmain_\d+', entailments)
        dom_entitlements_dict['Circumflex'] = circumflex

        dist_left_anterior = re.findall('laddist_\d+', entailments)
        dom_entitlements_dict['DistalLeftAnteriorDescendingArtery'] = dist_left_anterior

        dist_right_anterior = re.findall('rcadist_\d+', entailments)
        dom_entitlements_dict['DistalRightAnteriorDescendingArtery'] = dist_right_anterior

        left_main_truck = re.findall('lmt_\d+', entailments)
        dom_entitlements_dict['LeftMainTruck'] = left_main_truck
        
        prox_left_anterior = re.findall('ladprox_\d+', entailments)
        dom_entitlements_dict['ProximaLeftAnteriorDescendingArtery'] = prox_left_anterior

        prox_right_anterior = re.findall('rcaprox_\d+', entailments)
        dom_entitlements_dict['ProximaRightAnteriorDescendingArtery'] = prox_right_anterior

        entitlements_dict[domain] = dom_entitlements_dict
        print(f"=========== Finish storing entailments for domain: {domain} =========== \n")

    return entitlements_dict

def existence(value, list2):
    return True if value in list2 else False


        

def main():

    transfer_dir = '/home/juandiri/TFM/Project/Sample/Results/'
    ents_dir = '/home/juandiri/TFM/Project/Sample/Results/Entailments/'
    #domains = ["Cleveland", "Hungary"]
    domains = ["Cleveland", "Hungary", "LongBeach", "Switzerland"]
    correlation_dir = os.path.join(transfer_dir, 'Corr')
    if not os.path.exists(correlation_dir):
        os.mkdir(correlation_dir)
   
    entailment_dictionary = get_entitlement_per_entity(ents_dir, domains)
    #entailment_dictionary = dict()

    # Enquiry over entailment closure and explanatory knowledge
    # entailment mapping: 

    
    def ent_existence(source_domain:str, target_domain:str):
        entailment_source = entailment_dictionary[source_domain]
        entailment_target = entailment_dictionary[target_domain]

        entailment_existence = dict()
        for key in entailment_source.keys():
            for value in entailment_target[key]:
                entailment_existence[f"{value}"] = existence(value, entailment_source[key])
        return entailment_existence

    def read_transferability_indexes():
        F_Index = {}
        f = open(os.path.join(correlation_dir, 'tra.csv'), 'r')
        reader = csv.DictReader(f)
        for row in reader:
            F_Index[row['S-T']] = float(row['AUC-FI'])
        f.close()
        return F_Index

    def entailment_indexes():
        F_index = read_transferability_indexes()
        tra_v, inv_v, new_v, obs_v = [], [], [], []
        for source_domain in domains:
            for target_domain in domains:
                F_id = f"{source_domain}-{target_domain}"
                if source_domain == target_domain:
                    continue
                tra_v.append(F_index[F_id])
                entailment_source = entailment_dictionary[source_domain]
                entailment_target = entailment_dictionary[target_domain]
                new = len(set(entailment_target) - set(entailment_source)) / float(len(entailment_target))
        new_v.append(new)
        obs = len(set(entailment_source) - set(entailment_target)) / float(len(entailment_source))
        obs_v.append(obs)
        inv = len(set(entailment_source).intersection(entailment_target)) / float(len(set(entailment_source).union(entailment_target)))
        inv_v.append(inv)

    
        inv_corr, inv_p_val = stats.pearsonr(tra_v, inv_v)
        new_corr, new_p_val = stats.pearsonr(tra_v, new_v)
        obs_corr, obs_p_val = stats.pearsonr(tra_v, obs_v)
        print(f'inv_corr: {inv_corr}, inv_p_value: {inv_p_val}')
        print(f'new_corr: {new_corr}, new_p_vale: {new_p_val}')
        print(f'obs_corr: {obs_corr}, obs_p_vale: {obs_p_val}')

    entailment_indexes()

if __name__ == '__main__':
    if len(sys.argv[1:]) != 0:
        print("There are some extra parameters.")
        print((sys.argv[1:]))
        exit(1)
    main(*sys.argv[1:])