

> **Message**: For transparency, I have inserted comments to accompany each functions. In the advent that the implementation to any of these files remain elusive, I'll do my best to incorporate more documentation/comments.
> 
> Please see the below in order to navigate the attached files!



GA-Lab is created mostly using Python, Qt Designer and PySide2 however I've also uploaded my Virtual Environment to provide more clarity on the multitude of modules and dependencies that were used.

# Reporting files:
> ```sh
> STAT_REV.py   ##STAT REV implementation 
> STAT_AUM.py   ##STAT AUM implementation
> EIB_AUM.py   ##EIB generation for STAT AUM 
> EIB_REV.py   ##EIB generation for STAT REV
> ```
>*STAT AUM and STAT REV are automatically generated. Both files are able to automatically detect whether there is error in file provided by Rev in addtion to calculating output. Moreover, references to cells are added in order to provide trails for the calculations.
>
> *EIB for AUM and REV are both contingent upon the STAT excel files output. The accounting date and all other fileds (ex: memo) are automatically adjusted. No intervention is needed.

> # Comparator:
> ```sh
> web.comparator.py  ##Implementation of comparator (Please have Java installed for use)
> 
> ```
> This file creates a table showing a side by side, line by line comparison of text with inter-line and intra-line change highlights. THe parser supports PDF, Excel and Word documents.
> 
>  # Cash Finder:
> ```sh
> beta (not yet written)  ##Implementation of Cash Finder 
> 
> ```
>As of now, implementation remains a challenge due to all emails being encrypted consequently impeding direct access to outlook emails via code however other methods will be explored to circumvent this momentary obstacle.  

> Function: This implementation should be able to analyze any Unreconciled Cash Items obtained from WKDAY and instantly identify and locate it's support(Email body, Email attachment, Wire request folder, etc)

# RUN FILE:
main.py



