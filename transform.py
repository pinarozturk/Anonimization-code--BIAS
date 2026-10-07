import sys
import os
import pandas as pd
import unmask as u

def unmask_data(f, out):
    try:
        # Check if the input file exists
        if not os.path.exists(f):
            print("Error: Input file not found.")
            return
        # Extract the filename and extension
        _, file_extension = os.path.splitext(f)

        # Ensure the file extension is .xlsx
        if file_extension.lower() != '.xlsx':
            print("Error: Input file must have .xlsx extension.")
            return

        # Reading process starts here
        data = pd.read_excel(f, dtype={"High School Graduation Date": str})

        # ID: Rule 4 (Not needed)
        # MNGKOD: Rule 5 (Not needed)
        # Company Name: Rule 6 (Not needed)
        # Ad Code: Rule 7 (Not needed)
        # Ad Number: Rule 8 (Not needed)
        # Ad Name: Rule 9 (Not needed)

        # First Application Date: Rule 10
        data.loc[:, "First Application Date"] = data["First Application Date"].apply(u.applydate_to_date)

        # Last Application Date: Rule 11
        data.loc[:, "Last Application Date"] = data["Last Application Date"].apply(u.applydate_to_date)

        # Candidate Rerference Number: Rule 12 (Not needed)
        # CV Reference Number: Rule 13 (Not needed)
        # Name: Rule 14 (Not needed)

        # Birth Date: Rule 15
        data.loc[:, "Birth Date"] = data["Birth Date"].apply(u.birthdate_to_period_str)

        # Gender: Rule 16
        data.loc[:, "Gender"] = data["Gender"].apply(u.gender_to_str)

        # E-mail: Rule 17 (Not needed)
        # Phone Number: Rule 18 (Not needed)

        # Citizenship: Rule 19
        data.loc[:, "Citizenship"] = data["Citizenship"].apply(u.citizen_to_bool)

        # District: Rule 20 (Not needed)

        # City: Rule 21
        data.loc[:, "City"] = data["City"].apply(u.cityplate_to_float)

        # Employment Situation: Rule 22
        data.loc[:, "Employment Situation"] = data["Employment Situation"].apply(u.employsituation_to_bool)

        # Experience (time): Rule 23
        data.loc[:, "Experience (time)"] = data["Experience (time)"].apply(u.exptime_to_str)

        # Education Level: Rule 24
        data.loc[:, "Education Level"] = data["Education Level"].apply(u.education_to_int)

        # Graduation Status: Rule 25
        data.loc[:, "Graduation Status"] = data["Graduation Status"].apply(u.graduation_to_str)

        # Disability Status: Rule 26
        data.loc[:, "Disability Status"] = data["Disability Status"].apply(u.disability_to_bool)

        # Driving License: Rule 27 (Not needed)

        # Computer Information: Rule 28
        _offset = 100
        data.loc[:, "Computer Information"] = u.slide_col(data.loc[:, "Computer Information"], _offset)

        # Military Status: Rule 29 (MISSING)

        # High School Name: Rule 30
        _offset = 50
        data.loc[:, "High School Name"] = u.slide_col(data.loc[:, "High School Name"], _offset)

        # High School Type: Rule 31
        _offset = 200
        data.loc[:, "High School Type"] = u.slide_col(data.loc[:, "High School Type"], _offset)

        # High School Department: Rule 32
        _offset = 1000
        data.loc[:, "High School Department"] = u.slide_col(data.loc[:, "High School Department"], _offset)

        # High School Graduation Date: Rule 33
        _offset = 5000
        data.loc[:, "High School Graduation Date"] = u.slide_col(data.loc[:, "High School Graduation Date"], _offset)

        # Language 1: Rule 34
        data.loc[:, "Language 1"] = data["Language 1"].apply(u.language_to_str)

        # Reading 1: Rule 35
        data.loc[:, "Reading 1"] = data["Reading 1"].apply(u.langskill_to_str)

        # Writing 1: Rule 36
        data.loc[:, "Writing 1"] = data["Writing 1"].apply(u.langskill_to_str)

        # Speaking 1: Rule 37
        data.loc[:, "Speaking 1"] = data["Speaking 1"].apply(u.langskill_to_str)

        # Language 2: Rule 38
        data.loc[:, "Language 2"] = data["Language 2"].apply(u.language_to_str)

        # Reading 2: Rule 39
        data.loc[:, "Reading 2"] = data["Reading 2"].apply(u.langskill_to_str)

        # Writing 2: Rule 40
        data.loc[:, "Writing 2"] = data["Writing 2"].apply(u.langskill_to_str)

        # Speaking 2: Rule 41
        data.loc[:, "Speaking 2"] = data["Speaking 2"].apply(u.langskill_to_str)

        # Language 3: Rule 42
        data.loc[:, "Language 3"] = data["Language 3"].apply(u.language_to_str)

        # Reading 3: Rule 43
        data.loc[:, "Reading 3"] = data["Reading 3"].apply(u.langskill_to_str)

        # Writing 3: Rule 44
        data.loc[:, "Writing 3"] = data["Writing 3"].apply(u.langskill_to_str)

        # Speaking 3: Rule 45
        data.loc[:, "Speaking 3"] = data["Speaking 3"].apply(u.langskill_to_str)

        # Workplace 1: Rule 46 (Not Implemented)
        # Position 1: Rule 47 (Not needed)

        # Start Year Experience 1: Rule 48
        data.loc[:, "Start Year Experience 1"] = data["Start Year Experience 1"].apply(u.expyears_to_date)

        # Start Month Experience 1: Rule 49
        data.loc[:, "Start Month Experience 1"] = data["Start Month Experience 1"].apply(u.quarter_to_date)

        # End Year Experience 1: Rule 50
        data.loc[:, "End Year Experience 1"] = data["End Year Experience 1"].apply(u.expyears_to_date)

        # End Month Experience 1: Rule 51
        data.loc[:, "End Month Experience 1"] = data["End Month Experience 1"].apply(u.quarter_to_date)

        # Workplace 2: Rule 52 (Not Implemented)
        # Position 2: Rule 53 (Not needed)

        # Start Year Experience 2: Rule 54
        data.loc[:, "Start Year Experience 2"] = data["Start Year Experience 2"].apply(u.expyears_to_date)

        # Start Month Experience 2: Rule 55
        data.loc[:, "Start Month Experience 2"] = data["Start Month Experience 2"].apply(u.quarter_to_date)

        # End Year Experience 2: Rule 56
        data.loc[:, "End Year Experience 2"] = data["End Year Experience 2"].apply(u.expyears_to_date)

        # End Month Experience 2: Rule 57
        data.loc[:, "End Month Experience 2"] = data["End Month Experience 2"].apply(u.quarter_to_date)

        # Workplace 3: Rule 58 (Not Implemented)
        # Position 3: Rule 59 (Not needed)

        # Start Year Experience 3: Rule 60
        data.loc[:, "Start Year Experience 3"] = data["Start Year Experience 3"].apply(u.expyears_to_date)

        # Start Mount Experience 3: Rule 61
        data.loc[:, "Start Mount Experience 3"] = data["Start Mount Experience 3"].apply(u.quarter_to_date)

        # End Year Experience 3: Rule 62
        data.loc[:, "End Year Experience 3"] = data["End Year Experience 3"].apply(u.expyears_to_date)

        # End Mount Experience 3: Rule 63
        data.loc[:, "End Mount Experience 3"] = data["End Mount Experience 3"].apply(u.quarter_to_date)

        # University 1: Rule 64 (Not needed)
        # Department 1: Rule 65 (Not Implemented)

        # Start Year 1: Rule 66
        data.loc[:, "Start Year 1"] = data["Start Year 1"].apply(u.expyears_to_date)

        # Start Month 1: Rule 67
        data.loc[:, "Start Month 1"] = data["Start Month 1"].apply(u.quarter_to_date)

        # End Year 1: Rule 68
        data.loc[:, "End Year 1"] = data["End Year 1"].apply(u.expyears_to_date)

        # End Month 1: Rule 69
        data.loc[:, "End Month 1"] = data["End Month 1"].apply(u.quarter_to_date)

        # University 2: Rule 70 (Not needed)
        # Department 2: Rule 71 (Not Implemented)

        # Start Year 2: Rule 72
        data.loc[:, "Start Year 2"] = data["Start Year 2"].apply(u.expyears_to_date)

        # Start Month 2: Rule 73
        data.loc[:, "Start Month 2"] = data["Start Month 2"].apply(u.quarter_to_date)

        # End Year 2: Rule 74
        data.loc[:, "End Year 2"] = data["End Year 2"].apply(u.expyears_to_date)

        # End Month 2: Rule 75
        data.loc[:, "End Month 2"] = data["End Month 2"].apply(u.quarter_to_date)

        # University 3: Rule 76 (Not needed)
        # Department 3: Rule 77 (Not Implemented)

        # Start Year 3: Rule 78
        data.loc[:, "Start Year 3"] = data["Start Year 3"].apply(u.expyears_to_date)

        # Start Month 3: Rule 79
        data.loc[:, "Start Month 3"] = data["Start Month 3"].apply(u.quarter_to_date)

        # End Year 3: Rule 80
        data.loc[:, "End Year 3"] = data["End Year 3"].apply(u.expyears_to_date)

        # End Year 3.1: Rule 81
        data.loc[:, "End Year 3.1"] = data["End Year 3.1"].apply(u.quarter_to_date)

        data.to_csv(f"{out}.csv", index=False)

    except Exception as e:
        print("An error ocurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python transform.py <input.xlsx> <output.xlsx>")
        sys.exit(1)

    xlsx_file = sys.argv[1]
    out_file = sys.argv[2]
    unmask_data(xlsx_file, out_file)
