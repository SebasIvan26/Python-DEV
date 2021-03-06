

> **Message**: For transparency, I have inserted comments to accompany each functions. In the advent that the implementation to any of these files remain elusive, I'll do my best to incorporate more documentation/comments.
> 
> Please see the below in order to navigate the attached files!

>![GA Lab preview](https://user-images.githubusercontent.com/56465638/122435636-2a67ed80-cf66-11eb-81e4-a8986b4d0852.jpg)


GA-Lab is created mostly using Python, Qt Designer and PySide2 however I've also uploaded my Virtual Environment to provide more clarity on the multitude of modules and dependencies that were used.

# Reporting analysis automation:
> ```sh
> Analysis and extraction of WTC pools data
> STAT_REV.py   ##STAT REV implementation 
> STAT_AUM.py   ##STAT AUM implementation
> EIB_AUM.py   ##EIB generation for STAT AUM 
> EIB_REV.py   ##EIB generation for STAT REV
> ```
>*STAT AUM and STAT REV are automatically generated. Both files are able to automatically detect whether there is an error in the file provided by Rev in addition to calculating the output. Moreover, references to cells are added in order to provide trails for the calculations.
>
> *EIB for AUM and REV are both contingent upon the STAT excel files output. The accounting date and all other fileds (ex: memo) are automatically adjusted. No intervention is needed.

> # Admin Fee Accrual:
> ```sh
> #Analysis of Spend Category, Currency etc....
> #Pattern recognition used to generate worktags
> 
> Luxembourg Admin Fee accrual   ##EIB generation
> WFS Admin Fee accrual   ##EIB generation
> ```

> # WTC Cash Flow File:
> ```sh
> Generates insights into NB, LB, OCF based on data originating from Revport

>Recognizes quarter and assigns appropriate basis points. No manual intervention

> ```

> # Comparator:
> ```sh
> web.comparator.py  ##Implementation of comparator (Please have Java installed for use)
> 

> To install Java ---> Software Center -----> type "Java" in search area"----> Select "Oracle JAVA 8"
> 
> ```
> This file creates a table showing a side by side, line by line comparison of text with inter-line and intra-line change highlights. The parser supports PDF, Excel and Word documents.
> 

>  # Cash Finder:
> ```sh
> beta (not yet written)  ##Implementation of Cash Finder 
> 
> ```
>As of now, the implementation remains a challenge due to all emails being encrypted consequently impeding direct access to outlook emails via code however other methods will be explored to circumvent this momentary obstacle.  

> Function: This implementation should be able to analyze any Unreconciled Cash Items obtained from WKDAY and instantly identify and locate the origins of their support(Email body, Email attachment, Wire request folder, etc)
> 
# Accessing WD (beta):
> ```sh
> AccessingWD.py  ##Implementation of Accessing WD
> 
> ```
> The attached code offers the ability to directly connect to Workday's API from GA-Lab using web services. This means that any CR will be directly accessible from the app by completely bypassing the website. Any change in the prompts such as (date, entity, etc) can be easily accessed by modifying the link. 
> ex: www.wd.com/Import/Singapore/0131 --> Altough the fields in the links corresponding to the prompts won't be quite clearly delineated as in this example, there will be ways to access a specific report by manipulating the link so that its output reflects the desired report.
> 
> **Where does this lead to ?** 
> 
> GA-Lab would not be the only platform capable of accessing the report within the confines of a desktop App but also Microsoft Excel. This would signify that reports that are typically copy/pasted innumerable times such as the TB on the recon template fall in that category thereby giving ground to further optimize the recon template. The only existing drawback, based on my current tests/understanding, is the unavoidable fact that only advanced reports are accessible through workday services. As it stands TB is a composite report, therefore having recourse to such a feature would require deliberate efforts in transcribing that CR(composite) to a CR(advanced).
> 
> Lastly, we should find comfort that in the long run, such efforts will prove to be beneficial when considering the cumulative benefits of time saved and error prevention coupled with the now possiblity of easily applying such feature in other areas having tested and implemented it prior. 
> 
> 
> Note: execution viable however on hold per meeting with D. Ranfdord due to control liabilty from non-IT supported apps which have been a target of InfoSec and other governing groups.

>####Another approach to the above is by accessing a database containing all the expected information. On one end, the data would not be a live stream however the data can be frequently updated to simulate such effect. Lastly, the complexity of this implementation can be subtantially lower. 

# RUN FILE:
main.py



