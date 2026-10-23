#!/data/data/com.termux/files/usr/bin/python

import os, sys, time, inspect, xlsxwriter
from ansicolors import *

# Script metadata
sdn = os.path.dirname(sys.argv[0])
sbn = os.path.basename(sys.argv[0])
sne = os.path.splitext(sbn)[0]
sdbne = f'{sdn}/{sne}'
home = '/data/data/com.termux/files/home'
hbak = home + '/bak'
hbin = '/bin'
verbose = False

# Start timing
start_time = time.time()

import osl
osl.osl(sys.argv[0])  # Example: symlink a specific file
for message in osl.info:
    print(message)

# Command-line arguments
args = sys.argv[1:]
jargs = ' '.join(args).strip()

def usg():
    """Prints the usage instructions for the script."""
    usg = inspect.cleandoc(f'''
    alias: {fgr} {frs}
 function: {fyl} {frs}
    usage: {frs} {sbn} [argument]
    ''')
    print(f'{usg}')
    
""" this is how the salary file contents looks like
the field names: {jobno},{name},{salary},{attendances},{total_salary}
 
Team: Prepare
01,Entin Sukaesih,100,5,500
02,Fikri Fathurohman,100,5,500
03,Mulyana Santosa Machyar SE,100,5,500
04,Nonoy Nurjanah,100,5,500
05,Oon Wartia,100,5,500
06,Sopiah,100,5,500
07,Yuli Yanti,100,5,500
08,Galih Ramanda,100,5,500

Team: Produksi
09,Agus Rohendi,100,5,500
10,Esih,100,5,500
"""
import re

def create_excel_from_salary_file(salary_file_path, workbook, sheet_name):
    """
    Reads data from a salary file, processes it, and writes it to an Excel sheet.
    """
    try:
        with open(salary_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: Salary file not found at {salary_file_path}")
        return False
    except Exception as e:
        print(f"Error reading salary file: {e}")
        return False

    # Split the content into teams
    teams = re.split(r'\n(?=Team:)', content)
    
    # Iterate through each team
    for team_index, team_data in enumerate(teams):
        # Extract team name
        team_match = re.match(r'Team: (.*)', team_data)
        if team_match:
            team_name = team_match.group(1).strip()
        else:
            team_name = f"Team {team_index + 1}"

        # Split the team data into lines
        lines = team_data.splitlines()

        # Find the line containing the field names
        field_names_line = next((line for line in lines if "field names:" in line), None)
        if field_names_line:
            # Extract field names from the line
            field_names_match = re.search(r'{(.*?)}', field_names_line)
            if field_names_match:
                field_names_str = field_names_match.group(1)
                field_names = [name.strip() for name in field_names_str.split(',')]
            else:
                field_names = ['jobno', 'name', 'salary', 'attendances', 'total_salary']
        else:
            field_names = ['jobno', 'name', 'salary', 'attendances', 'total_salary']

        # Extract the data lines (skipping the field names line and any other non-data lines)
        data_lines = [line for line in lines if line and not line.startswith('Team:') and not "field names:" in line]

        # Add a new worksheet for each team
        worksheet = workbook.add_worksheet(f"{sheet_name}_{team_name}")

        # Write the headers
        for col_num, field_name in enumerate(field_names):
            worksheet.write(0, col_num, field_name)

        # Write the data
        for row_num, line in enumerate(data_lines):
            values = [value.strip() for value in line.split(',')]
            for col_num, value in enumerate(values):
                worksheet.write(row_num + 1, col_num, value)
    return True
    
def create_excel_from_file(file_path):
    """
    Creates Excel files from a text file, with each block becoming a separate sheet.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    blocks = content.split('\n\n')

    output_dir = f'/sdcard/{sne}'
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except OSError as e:
            print(f"Error creating directory {output_dir}: {e}")
            return
    import datetime
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%y%m%d-%H%M%S")
    print(timestamp)
    #filename = os.path.join(output_dir, f"{sne}.xlsx")
    filename = os.path.join(output_dir, f"{sne}_{timestamp}.xlsx")
    try:
        workbook = xlsxwriter.Workbook(filename)

        for block_num, block in enumerate(blocks):
            titles = []
            subtitles = []
            intro_lines = []
            headers_str = None
            subheader_str = None
            content_lines = []
            lpos_lines = []
            cpos_lines = []
            rpos_lines = []
            sheetname = None
            default_rows = 13  # Initialize default_rows

            for line in block.splitlines():
                line = line.strip()
                if line.startswith('title:'):
                    titles.append(line[len('title:'):].strip())
                elif line.startswith('subs:'):
                    subtitles.append(line[len('subs:'):].strip())
                elif line.startswith('intro:'):
                    intro_lines.append(line[len('intro:'):].strip())
                elif line.startswith('headers:'):
                    headers_str = line[len('headers:'):].strip()
                elif line.startswith('below headers:'):
                    subheader_str = line[len('below headers:'):].strip()
                elif line.startswith('content:'):
                    content_lines.append(line[len('content:'):].strip())
                elif line.startswith('lpos:'):
                    lpos_lines.append(line[len('lpos:'):].strip())
                elif line.startswith('cpos:'):
                    cpos_lines.append(line[len('cpos:'):].strip())
                elif line.startswith('rpos:'):
                    rpos_lines.append(line[len('rpos:'):].strip())
                elif line.startswith('sheetname:'):
                    sheetname = line[len('sheetname:'):].strip()
                elif line.startswith('rownum:'):
                    try:
                        default_rows = int(line[len('rownum:'):].strip())
                    except ValueError:
                        print(f"Invalid rownum value: {line[len('rownum:'):].strip()}. Using default value 13.")

            if titles and headers_str:
                headers = [h.strip() for h in headers_str.split(',')]
                subheaders = [sh.strip() for sh in (subheader_str.split(',') if subheader_str else [])]

                sheet_name = sheetname if sheetname else f"Sheet{block_num + 1}"
                sheet_name = sheet_name[:31] if len(sheet_name) > 31 else sheet_name

                worksheet = workbook.add_worksheet(sheet_name)

                # Pass default_rows to write_excel_sheet
                write_excel_sheet(workbook, worksheet, titles, subtitles, intro_lines, headers, subheaders, content_lines, lpos_lines, cpos_lines, rpos_lines, default_rows=default_rows)

        workbook.close()
        print(f"Excel file '{filename}' created successfully with multiple sheets.")

    except Exception as e:
        print(f"Error creating Excel file: {e}")

def write_excel_sheet(workbook, worksheet, titles, subtitles, intro_lines, headers, subheaders, content_lines, lpos_lines, cpos_lines, rpos_lines, default_rows):
    """
    Writes data to a single Excel sheet.
    """

    # Define formats
    title_format = workbook.add_format({
        'font_name': 'Inconsolata',
        'bold': True,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14})

    subtitle_format = workbook.add_format({
        'font_name': 'Inconsolata',
        'bold': False,
        'italic': False,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 12})

    intro_format = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True})

    header_format = workbook.add_format({
        'bold': True,
        'align': 'center',
        'text_wrap': True,
        'valign': 'vcenter'})

    subheader_format = workbook.add_format({
        'bold': False,
        'align': 'center',
        'text_wrap': True,
        'valign': 'vcenter'})

    lpos_format = workbook.add_format({'align': 'center', 'text_wrap': True})  # Left align
    cpos_format = workbook.add_format({'align': 'center', 'text_wrap': True})
    rpos_format = workbook.add_format({'align': 'center', 'text_wrap': True})
    content_format = workbook.add_format({'align': 'left', 'valign': 'top', 'text_wrap': True})
    numbering_format = workbook.add_format({'align': 'center'})

    # New format for zigzag numbering
    zigzag_left_format = workbook.add_format({'align': 'left', 'valign': 'top'})
    zigzag_center_format = workbook.add_format({'align': 'center', 'valign': 'top'})

    # Store maximum width for each column
    column_widths = {}

    # Initial row number
    row_num = 0

    # Determine the maximum number of columns
    max_cols = max(len(headers), len(subheaders) if subheaders else 0)

    # Write the titles (merged and centered)
    for title in titles:
        if max_cols > 1:  # Prevent merging if only 1 column
            worksheet.merge_range(row_num, 0, row_num, max_cols - 1, title, title_format)
        else:
            worksheet.write(row_num, 0, title, title_format)
        row_num += 1

    # Write the subtitles (merged and centered)
    for subtitle in subtitles:
        if subtitle:
            if max_cols > 1:  # Prevent merging if only 1 column
                worksheet.merge_range(row_num, 0, row_num, max_cols - 1, subtitle, subtitle_format)
            else:
                worksheet.write(row_num, 0, subtitle, subtitle_format)
            row_num += 1

    # Write the intro lines
    if intro_lines:
        # Find the row that was last written (title or subtitle)
        last_written_row = row_num -1

        for intro_line in intro_lines:
            if max_cols > 1:  # Prevent merging if only 1 column
                worksheet.merge_range(row_num, 0, row_num, max_cols - 1, intro_line.replace('\\n', '\n'), intro_format)
            else:
                worksheet.write(row_num, 0, intro_line.replace('\\n', '\n'), intro_format)
            row_num += 1

    # Determine header row
    header_row = row_num
    subheader_row = header_row + 1 if subheaders else header_row  # Subheaders will be written below headers

    # Write the headers and handle merged cells
    col_num = 0
    header_col_start = 0  # Track the starting column for merged headers
    tanda_tangan_col = None # Track the column index of 'Tanda tangan'

    for i, header in enumerate(headers):
        merge_count = 1
        header_text = header  # Original header text
        explicit_width = None

        if '{char=' in header and '}' in header:
            try:
                start_index = header.find('{char=') + len('{char=')
                end_index = header.find('}', start_index)
                width_value = int(header[start_index:end_index])
                explicit_width = width_value
                header_text = header[:header.find('{char=')].strip()  # Text before the width specifier
                header = header_text # use it later
            except ValueError:
                pass # If the value inside {char= } is not a number, ignore it

        if header and header.endswith(')') and '(' in header:
            try:
                merge_count = int(header[header.rfind('(') + 1: -1])
                header = header[:header.rfind('(')].strip()  # Remove the (n) from header
            except ValueError:
                pass  # If the value inside () is not a number, ignore it

        #Corrected condition:  Check if merge_count is greater than 1 before merging
        if merge_count > 1:
            worksheet.merge_range(header_row, header_col_start, header_row, header_col_start + merge_count - 1, header, header_format)
        else:
            worksheet.write(header_row, header_col_start, header, header_format)
        
        # Determine column width
        if explicit_width is not None:
            column_width = explicit_width
        else:
            column_width = len(header_text) + 2

        column_widths[header_col_start] = max(column_widths.get(header_col_start, 0), column_width)

        # Set column width for merged cells
        for j in range(header_col_start, header_col_start + merge_count):
            column_widths[j] = column_widths[header_col_start]

        if header == 'Tanda tangan':
            tanda_tangan_col = header_col_start

        header_col_start += merge_count
        col_num += 1

    # Write zigzag numbering under 'Tanda tangan'
    if tanda_tangan_col is not None:
        number = 1
        zigzag_row = header_row + 1 if not subheaders else subheader_row + 1

        # Calculate max_lines *before* the loop
        num_lpos = len(lpos_lines)
        num_cpos = len(cpos_lines)
        num_rpos = len(rpos_lines)
        max_lines = max(num_lpos, num_cpos, num_rpos)

        for i in range(default_rows):  # Write numbers to match the table rows
            number_str = f"{number}."
            format = zigzag_left_format if number % 2 != 0 else zigzag_center_format
            worksheet.write(zigzag_row + i, tanda_tangan_col, number_str, format)
            number += 1

    # Write subheaders
    if subheaders:
        col_num = 0
        for subheader in subheaders:
            worksheet.write(subheader_row, col_num, subheader, subheader_format)
            column_widths[col_num] = max(column_widths.get(col_num, 0), len(subheader) + 2)
            col_num += 1
        row_num = subheader_row + 1 #Move past subheader row
    else:
        row_num = header_row + 1

    # Write content lines and numbering
    for i in range(default_rows):
        # Write row number
        worksheet.write(row_num + i, 0, i + 1, numbering_format)
        #Write content, if any
        if i < len(content_lines):
            # Treat every \n as newline
            content = content_lines[i].replace('\\n', '\n')
            worksheet.write(row_num + i, 1, content, content_format)
            column_widths[1] = max(column_widths.get(1, 0), len(content) + 2)

        # Set the row height to approximately 2 rows
        worksheet.set_row(row_num + i, 30)  # 30 is roughly double the default height

    row_num += default_rows  # Move past data rows

    # Write positioned lines sequentially, occupying 100% of workbook width
    max_col = max(len(headers), len(subheaders) if subheaders else 0)
    start_row = header_row + 1 if not subheaders else subheader_row + 1 + default_rows  # start after content

    if intro_lines:
        start_row = row_num - max(len(content_lines), 1) + 1  # place after intro
        row_num = start_row

    num_lines = max(len(lpos_lines), len(cpos_lines), len(rpos_lines))

    for i in range(num_lines):
        col = 0
        if i < len(lpos_lines):
            content = lpos_lines[i].replace('\\n', '\n')
            worksheet.merge_range(start_row, col, start_row, col + 1, content, lpos_format)
            col += 2
        else:
            col += 2

        if i < len(cpos_lines):
            content = cpos_lines[i].replace('\\n', '\n')
            worksheet.merge_range(start_row, col, start_row, col + 1, content, cpos_format)
            col += 2
        else:
            col += 2

        if i < len(rpos_lines):
            content = rpos_lines[i].replace('\\n', '\n')
            worksheet.merge_range(start_row, col, start_row, col + 1, content, rpos_format)
            col += 2
        else:
            col += 2

        worksheet.set_row(start_row, 16)
        start_row += 1
        row_num = start_row

    # Set column widths at the end
    for col_num, width in column_widths.items():
        worksheet.set_column(col_num, col_num, width)

# Main execution
file_path = f'{sne}.txt'
create_excel_from_file(file_path)

if __name__ == '__main__':
    try:
        if sys.argv[1] == '-h':
            usg()
            sys.exit()
    except Exception:
        pass

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")