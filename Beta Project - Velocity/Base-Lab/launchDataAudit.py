import os
import sys as Sys
import platform

######The below launches an excel file to run 
def main(data_audit_type):
    system = platform.system() ##Windows or MAC
    launchscript = r""

    #######Script adapts to platform on which it is ran as well as launches different data audits based on the accrual in question###############
    if 'ADMIN' in data_audit_type.upper() and 'FEE' in data_audit_type.upper():
        launchscript = r"open -a 'Microsoft Excel' '/Users/sebastienstvil/Documents/Python/Python-DEV/Beta Project - Velocity/Base-Lab/Testing/Admin Fee accrual/Data_Audit_-_Spend_Categories.xlsx'" \
                    if system == 'Darwin' else r"open -a 'Microsoft Excel.app' '\\prod-corpfile\netshare\GA\000-Common Files\Virtual - GA Lab\cache\Templates\GA LAB Data Audit Spend Category.xlsx'"
    else:
        #############Replace condition below to reflect desired file when Adding new Data audits in the future###################
        launchscript = launchscript

    os.system(launchscript)

if __name__ == "__main__":
    main(data_audit_type)