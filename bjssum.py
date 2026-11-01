#!/data/data/com.termux/files/usr/bin/python
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
hsym  = home + '/symlink'
import sys
if not hbin in sys.path:
   sys.path.append(hbin)
from ansicolors import *

import os, sys
sdn   = os.path.dirname(sys.argv[0])
sbn   = os.path.basename(sys.argv[0])
sne   = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home  = '/data/data/com.termux/files/home'
hbak  = home + '/bak'
hbin  = home + '/bin'
verbose = False

import time
start_time = time.time()

import osl
osl.osl(sys.argv[0])  # Example: symlink a specific file
for message in osl.info:
    print(message)

args = sys.argv[1:]
jargs = ' '.join(args).strip()

import inspect
def usg():
    usg = inspect.cleandoc(f'''
    alias: {fgr} {frs}
 function: {fyl} {frs}
    usage: {frs} {sbn} [argument]
    ''')
    print(f'{usg}')
 
#insert_your_codes_here

""" this is how the input formatted
00,Admin,2025-08-29,15:22,undefined,2025-08-29,15:47,undefined,2025-08-29,15:48,undefined
01,Entin Sukaesih,2025-08-31,12:34,checkIn,2025-08-31,21:48,checkOut,2025-09-01,11:31,checkIn
02,Fikri Fathurohman,2025-08-31,11:50,checkIn,2025-08-31,21:47,checkOut,2025-09-01,12:12,checkIn
"""

try:
   import xlsxwriter
except Exception:
   os.system(f'pip install xlsxwriter')
   import xlsxwriter

import datetime
import csv
from io import StringIO
import sys
import os

# Team jobno
"""
data:[01] Entin Sukaesih,100000,5,500000
data:[02] Fikri Fathurohman,100000,5,500000
data:[03] Mulyana Santosa Machyar SE,125000,5,625000
data:[04] Nonoy Nurjanah,100000,5,500000
data:[05] Oon Wartia,100000,5,500000
data:[06] Sopiah,100000,5,500000
data:[07] Yuli Yanti,100000,5,500000
data:[08] Galih Ramanda,100000,5,500000
data:[09] Agus Rohendi,100000,5,500000
data:[10] Esih,100000,5,500000
data:[11] Ade Sutisna,150000,5,750000
data:[12] Jajang,100000,5,500000
data:[13] Tini Wartini,100000,5,500000
data:[14] Yana,100000,5,500000
data:[15] Wartijah,125000,5,625000
data:[16] Ai Kokon,125000,5,625000
data:[17] Beben Sobana,100000,5,500000
data:[18] Bryandita Fahmi Alamin,100000,5,500000
data:[19] Fitri Dwiyanti,100000,5,500000
data:[20] Kamal Abdul Aziz,100000,5,500000
data:[21] Noviyan,100000,5,500000
data:[22] Restiana Nurhovipah,100000,5,500000
data:[23] Siti Jubaedah,100000,4,400000
data:[24] Syifa Nurmala,100000,5,500000
data:[25] Teguh Muhammad Ramdan,100000,5,500000
data:[26] Andri Fujiawan,100000,5,500000
data:[27] Ari Januarsyah Mustafa,100000,5,500000
data:[28] Cecep Sanjaya Timorsyah,100000,5,500000
data:[29] Galih Nur Habib,100000,5,500000
data:[30] Helmi Ridwansyah,100000,5,500000
data:[31] Herman Hermawan,100000,5,500000
data:[32] Rd Muh Habil Giri Maulana J,100000,5,500000
data:[33] Riandra Agustian Putra,100000,5,500000
data:[34] Zidan Juniar Putra,100000,5,500000
data:[35] Yati Suryati Maelani,100000,5,500000
data:[36] Titi Sumiati,125000,5,625000
data:[37] Yulia Agustin,100000,5,500000
data:[39] Andre Permana,100000,5,500000
data:[40] Asep Wahyudin Permana,100000,5,500000
data:[41] Faisal G,100000,5,500000
data:[42] Eko Suherman,100000,5,500000
data:[43] Indra Putra Gumilang S.K.M,100000,5,500000
data:[44] Yuli Fridiawati,150000,5,750000
"""

# Team assignments
team_assignments = {
    'prepare'   : ['03(c):125000', '01:110000', '05:110000', '06:110000', '07:110000', '10:110000', '32:110000', '35:110000'],
    'produksi'  : ['15(c):125000', '09:110000', '11:150000', '12:110000', '13:110000', '14:110000', '17:110000', '28:110000'],
    'pemorsian' : ['16(c):125000', '04:110000', '18:110000', '19:110000', '21:110000', '22:110000', '23:110000', '24:110000', '25:110000', '34:110000'],
    'pencucian' : ['36(c):125000', '08:110000', '20:110000', '26:110000', '27:110000', '29:110000', '30:110000', '31:110000', '33:110000', '37:110000', '40:110000'],
    'distribusi': ['44(c):150000', '02:110000', '39:110000', '41:110000', '42:110000', '43:110000']
}

def create_attendance_sheet(csv_content, output_path="/sdcard/attendance.xlsx", num_dates=6):
    """
    Generates an Excel attendance sheet from CSV data, handling the specific CSV
    format provided in the comments, without merging rows, adding a column for
    total attendance, dynamically determining the start date from the oldest
    date in the CSV data, and showing all entries on each date.  Each team is placed
    on their respective sheet, and the captain of each team is noted (jobno ends with 'c').
    For all members of the 'produksi' team, their total attendance is decremented by 1.

    Args:
        csv_content (str): CSV data as a string.
        output_path (str, optional): Path to save the Excel file. Defaults to '/sdcard/attendance.xlsx'.
        num_dates (int, optional): Number of dates to include in the attendance sheet. Defaults to 7.
    """

    # String substitutions
    replacements = {
        'breakIn': 'bi',
        'breakOut': 'bo',
        'checkIn': 'ci',
        'checkOut': 'co',
        'overtimeIn': 'oi',
        'overtimeOut': 'oo',
        'undefined': 'ud'
    }

    # Identify team captains (job numbers which contains '(c)')
    team_captains = {}
    for team, members in team_assignments.items():
        team_captains[team] = [member for member in members if '(c)' in member]

    # Read the CSV data to determine the oldest date
    csv_file = StringIO(csv_content)
    csv_reader = csv.reader(csv_file)

    # Store all employee data
    employee_data = {}

    oldest_date = None
    for row in csv_reader:
        if not row:
            continue

        jobno = row[0]
        name = row[1]
        employee_data[jobno] = name

        # Process dates in the format: date, time, status, date, time, status...
        for i in range(2, len(row), 3):
            if i + 2 >= len(row):
                break  # Ensure there are enough elements

            date_str = row[i]
            if not date_str:
                continue

            try:
                date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if oldest_date is None or date_obj < oldest_date:
                    oldest_date = date_obj
            except ValueError:
                print(f"Invalid date format found: {date_str}. Skipping.")
                continue

    # If no valid dates are found, use a default start date
    if oldest_date is None:
        oldest_date = datetime.date(2025, 8, 29)
        print("No valid dates found in CSV. Using default start date: 2025-08-29")

    # Rewind the CSV file
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file)

    # Create a new Excel file.
    workbook = xlsxwriter.Workbook(output_path)

    # Create worksheets for each team
    team_worksheets = {}
    for team in team_assignments:
        team_worksheets[team] = workbook.add_worksheet(team)

    # Define formats for different parts of the sheet with comprehensive font configuration
    title_format = workbook.add_format({
        'bold': True,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14,
        'bg_color': '#D3D3D3',  # Light gray background
        'font_name': 'Arial',
        'font_color': 'black',
        'italic': False
    })

    header_format = workbook.add_format({
        'bold': True,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 10,
        'bg_color': '#E0E0E0',
        'font_name': 'Calibri',
        'font_color': 'black',
        'italic': False
    })

    left_format = workbook.add_format({
        'align': 'left',
        'font_name': 'Times New Roman',
        'font_size': 10,
        'font_color': 'black',
        'italic': False
    })

    center_format = workbook.add_format({
        'align': 'center',
        'font_name': 'Courier New',
        'font_size': 10,
        'font_color': 'black',
        'italic': False
    })

    right_format = workbook.add_format({
        'align': 'right',
        'font_name': 'Verdana',
        'font_size': 10,
        'font_color': 'black',
        'italic': False
    })    

    captain_format = workbook.add_format({
        'align': 'left',
        'font_name': 'Inconsolata',
        'font_size': 10,
        'font_color': 'blue',
        'italic': True
    })

    # Define the headers.
    headers = ['jobno', 'name']

    # Generate the date headers.
    print(f'{frd}generating date headers{frs}')
    date_headers = [(oldest_date + datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(num_dates)]
    headers.extend(date_headers)
    print(f'{frd}date headers: {fyl}{date_headers}{frs}')

    # Add the "Total Attendance" header
    headers.append("Totals")

    att_data = {}
    # Write headers and data to each team's worksheet
    for team, worksheet in team_worksheets.items():
        # Write the title to the worksheet
        title = f"Boga Jaya Santosa: {team.capitalize()} Team Attendance Records"
        # Merge cells for the title (from A1 to the last column with data)
        worksheet.merge_range(0, 0, 0, num_dates + 2, title, title_format)
        # Set row height for the title
        worksheet.set_row(0, 25)  # Adjust height as needed

        # Write the headers to the worksheet.
        for col_num, header in enumerate(headers):
            worksheet.write(1, col_num, header, header_format)
            if header == 'name':
               worksheet.set_column(col_num, col_num, len(header) + 28)
            else:
               worksheet.set_column(col_num, col_num, len(header) + 2)

        row_num = 2
        # Add team captain information to the worksheet
        captain_list = team_captains.get(team, [])
        captain_names = []
        for captain in captain_list:
            captain_jobno = captain.replace('(c)', '').rsplit(':', 1)[0]  # Remove '(c)' suffix
            captain_names.append(employee_data.get(captain_jobno, "Unknown"))
        captain_string = ", ".join(captain_names)
        # Use the stored employee data instead of re-reading the CSV
        team_members = team_assignments[team]
        team_data = []
        att_data[team] = []
        total_attendance = 0
        for jobno in team_members:
            jobno = jobno.rsplit(':', 1)[0]
            jobno_no_c = jobno.replace('(c)', '').rsplit(':', 1)[0]
            name = employee_data.get(jobno_no_c, "Unknown")
            salary_info = next((s for s in team_assignments[team] if s.startswith(jobno)), None)
            salary = int(salary_info.split(':')[1]) if salary_info else 0

            # Write jobno with left alignment
            worksheet.write(row_num, 0, jobno, left_format)
            worksheet.write(row_num, 1, name, left_format)

            attended_dates = set()
            date_entries = {}

            # Reset the CSV reader to the beginning for each employee
            csv_file.seek(0)
            csv_reader = csv.reader(csv_file)
            employee_row = None
            for row in csv_reader:
                # Check if row is not empty before accessing its elements
                if row:
                    jobno_row = row[0]
                    jobno_row_no_c = jobno_row.replace('(c)','').rsplit(':', 1)[0]
                    if jobno_row_no_c == jobno_no_c:
                        employee_row = row
                        break
                else:
                    continue  # Skip empty rows

            if employee_row:
                col_index = 2
                date_index = 0

                while date_index < len(date_headers):
                    if col_index + 2 >= len(employee_row):
                        break

                    date_str = employee_row[col_index]
                    time_str = employee_row[col_index + 1]
                    status_str = employee_row[col_index + 2]

                    if not date_str:
                        col_index += 3
                        continue

                    try:
                        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                        date_header_objs = [datetime.datetime.strptime(h, "%Y-%m-%d").date() for h in date_headers]

                        if date_obj in date_header_objs:
                            d_index = date_header_objs.index(date_obj)
                            attendance_value = f"{time_str} {status_str}".strip()

                            # Apply string replacements
                            for old, new in replacements.items():
                                attendance_value = attendance_value.replace(old, new)

                            if d_index not in date_entries:
                                date_entries[d_index] = []
                            date_entries[d_index].append(attendance_value)

                            attended_dates.add(date_obj)
                            col_index += 3
                        else:
                            col_index += 3

                    except ValueError as ve:
                        print(f"ValueError processing date: {date_str}. Error: {ve}")
                        col_index += 3  # Skip the date, time, and status
                    except IndexError:
                        print(f"IndexError at row {row_num}, column {col_index}. Check CSV format.")
                        break

                    if col_index >= len(employee_row):
                        break

                # Concatenate all entries for each date and write to the cell
                for d_index, entries in date_entries.items():
                    worksheet.write(row_num, d_index + 2, "\n".join(entries), center_format)

                # Calculate total attendance (count of unique dates)
                total_attendance = len(attended_dates)
                print(f'total_attendance-{name}: {total_attendance}')
                if total_attendance > 5:
                   total_attendance -= 1 # Limit to max 5 days
                print(f'total_attendance-{name} after_subtraction: {total_attendance}')

                # Write total attendance to the "Total Attendance" column with center alignment
                worksheet.write(row_num, len(headers) - 1, total_attendance, center_format)

            row_num += 1
            print(f'adding {name} attendance data...')

            att_data[team].append({ # Append to the team's list
                'jobno': jobno_no_c,
                'name': name,
                'salary': salary,
                'total_attendance': total_attendance,
                'total_salary': salary * total_attendance
            })

        # Add team captain information to the worksheet
        captain_list = team_captains.get(team, [])
        captain_names = []
        for captain in captain_list:
            captain_jobno = captain.replace('(c)', '').rsplit(':', 1)[0]  # Remove '(c)' suffix
            captain_names.append(employee_data.get(captain_jobno, "Unknown"))
        captain_string = ", ".join(captain_names)
        
        worksheet.write(row_num + 1, 0, f"Team Leader: {captain_string}", captain_format)
        att_data[team].append({'leader': captain_string})


    # Close the workbook.
    workbook.close()
    print(f"Excel file created at {output_path}")
    year = os.path.basename(output_path).split('-')[0]
    month = os.path.basename(output_path).split('-')[1]
    print(f'year: {year}')
    os.system(f'rcopyto.py {output_path} gdcs:bjs/attendance/{year}/{month}')
    #input(f'press Enter'); sys.exit()
    print(f'{fyl}{sne}{fmg}cas-att_data:\n{att_data}{frs}')
    return att_data

import csv
from io import StringIO
import inspect
import datetime
from datetime import timedelta

if len(sys.argv) > 1:
   csv_file = sys.argv[1]
   output_date = csv_file.rsplit('-recordList')[0].rsplit('/', 1)[1]
   print(f'csv_file: {csv_file}')
   print(f'output_date: {output_date}')
   with open(csv_file, 'r') as csvf:
        csv_content = csvf.read()
   #csv_content = sys.argv[1]
else:
   csv_content = ""
   print("No CSV content provided as a command-line argument. exiting...")
   sys.exit()
if os.path.exists(csv_file):
   outfilepath = csv_file.rsplit('.', 1)[0] + f'.xlsx'
   output_path_prefix = csv_file.rsplit('.', 1)[0]
else:
   outfilepath = '/sdcard/bjs/attendance.xlsx'
   output_path_prefix = '/sdcard/bjs/attendance'
output_file_path = outfilepath

def calculate_and_save_salaries(csv_content, output_path_prefix):
    print(f'{fyl}calc_salaries:start{frs}')
    att_data = create_attendance_sheet(csv_content, output_path=output_file_path)
    print(f'{fmg}calc_sals-att_data:\n{att_data}{frs}')

    # Read the CSV data
    csv_file = StringIO(csv_content)
    csv_reader = csv.reader(csv_file)

    # Store all employee data
    employee_data = {}

    for row in csv_reader:
        if not row:
           continue

        jobno = row[0]
        name  = row[1]
        employee_data[jobno] = {'name': name, 'attendance': set()}

        # Process dates in the format: date, time, status, date, time, status...
        for i in range(2, len(row), 3):
            if i + 2 >= len(row):
                break  # Ensure there are enough elements

            date_str = row[i]
            if not date_str:
               continue

            try:
                import datetime
                date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                employee_data[jobno]['attendance'].add(date_obj)
            except ValueError:
                print(f"Invalid date format found: {date_str}. Skipping.")
                continue

    # Save to file
    output_file = f"/sdcard/bjs/{output_path_prefix}-salary.txt"
    with open(output_file, 'w') as f:
        print(f'{fyl}output_file_date_naming{frs}: {output_date}')
        def datename(date_str, form):
            from datetime import datetime
            date_string = date_str
            date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
            dt_name = date_object.strftime(f'{form}')
            #print(day_name)
            return dt_name
        year = datename(output_date, '%Y')        
        monthname = datename(output_date, '%B')
        dayname = datename(output_date, '%A')
        dt = datename(output_date, '%d')
        print(f'year: {year}, month: {monthname}, day: {dayname}, date: {dt}')
        from datetime import datetime, timedelta

        init_date_str = output_date
        init_date = datetime.strptime(init_date_str, "%Y-%m-%d").date()
        
        end_date = init_date + timedelta(days=5)
        end_date = str(end_date)
        print(f'end_date: {end_date}')
        
        end_year = datename(end_date, '%Y')        
        end_mnt = datename(end_date, '%B')
        end_day = datename(end_date, '%A')
        end_dat = datename(end_date, '%d')
        print(f'endyear: {end_year}, endmonth: {end_mnt}, endday: {end_day}, enddate: {end_dat}')

        #for team, salaries in employee_salaries.items():
        for team, salaries in att_data.items():
            teamc = team.capitalize()
            f.write(f"Team: {team.capitalize()}\n") # Team header
            rownum = len(salaries)  # Set rownum to the number of members in the team
            subheaders = inspect.cleandoc(f'''
            title:SPPG Boga Jaya Santosa: Tanda Terima Pembayaran Gaji 
            subs:Tim {teamc} Periode [{year}] {monthname} {dt} - [{end_year}] {end_mnt} {end_dat}
            intro:
            rownum:{rownum}
            headers:No.,Nama{{char=34}},Gaji per hari,Jumlah hari kerja,Jumlah gaji yg diterima,Tanda tangan
            below headers:
            ''')
            f.write(f'{subheaders}\n')
            lsnum = 1
            for data in salaries:
                if 'leader' in data:
                   nama_leader = data['leader']
                   print(f"team {team} leader: {data['leader']}")
                   continue
                else:
                   nama_leader = ''
                print(f'current data in salaries: {data}')
                if data['name'] == 'Unknown':
                   print(f"{frd}skipping the Unknown({data['jobno']}){frs}")
                   continue
                f.write(f"data:[{data['jobno']}] {data['name']},{data['salary']},{data['total_attendance']},{data['total_salary']}\n")
                lsnum += 1

            outro = inspect.cleandoc(f'''
            lpos:
            lpos:Leader Tim {teamc}
            lpos:
            lpos:
            lpos:[{nama_leader}]
            cpos:
            cpos:Owner Dapur Boga Jaya Santosa
            cpos:
            cpos:
            cpos:[N.Yanti Yulianti S.Si., Apt.]
            rpos:Mengetahui,
            rpos:SPPI Boga Jaya Santosa
            rpos:
            rpos:
            rpos:[Muhammad Ikhsan Nur Zamzam, S.Pd.]
            ''')
            print(f'outro: {outro}')
            #sys.exit()
            f.write(outro)
            f.write("\n\n") # Add a newline between teams

    print(f"Salary data saved to {output_file}")
    year = os.path.basename(output_file).split('-')[0]
    month = os.path.basename(output_file).split('-')[1]
    os.system(f'rcopyto.py {output_file} gdcs:bjs/attendance/{year}/{month}')
    #input(f'press Enter'); sys.exit()
    
# Example usage (integrate into your existing script):
if __name__ == "__main__":
   try:
     if sys.argv[1] == '-h':
        usg()
        sys.exit()
   except Exception:
     pass
   create_attendance_sheet(csv_content, output_path=output_file_path)
   startdate = output_date
   calculate_and_save_salaries(csv_content, output_path_prefix=f'{output_date}-{sne}')
   os.system(f'bjssal.py {output_date}')
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Elapsed time: {elapsed_time} seconds")
   