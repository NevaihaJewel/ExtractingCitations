<h1>Extracting Facility Citations</h1>

<h2>Description</h2>
This Python program automates the retrieval of citation records for healthcare facilities from a public database. Using Selenium for web scraping and Pandas for data handling, the program searches for facilities listed in an Excel file, extracts the most recent citation data, and stores the results in a new spreadsheet.
<br></br>
<b>Key Features:</b>

- <b>Automated Search & Extraction:</b> Inputs a facility name, navigates through multiple web pages, and retrieves citation details.
- <b>Data Processing:</b> Reads facility names, phone numbers, and addresses from an Excel file and appends citation data.
- <b>Error Handling:</b> Implements exception handling to manage missing data, unresponsive elements, and timeouts.
- <b>Excel Integration:</b> Saves extracted information in a structured format for further analysis.

<h2>Languages Used</h2>

- <b>Python</b>

<h2>Environments Used</h2>

- <b>Google Chrome</b>
- <b>Visual Studio Code</b>

<h2>Project Walk-Through:</h2>

<p align="center">
The Program: Opens the website and searches the facility name on the first webpage<br/>
<img src="https://i.imgur.com/AWbehCa.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
The Program: Selects the facility on the second webpage and gathers citation details from the most recent year on the third webpage<br/>
<img src="https://i.imgur.com/TOo2s6s.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
The Program: Counts the number of citations on the fourth webpage then returning to the first webpage for the next facility<br/>
<img src="https://i.imgur.com/Sn3rimM.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
The Program: Collects all of the extracted data and stores it in a new Excel file<br/>
<img src="https://i.imgur.com/Rgmoc9F.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
  
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
