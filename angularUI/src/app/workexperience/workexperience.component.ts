import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-workexperience',
  templateUrl: './workexperience.component.html',
  styleUrls: ['./workexperience.component.css']
})
export class WorkexperienceComponent implements OnInit {

  fullTimeTitle = 'IBM / Software Engineer for IBM’s internal Security and Compliance team';
  fullTimeDates = 'October 2016 - January 2018';
  fullTimeLocation = 'IBM Technology Campus, Damastown, Dublin ';
  fullTimeRole = 'This role was a follow on from my Graduate role on the same team in IBM, it was a full time permanent '
               + 'position. I continued to add new features and support the Inventory project that I worked on previously '
               + 'as a Graduate. I also took on some more responsibilities for other applications when the Inventory '
               + 'squad(Squad is a smaller team within our main Security Operations Services team) joined with the Reporting squad.';

  fullTimeProject = 'This project was made up of a IBM Cognos Analytics application, a Spring Boot application, and a DB2 '
                  + 'relational database. The Spring Boot application was used to make calls(REST,SOAP,JDBC) to some of the '
                  + 'other SOS squads tools(Vulnerability Scanning, Endpoint Manager, SIEM, Anti-Virus, Infrastructure) and '
                  + 'pull information from them so that it can be centralized in the DB2 database. This makes it easier for '
                  + 'Security Admins to track their security and compliance posture. Cognos Analytics Reports can be '
                  + 'generated from this information and sent to the Chief Information Security Officers for each of IBMs '
                  + 'Business Units. I worked on this project with an IBM Architect, Senior Software Engineer'
                  + ', and a Junior Software Engineer.';


  fullTimeAchievement1 = 'Setup and configured an SOS Domino Web Server environment, and helped to move the Inventory '
                        + 'application across from a different IBM infrastructure teams environment. ';
  fullTimeAchievement2 = 'Integrated Symantec Two Factor Authentication(2FA) into our Web application so managers could '
                        + 'request a temporary token and have it emailed to the user that is locked out. ';
  fullTimeAchievement3 = 'Worked with another Junior Software Engineer to automate publishing Subnets to our '
                        + 'Vulnerability Scanning tool so customers could process their own IPs to be scanned. ';
  fullTimeAchievement4 = 'Worked directly under a Project Manager to create a Vulnerability view in the Web UI so that '
                        + 'Security Admins could easily see which Vulnerabilities are affecting their Systems. ';
  fullTimeAchievement5 = 'Helped to train and wrote training documentation for 2 new Junior Engineers.';

  fullTimeSkills = 'SQL (DB2), Apache Web Server, Spring Boot, JDBC, Git, Bash, Web Services, Spring Tool Suite';

  graduateTitle = 'IBM / Information Communication Technology Graduate';
  graduateDates = 'January 2016 - October 2016';
  graduateLocation = 'IBM Technology Campus, Damastown, Dublin';
  graduateRole = 'I started my career at IBM on an 11 month ICT contract with the Security Operational Services team and '
                + 'was moved onto a permanent role after 10 months. This is an internal security tooling team that helps '
                + 'to manage the security and compliance of other IBM teams. ';

  graduateProject = 'This project involved making the same functionality of a Lotus Notes Thick client application available in '
                  + 'the Web. The Inventory management tool enables SOS customers(Internal IBM teams) to track and '
                  + 'update security/compliance information about their Servers/Network Devices/Virtual IPs/Storage Controllers'
                  + '/Expansion Units/Vlans/Subnets/Applications. I worked together with a distinguished IBM Software Architect '
                  + 'on this project.';


  graduateAchievement1 = 'Found a bug that was application wide and causing the page state to be lost. '
                        + 'Fixing this bug reduced our customer tickets dramatically (10%-20%).';
  graduateAchievement2 = 'Further developed and Maintained a REST API which was built using Java Servlets '
                        + 'and IBMs Java Json library.';
  graduateAchievement3 = 'Added excel Import/Export functionality to Web UI using Apache POI, this involved '
                        + 'adapting legacy code from Notes Client to work in the Web.';

  graduateSkills = 'Skills:​ Java, NoSQL(Notes Document Based), XPages(technology built on JavaServer Faces), Domino Web Server'
                  + ', JQuery, Bootstrap, Dojo Toolkit, JavaScript, AJAX, Eclipse, Linux, Windows, Kernel Virtual Machine Manager';

  constructor() { }

  ngOnInit() {
  }

}
