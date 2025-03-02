"""
Medical information handling utilities for the Clinical Trial Analysis Platform.
"""

import streamlit as st
from datetime import datetime
from .translations import get_translation, SUPPORTED_LANGUAGES

def render_medical_info_page(language: str):
    """
    Render the medical information entry page.
    
    Args:
        language (str): Current language code
    """
    st.title(get_translation('medical_info_title', language))
    
    # Language Selector
    language_options = list(SUPPORTED_LANGUAGES.keys())
    current_language_index = language_options.index(
        next(k for k, v in SUPPORTED_LANGUAGES.items() if v == st.session_state.language)
    )
    
    selected_language = st.selectbox(
        get_translation('language_selector', language),
        options=language_options,
        index=current_language_index,
        key='language_select'
    )
    
    # Update language if changed
    new_language = SUPPORTED_LANGUAGES[selected_language]
    if new_language != st.session_state.language:
        st.session_state.language = new_language
        st.rerun()
    
    # Create tabs for different sections
    tabs = st.tabs([
        get_translation('demographics', language),
        get_translation('vital_signs', language),
        get_translation('medical_history', language),
        get_translation('medications', language),
        get_translation('lab_results', language),
        get_translation('imaging', language),
        get_translation('procedures', language),
        get_translation('lifestyle', language),
        get_translation('family_history', language),
        get_translation('rare_diseases', language)
    ])
    
    with tabs[0]:
        render_demographics(language)
    
    with tabs[1]:
        render_vital_signs(language)
        
    with tabs[2]:
        render_medical_history(language)
        
    with tabs[3]:
        render_medications(language)
        
    with tabs[4]:
        render_lab_results(language)
        
    with tabs[5]:
        render_imaging(language)
        
    with tabs[6]:
        render_procedures(language)
        
    with tabs[7]:
        render_lifestyle(language)
        
    with tabs[8]:
        render_family_history(language)
        
    with tabs[9]:
        render_rare_diseases(language)

def render_demographics(language: str):
    """Render demographics section."""
    # Get existing data from session state
    demographics_data = st.session_state.get('demographics_data', {})
    
    col1, col2 = st.columns(2)
    
    with col1:
        dob = st.date_input(
            get_translation('date_of_birth', language),
            value=demographics_data.get('dob', datetime(1900, 1, 1)),
            min_value=datetime(1900, 1, 1),
            key="dob"
        )
        
        # Define gender options using translation keys
        gender_options = ['gender_male', 'gender_female', 'gender_other']
        translated_genders = [get_translation(g, language) for g in gender_options]
        
        # Get the current gender value and find its index, with fallback handling
        current_gender = demographics_data.get('gender', 'gender_male')
        try:
            current_gender_index = gender_options.index(current_gender)
        except ValueError:
            # If the stored value is a translated string, find its corresponding key
            try:
                current_gender_index = translated_genders.index(current_gender)
            except ValueError:
                current_gender_index = 0  # Default to first option if not found
        
        gender = st.selectbox(
            get_translation('gender', language),
            options=translated_genders,
            index=current_gender_index,
            key="gender"
        )
        race = st.selectbox(
            get_translation('race/ethnicity', language),
            options=[get_translation('caucasian or white', language), get_translation('asian', language), get_translation('black or african american', language), get_translation('hispanic', language), get_translation('other', language)],
        )
   
        
        insurance = st.text_input(
            get_translation('insurance_provider', language),
            value=demographics_data.get('insurance', ''),
            key="insurance_provider"
        )

    with col2:
        emergency_name = st.text_input(
            get_translation('emergency_contact_name', language),
            value=demographics_data.get('emergency_name', ''),
            key="emergency_contact_name"
        )
        emergency_phone = st.text_input(
            get_translation('emergency_contact_phone', language),
            value=demographics_data.get('emergency_phone', ''),
            key="emergency_contact_phone"
        )
        physician = st.text_input(
            get_translation('primary_care_physician', language),
            value=demographics_data.get('physician', ''),
            key="primary_care_physician"
        )

    # Save button
    if st.button("Save Demographics"):
        # Get the selected gender key based on the translated selection
        selected_gender_key = gender_options[translated_genders.index(gender)]
        
        # Get the selected ethnicity key based on the translated selection
        selected_ethnicity_key = race
        
        new_data = {
            'dob': dob,
            'gender': selected_gender_key,
            'ethnicity': selected_ethnicity_key,
            'insurance': insurance,
            'emergency_name': emergency_name,
            'emergency_phone': emergency_phone,
            'physician': physician
        }
        st.session_state.demographics_data = new_data
        st.success("Demographics data saved successfully!")

def render_vital_signs(language: str):
    """Render vital signs section."""
    # Get existing data from session state
    vital_signs_data = st.session_state.get('vital_signs_data', {})
    
    col1, col2 = st.columns(2)
    
    with col1:
        height = st.number_input(
            get_translation('height', language),
            min_value=0,
            max_value=300,
            value=vital_signs_data.get('height', 0)
        )
        weight = st.number_input(
            get_translation('weight', language),
            min_value=0,
            max_value=500,
            value=vital_signs_data.get('weight', 0)
        )
        temperature = st.number_input(
            get_translation('body_temperature', language),
            min_value=35.0,
            max_value=42.0,
            step=0.1,
            value=vital_signs_data.get('temperature', 37.0)
        )
        respiratory_rate = st.number_input(
            get_translation('respiratory_rate', language),
            min_value=0,
            max_value=60,
            value=vital_signs_data.get('respiratory_rate', 0)
        )

    with col2:
        systolic = st.number_input(
            get_translation('blood_pressure_systolic', language),
            min_value=0,
            max_value=250,
            value=vital_signs_data.get('systolic', 0)
        )
        diastolic = st.number_input(
            get_translation('blood_pressure_diastolic', language),
            min_value=0,
            max_value=200,
            value=vital_signs_data.get('diastolic', 0)
        )
        heart_rate = st.number_input(
            get_translation('heart_rate', language),
            min_value=0,
            max_value=250,
            value=vital_signs_data.get('heart_rate', 0)
        )

    # Save button
    if st.button("Save Vital Signs"):
        new_data = {
            'height': height,
            'weight': weight,
            'temperature': temperature,
            'respiratory_rate': respiratory_rate,
            'systolic': systolic,
            'diastolic': diastolic,
            'heart_rate': heart_rate
        }
        st.session_state.vital_signs_data = new_data
        st.success("Vital signs data saved successfully!")

def render_medical_history(language: str):
    """Render medical history section."""
    st.subheader(get_translation('current_medical_conditions', language))
    # Initialize diagnoses list in session state if it doesn't exist
    if 'diagnoses' not in st.session_state:
        st.session_state.diagnoses = []
    
    # Display existing diagnoses with remove buttons
    for i, diagnosis in enumerate(st.session_state.diagnoses):
        container = st.container()
        col1, col2 = container.columns([9, 1])
        
        with col1:
            st.session_state.diagnoses[i] = st.text_input(
                label=get_translation('diagnosis', language),
                value=diagnosis,
                key=f"diagnosis_{i}",
                label_visibility="collapsed"
            )
        
        with col2:
            if st.button("✕", key=f"remove_{i}", help=get_translation('remove_diagnosis', language), use_container_width=True):
                st.session_state.diagnoses.pop(i)
                st.rerun()
    
    # Add new diagnosis button
    if st.button(get_translation('add_diagnosis', language)):
        st.session_state.diagnoses.append("")
        st.rerun()
    
    # Past Medical History section
    st.subheader(get_translation('past_medical_history', language))
    if 'past_conditions' not in st.session_state:
        st.session_state.past_conditions = []
    
    for i, condition in enumerate(st.session_state.past_conditions):
        container = st.container()
        col1, col2 = container.columns([9, 1])
        
        with col1:
            st.session_state.past_conditions[i] = st.text_input(
                label=get_translation('previous_conditions', language),
                value=condition,
                key=f"past_condition_{i}",
                label_visibility="collapsed"
            )
        
        with col2:
            if st.button("✕", key=f"remove_past_{i}", help=get_translation('remove_diagnosis', language), use_container_width=True):
                st.session_state.past_conditions.pop(i)
                st.rerun()
    
    if st.button(f"{get_translation('add_diagnosis', language)} ({get_translation('past_medical_history', language)})"):
        st.session_state.past_conditions.append("")
        st.rerun()
    
    # Allergies section
    st.subheader(get_translation('allergies_adverse_reactions', language))
    col1, col2 = st.columns(2)
    with col1:
        st.multiselect(get_translation('medication_allergies', language), [
            "Penicillin", "Sulfa", "NSAIDs", "Other"
        ])
    with col2:
        st.text_input(get_translation('reaction_description', language))
    
    # Immunizations section
    st.subheader(get_translation('immunizations', language))
    if 'immunizations' not in st.session_state:
        st.session_state.immunizations = []
    
    for i, immunization in enumerate(st.session_state.immunizations):
        container = st.container()
        col1, col2 = container.columns([8, 1])
        
        with col1:
            st.session_state.immunizations[i] = st.text_input(
                label=get_translation('vaccination_history', language),
                value=immunization,
                key=f"immunization_{i}",
                label_visibility="collapsed"
            )
        
        with col2:
            if st.button("✕", key=f"remove_imm_{i}", help=get_translation('remove_diagnosis', language), use_container_width=True):
                st.session_state.immunizations.pop(i)
                st.rerun()
    
    if st.button(get_translation('add_immunization', language)):
        st.session_state.immunizations.append("")
        st.rerun()

def render_medications(language: str):
    """Render the Current Medications section dynamically."""

    # Initialize session state for medications if not present
    if "medications" not in st.session_state:
        st.session_state.medications = []

    st.subheader(get_translation('current_medications', language))

    # Loop through existing medication entries
    for i in range(len(st.session_state.medications)):
        col1, col2, col3, col4 = st.columns([3, 2, 2, 1])  # Last column for remove button

        with col1:
            st.session_state.medications[i]["name"] = st.text_input(
                get_translation('medication_name', language),
                value=st.session_state.medications[i]["name"],
                key=f"med_name_{i}"
            )

        with col2:
            st.session_state.medications[i]["dose"] = st.text_input(
                get_translation('dosage', language),
                value=st.session_state.medications[i]["dose"],
                key=f"med_dose_{i}"
            )

        with col3:
            st.session_state.medications[i]["freq"] = st.selectbox(
                get_translation('frequency', language),
                [
                    get_translation('once_daily', language),
                    get_translation('twice_daily', language),
                    get_translation('three_times_daily', language),
                    get_translation('four_times_daily', language),
                    get_translation('as_needed', language),
                    get_translation('weekly', language),
                    get_translation('monthly', language)
                ],
                index=[
                    get_translation('once_daily', language),
                    get_translation('twice_daily', language),
                    get_translation('three_times_daily', language),
                    get_translation('four_times_daily', language),
                    get_translation('as_needed', language),
                    get_translation('weekly', language),
                    get_translation('monthly', language)
                ].index(st.session_state.medications[i]["freq"]),
                key=f"med_freq_{i}"
            )

        # Remove button with same styling as immunizations
        with col4:
            if st.button("✕", key=f"remove_med_{i}", help=get_translation('remove_diagnosis', language), use_container_width=True):
                st.session_state.medications.pop(i)
                st.rerun()

    # Button to add a new medication entry
    if st.button("➕ Add Medication"):
        st.session_state.medications.append({"name": "", "dose": "", "freq": get_translation('once_daily', language)})
        st.rerun()

    st.subheader(get_translation('past_medications', language))
    st.text_area(get_translation('previous_medications_history', language))

def render_lab_results(language: str):
    """Render laboratory results section."""
    # Get existing data from session state
    lab_results_data = st.session_state.get('lab_results_data', {})
    
    st.subheader(get_translation('recent_laboratory_results', language))
    
    # Basic Blood Panel
    st.markdown(f"#### {get_translation('complete_blood_count', language)}")
    col1, col2 = st.columns(2)
    with col1:
        hemoglobin = st.number_input(
            get_translation('hemoglobin', language),
            value=lab_results_data.get('hemoglobin', 0.0)
        )
        wbc = st.number_input(
            get_translation('white_blood_cell_count', language),
            value=lab_results_data.get('wbc', 0.0)
        )
    with col2:
        platelets = st.number_input(
            get_translation('platelet_count', language),
            value=lab_results_data.get('platelets', 0.0)
        )
        cbc_date = st.date_input(
            get_translation('test_date', language),
            value=lab_results_data.get('cbc_date', datetime.now()),
            key="cbc_date"
        )
    
    # Chemistry Panel
    st.markdown(f"#### {get_translation('basic_metabolic_panel', language)}")
    col1, col2 = st.columns(2)
    with col1:
        glucose = st.number_input(
            get_translation('glucose', language),
            value=lab_results_data.get('glucose', 0.0)
        )
        creatinine = st.number_input(
            get_translation('creatinine', language),
            value=lab_results_data.get('creatinine', 0.0)
        )
    with col2:
        sodium = st.number_input(
            get_translation('sodium', language),
            value=lab_results_data.get('sodium', 0.0)
        )
        potassium = st.number_input(
            get_translation('potassium', language),
            value=lab_results_data.get('potassium', 0.0)
        )

    # Save button
    if st.button("Save Lab Results"):
        new_data = {
            'hemoglobin': hemoglobin,
            'wbc': wbc,
            'platelets': platelets,
            'cbc_date': cbc_date,
            'glucose': glucose,
            'creatinine': creatinine,
            'sodium': sodium,
            'potassium': potassium
        }
        st.session_state.lab_results_data = new_data
        st.success("Lab results saved successfully!")

def render_imaging(language: str):
    """Render imaging studies section."""
    # Get existing data from session state
    imaging_data = st.session_state.get('imaging_data', {})
    
    st.subheader(get_translation('imaging_studies', language))
    
    imaging_types = ["X-Ray", "CT Scan", "MRI", "Ultrasound", "PET Scan"]
    current_imaging_data = {}
    
    for type in imaging_types:
        st.markdown(f"#### {type}")
        col1, col2 = st.columns(2)
        type_data = imaging_data.get(type, {})
        
        with col1:
            study_date = st.date_input(
                get_translation('study_date', language),
                value=type_data.get('date', datetime.now()),
                key=f"img_date_{type}"
            )
            body_region = st.text_input(
                get_translation('body_region', language),
                value=type_data.get('region', ''),
                key=f"img_region_{type}"
            )
        with col2:
            findings = st.text_area(
                get_translation('findings', language),
                value=type_data.get('findings', ''),
                key=f"img_findings_{type}"
            )
        
        current_imaging_data[type] = {
            'date': study_date,
            'region': body_region,
            'findings': findings
        }

    # Save button
    if st.button(get_translation('save_imaging', language)):
        st.session_state.imaging_data = current_imaging_data
        st.success(get_translation('imaging_saved', language))

def render_procedures(language: str):
    """Render procedures section."""
    # Get existing data from session state
    procedures_data = st.session_state.get('procedures_data', {})
    
    st.subheader(get_translation('surgical_procedures', language))
    surgical_procedures = []
    
    for i in range(3):
        col1, col2 = st.columns(2)
        proc_data = procedures_data.get(f'procedure_{i}', {})
        
        with col1:
            name = st.text_input(
                get_translation('procedure_name', language),
                value=proc_data.get('name', ''),
                key=f"proc_name_{i}"
            )
            date = st.date_input(
                get_translation('procedure_date', language),
                value=proc_data.get('date', datetime.now()),
                key=f"proc_date_{i}"
            )
        with col2:
            notes = st.text_area(
                get_translation('procedure_notes', language),
                value=proc_data.get('notes', ''),
                key=f"proc_notes_{i}"
            )
        
        surgical_procedures.append({
            'name': name,
            'date': date,
            'notes': notes
        })
    
    st.subheader(get_translation('other_procedures', language))
    other_procedures = st.text_area(
        get_translation('non_surgical_procedures', language),
        value=procedures_data.get('other_procedures', '')
    )

    # Save button
    if st.button(get_translation('save_procedures', language)):
        new_data = {
            f'procedure_{i}': proc_data 
            for i, proc_data in enumerate(surgical_procedures)
        }
        new_data['other_procedures'] = other_procedures
        st.session_state.procedures_data = new_data
        st.success(get_translation('procedures_saved', language))

def render_lifestyle(language: str):
    """Render lifestyle section."""
    # Get existing data from session state
    lifestyle_data = st.session_state.get('lifestyle_data', {})
    
    col1, col2 = st.columns(2)
    
    with col1:
        smoking_status = st.selectbox(
            get_translation('smoking_status', language),
            [
                get_translation('never', language),
                get_translation('former', language),
                get_translation('current', language)
            ],
            index=['never', 'former', 'current'].index(lifestyle_data.get('smoking_status', 'never'))
        )
        
        years_smoking = None
        cigarettes_per_day = None
        if smoking_status in [get_translation('former', language), get_translation('current', language)]:
            years_smoking = st.number_input(
                get_translation('years_of_smoking', language),
                value=lifestyle_data.get('years_smoking', 0)
            )
            cigarettes_per_day = st.number_input(
                get_translation('cigarettes_per_day', language),
                value=lifestyle_data.get('cigarettes_per_day', 0)
            )
        
        activity_level = st.selectbox(
            get_translation('physical_activity_level', language),
            [
                get_translation('sedentary', language),
                get_translation('light', language),
                get_translation('moderate', language),
                get_translation('very_active', language),
                get_translation('extremely_active', language)
            ],
            index=['sedentary', 'light', 'moderate', 'very_active', 'extremely_active'].index(
                lifestyle_data.get('activity_level', 'sedentary'))
        )
    
    with col2:
        alcohol_status = st.selectbox(
            get_translation('alcohol_consumption', language),
            [
                get_translation('none', language),
                get_translation('occasional', language),
                get_translation('regular', language)
            ],
            index=['none', 'occasional', 'regular'].index(lifestyle_data.get('alcohol_status', 'none'))
        )
        
        drinks_per_week = None
        if alcohol_status in [get_translation('occasional', language), get_translation('regular', language)]:
            drinks_per_week = st.number_input(
                get_translation('drinks_per_week', language),
                value=lifestyle_data.get('drinks_per_week', 0)
            )
        
        dietary_restrictions = st.text_area(
            get_translation('dietary_restrictions', language),
            value=lifestyle_data.get('dietary_restrictions', '')
        )

    # Save button
    if st.button(get_translation('save_lifestyle', language)):
        new_data = {
            'smoking_status': smoking_status,
            'activity_level': activity_level,
            'alcohol_status': alcohol_status,
            'dietary_restrictions': dietary_restrictions
        }
        
        if years_smoking is not None:
            new_data['years_smoking'] = years_smoking
        if cigarettes_per_day is not None:
            new_data['cigarettes_per_day'] = cigarettes_per_day
        if drinks_per_week is not None:
            new_data['drinks_per_week'] = drinks_per_week
            
        st.session_state.lifestyle_data = new_data
        st.success(get_translation('lifestyle_saved', language))

def render_family_history(language: str):
    """Render family history section."""
    # Get existing data from session state
    family_history_data = st.session_state.get('family_history_data', {})
    
    relatives = [
        get_translation('mother', language),
        get_translation('father', language),
        get_translation('siblings', language),
        get_translation('children', language),
        get_translation('grandparents', language)
    ]
    conditions = [
        get_translation('heart_disease', language),
        get_translation('diabetes', language),
        get_translation('cancer', language),
        get_translation('hypertension', language),
        get_translation('stroke', language),
        get_translation('mental_health_conditions', language),
        get_translation('other', language)
    ]
    
    current_data = {}
    
    for relative in relatives:
        st.subheader(get_translation('family_member_history', language) % relative)
        relative_key = relative.lower().replace(' ', '_')
        
        selected_conditions = st.multiselect(
            get_translation('medical_conditions', language) % relative,
            conditions,
            default=family_history_data.get(f"{relative_key}_conditions", []),
            key=f"fh_{relative}"
        )
        
        additional_notes = st.text_area(
            get_translation('additional_details', language) % relative,
            value=family_history_data.get(f"{relative_key}_notes", ""),
            key=f"fh_notes_{relative}"
        )
        
        current_data[f"{relative_key}_conditions"] = selected_conditions
        current_data[f"{relative_key}_notes"] = additional_notes

    # Save button
    if st.button(get_translation('save_family_history', language)):
        st.session_state.family_history_data = current_data
        st.success(get_translation('family_history_saved', language))

def render_rare_diseases(language: str):
    """Render rare diseases section."""
    # Get existing data from session state
    rare_diseases_data = st.session_state.get('rare_diseases_data', {})
    
    col1, col2 = st.columns(2)
    
    rare_diseases = [
        "Achalasia", "Addison's Disease", "Alkaptonuria",
        "Amyloidosis", "Angelman Syndrome", "Ataxia Telangiectasia",
        "Behcet's Disease", "Castleman Disease", "Cushing's Syndrome",
        "Dercum's Disease", "Ehlers-Danlos Syndrome", "Fabry Disease",
        "Gaucher Disease", "Hereditary Angioedema", "Huntington's Disease",
        "Kawasaki Disease", "Kleine-Levin Syndrome", "Krabbe Disease",
        "Marfan Syndrome", "Myasthenia Gravis", "Niemann-Pick Disease",
        "Paget's Disease", "Pompe Disease", "Prader-Willi Syndrome",
        "Rett Syndrome", "Sarcoidosis", "Scleroderma",
        "Syringomyelia", "Tay-Sachs Disease", "Turner Syndrome",
        "Von Hippel-Lindau Disease", "Wilson's Disease",
        "X-linked Agammaglobulinemia", "Zollinger-Ellison Syndrome"
    ]
    
    with col1:
        diagnosed_diseases = st.multiselect(
            get_translation('diagnosed_rare_diseases', language),
            rare_diseases,
            default=rare_diseases_data.get('diagnosed_diseases', [])
        )
        diagnosed_notes = st.text_area(
            get_translation('additional_notes_diagnosed', language),
            value=rare_diseases_data.get('diagnosed_notes', '')
        )
        
    with col2:
        suspected_diseases = st.multiselect(
            get_translation('suspected_rare_diseases', language),
            rare_diseases,
            default=rare_diseases_data.get('suspected_diseases', [])
        )
        symptoms = st.text_area(
            get_translation('symptoms_observations', language),
            value=rare_diseases_data.get('symptoms', '')
        )
    
    st.subheader(get_translation('genetic_testing', language))
    col3, col4 = st.columns(2)
    
    with col3:
        testing_status = st.selectbox(
            get_translation('genetic_testing_status', language),
            [
                get_translation('not_done', language),
                get_translation('scheduled', language),
                get_translation('completed', language)
            ],
            index=['not_done', 'scheduled', 'completed'].index(
                rare_diseases_data.get('testing_status', 'not_done')
            )
        )
        
        testing_date = None
        if testing_status in [get_translation('scheduled', language), get_translation('completed', language)]:
            testing_date = st.date_input(
                get_translation('testing_date', language),
                value=rare_diseases_data.get('testing_date', datetime.now())
            )
    
    with col4:
        testing_results = st.text_area(
            get_translation('genetic_testing_results', language),
            value=rare_diseases_data.get('testing_results', '')
        )
        genetic_conditions = st.text_area(
            get_translation('family_genetic_conditions', language),
            value=rare_diseases_data.get('genetic_conditions', '')
        )

    # Save button
    if st.button(get_translation('save_rare_diseases', language)):
        new_data = {
            'diagnosed_diseases': diagnosed_diseases,
            'diagnosed_notes': diagnosed_notes,
            'suspected_diseases': suspected_diseases,
            'symptoms': symptoms,
            'testing_status': testing_status,
            'testing_results': testing_results,
            'genetic_conditions': genetic_conditions
        }
        
        if testing_date is not None:
            new_data['testing_date'] = testing_date
            
        st.session_state.rare_diseases_data = new_data
        st.success(get_translation('rare_diseases_saved', language)) 