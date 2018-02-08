import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-personalinformation',
  templateUrl: './personalinformation.component.html',
  styleUrls: ['./personalinformation.component.css']
})
export class PersonalinformationComponent implements OnInit {

  name = 'John Condon';
  address = ​'Dublin, Ireland';
  email =​ 'johnnycndn@gmail.com';
  linkedIn = 'https://www.linkedin.com/in/johnnycondon';
  github ​= 'https://github.com/jaycondon';

  personalStatement = 'Enthusiastic Software Engineer with excellent troubleshooting skills and a good knowledge of web '
                  + 'application development principles across all architectural layers: Database, Business, and Presentation. '
                  + 'Interested in Cyber Security and working towards a CISSP(Certified Information Systems Security '
                  + 'Professional) certificate. Looking for a new challenge to further develop skills. I am available to start '
                  + 'work immediately.';


  constructor() { }

  ngOnInit() {
  }

}
