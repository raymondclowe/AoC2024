with open('day2.txt', 'r') as file:
    lines = file.readlines()

reports = []
for line in lines:
    splitted = line.split()
    integed = [int(i) for i in splitted]
    reports.append(integed)

safe_reports = 0

def first_check(report):
    # print(report, sorted(report), report[::-1])
    if (sorted(report) == report) or (sorted(report) == report[::-1]):
        return True
    else:
        return False
    
def second_checK(report):
    for i in range(len(report)-1):
        if not( abs(report[i] - report[i+1]) in [1,2,3] ):
            return False
    
    return True

def report_checker(report):
    for i in range(len(report)):
        truncated_report = report.copy()
        del truncated_report[i]
        if first_check(truncated_report) and second_checK(truncated_report):
            return True      
        
    return False

for report in reports:
    # print(report, first_check(report), second_checK(report))
    if report_checker(report):
        
        safe_reports += 1

print(safe_reports)
