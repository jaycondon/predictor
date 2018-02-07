import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-education',
  templateUrl: './education.component.html',
  styleUrls: ['./education.component.css']
})
export class EducationComponent implements OnInit {

  educationTitle = 'Carlow Institute of Technology / BSc (Hons) Software Development - Attained 2.2';
  educationDates = 'September 2011 - May 2015​';
  educationLocation = 'Kilkenny Road, Carlow';

  projectTitle = 'Final Year Project / Electronic Scratch Cards';
  projectBackground = 'The goal of this project was to build a system that would electronically replicate the national lottery '
                    + 'scratch cards bought in shops. This involved researching application security in particular OWASP top 10 '
                    + 'and also PCI compliance because I was dealing with Credit/Debit cards. Single handedly worked on this '
                    + 'project under the guidance of my college lecturer.';

  projectGithubUrl = 'https://github.com/jaycondon/Escratchcard';

  educationAchievement1 = 'Encrypting the communication from server to browser using Transport Layer Security 1.2.';
  educationAchievement2 = 'Interfacing with Paypal’s API to allow credit/debit card payments.';
  educationAchievement3 = 'Developed using Python, built on the Flask framework, and deployed on Heroku hosting.';

  educationProjectUrl = 'http://electronicscratchcardgame.herokuapp.com/login';
  educationSkills = 'Python, Flask, Bootstrap, Heroku, Git';

  constructor() { }

  ngOnInit() {
  }

}
