import pandas as pd
import re
from fuzzywuzzy import process


def validate_and_find_nearest(code, valid_codes):
    icao_pattern = re.compile(r'^[A-Z]{4}$')
    if re.match(icao_pattern, code):
        return code
    else:
        closest_match, _ = process.extractOne(code, valid_codes)
        return closest_match


# Read CSV file into a DataFrame
csv_file_path = 'data/1Logbook.csv'
df = pd.read_csv(csv_file_path)


valid_icao_codes = ['KBDN', 'KRDM', 'S39', 'S21', 'KDLS', '62S']


df['Valid_ICAO_Code'] = df['ICAO_Code'].apply(lambda x: validate_and_find_nearest(x, valid_icao_codes))


print(df)

header = ['Date',
          'Aircraft Make and Model',
          'Aircraft Ident',
          'From',
          'To',
          'Total Duration of Flight',
          'Airplane Single-Engine Land',
          'Airplane Single-Engine Sea',
          'Airplane Multi-Engine Land',
          'Ground Instruction',
          'Day Landings',
          'Night Landings',
          'Night',
          'Actual Instrument',
          'Simulated Instrument',
          'Flight Simulator',
          'Cross-Country',
          'Solo',
          'Pilot in Command',
          'Second in Command',
          'Dual Received',
          'As Flight Instructor',
          'Remarks and Endorsements',
          ]
